// Function to filter YouTube content
function filterContent() {
  chrome.storage.local.get("blockedKeywords", (data) => {
      const blockedKeywords = data.blockedKeywords || [];
      if (blockedKeywords.length === 0) return;

      document.querySelectorAll("ytd-video-renderer, ytd-grid-video-renderer").forEach((video) => {
          const titleElement = video.querySelector("#video-title");
          if (titleElement) {
              const titleText = titleElement.innerText.toLowerCase();
              if (blockedKeywords.some(keyword => titleText.includes(keyword.toLowerCase()))) {
                  video.style.display = "none";
              }
          }
      });
  });
}

// Run filtering initially and on mutations
const observer = new MutationObserver(filterContent);
observer.observe(document.body, { childList: true, subtree: true });

// Initial filtering
filterContent();


chrome.storage.sync.get("youtubeKeywords", (data) => {
  let blockedKeywords = data.youtubeKeywords || [];
  
  function filterVideos() {
      let videos = document.querySelectorAll("#video-title");
      videos.forEach(video => {
          let title = video.innerText.toLowerCase();
          if (blockedKeywords.some(keyword => title.includes(keyword))) {
              video.closest("ytd-video-renderer").style.display = "none";
          }
      });
  }

  setInterval(filterVideos, 3000); // Run every 3 seconds to check new content
});
