function getStoredKeywords(callback) {
    chrome.storage.sync.get(["youtubeKeywords"], (data) => {
        callback(data.youtubeKeywords || []);
    });
}

function rearrangeYouTubeContent() {
    getStoredKeywords((keywords) => {
        if (!keywords.length) return;

        let videoContainers = document.querySelectorAll("ytd-rich-item-renderer, ytd-video-renderer, ytd-grid-video-renderer");
        let matchingVideos = [];
        let nonMatchingVideos = [];

        videoContainers.forEach((video) => {
            let titleElement = video.querySelector("#video-title");
            if (!titleElement) return;

            let title = titleElement.innerText.toLowerCase();
            if (keywords.some(keyword => title.includes(keyword.toLowerCase()))) {
                matchingVideos.push(video);
            } else {
                nonMatchingVideos.push(video);
                video.style.display = 'none'; // Hide irrelevant videos
            }
        });

        let parentContainer = document.querySelector("ytd-section-list-renderer");
        if (parentContainer) {
            matchingVideos.forEach(video => parentContainer.prepend(video));
            console.log("✅ Moved relevant videos to the top");
        }
    });
}

// Observe for changes and reapply filtering
let observer = new MutationObserver(() => {
    setTimeout(rearrangeYouTubeContent, 500);
});

function startObserving() {
    let feedContainer = document.querySelector("ytd-page-manager");
    if (feedContainer) {
        observer.observe(feedContainer, { childList: true, subtree: true });
        console.log("✅ MutationObserver started.");
    } else {
        console.warn("⚠️ YouTube feed not found. Retrying...");
        setTimeout(startObserving, 500);
    }
}

// Run when the page loads
window.addEventListener('load', function () {
    console.log("✅ content.js is running on YouTube!");
    rearrangeYouTubeContent();
    startObserving();
    
    // Auto-scroll to ensure all videos load
    let scrollInterval = setInterval(() => {
        window.scrollBy(0, 1000);
        if (document.documentElement.scrollHeight - window.scrollY <= window.innerHeight) {
            clearInterval(scrollInterval);
        }
    }, 1000);
});


fetch("http://localhost:5000/recommend?query=" + encodeURIComponent(userInput))
    .then(response => response.json())
    .then(data => {
        let videos = document.querySelectorAll("ytd-video-renderer");
        videos.forEach(video => {
            let title = video.querySelector("#video-title").innerText.toLowerCase();
            if (!data.recommended_titles.includes(title)) {
                video.style.display = 'none';
            }
        });
    })
    .catch(error => console.error("❌ Error fetching recommended videos:", error));
