document.addEventListener("DOMContentLoaded", () => {
    const keywordInput = document.getElementById("keyword");
    const saveKeywordBtn = document.getElementById("saveKeyword");
    const keywordList = document.getElementById("keywordList");
    const clearKeywordsBtn = document.getElementById("clearKeywords");

    function updateKeywordList() {
        chrome.storage.sync.get("youtubeKeywords", (data) => {
            let keywords = data.youtubeKeywords || [];
            keywordList.innerHTML = "";

            keywords.forEach((keyword) => {
                let li = document.createElement("li");
                li.textContent = keyword;

                let removeBtn = document.createElement("button");
                removeBtn.textContent = "❌";
                removeBtn.onclick = () => removeKeyword(keyword);

                li.appendChild(removeBtn);
                keywordList.appendChild(li);
            });
        });
    }

    saveKeywordBtn.addEventListener("click", () => {
        let newKeyword = keywordInput.value.trim().toLowerCase();
        if (!newKeyword) return;

        chrome.storage.sync.get("youtubeKeywords", (data) => {
            let keywords = data.youtubeKeywords || [];
            if (!keywords.includes(newKeyword)) {
                keywords.push(newKeyword);
                chrome.storage.sync.set({ youtubeKeywords: keywords }, () => {
                    updateKeywordList();
                    notifyContentScript();
                    keywordInput.value = ""; 
                });
            }
        });
    });

    function removeKeyword(keyword) {
        chrome.storage.sync.get("youtubeKeywords", (data) => {
            let keywords = data.youtubeKeywords || [];
            keywords = keywords.filter(k => k !== keyword);
            chrome.storage.sync.set({ youtubeKeywords: keywords }, () => {
                updateKeywordList();
                notifyContentScript();
            });
        });
    }

    clearKeywordsBtn.addEventListener("click", () => {
        chrome.storage.sync.set({ youtubeKeywords: [] }, () => {
            updateKeywordList();
            notifyContentScript();
        });
    });

    function notifyContentScript() {
        chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
            if (tabs.length > 0 && tabs[0].id) {
                chrome.scripting.executeScript({
                    target: { tabId: tabs[0].id },
                    func: () => {
                        window.location.reload(); 
                    }
                });
            }
        });
    }

    updateKeywordList();
});
