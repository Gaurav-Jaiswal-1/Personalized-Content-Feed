document.addEventListener("DOMContentLoaded", () => {
  const keywordInput = document.getElementById("keyword");
  const saveKeywordBtn = document.getElementById("saveKeyword");
  const keywordList = document.getElementById("keywordList");
  const clearKeywordsBtn = document.getElementById("clearKeywords");

  // Load saved keywords
  function updateKeywordList() {
      chrome.storage.sync.get("youtubeKeywords", (data) => {
          let keywords = data.youtubeKeywords || [];
          keywordList.innerHTML = "";

          keywords.forEach((keyword) => {
              let li = document.createElement("li");
              li.textContent = keyword;

              let removeBtn = document.createElement("button");
              removeBtn.textContent = "❌";
              removeBtn.onclick = function() {
                  removeKeyword(keyword);
              };

              li.appendChild(removeBtn);
              keywordList.appendChild(li);
          });
      });
  }

  // Add keyword to storage
  saveKeywordBtn.addEventListener("click", () => {
      const keyword = keywordInput.value.trim().toLowerCase();
      if (!keyword) return;

      chrome.storage.sync.get("youtubeKeywords", (data) => {
          let keywords = data.youtubeKeywords || [];
          if (!keywords.includes(keyword)) {
              keywords.push(keyword);
              chrome.storage.sync.set({ "youtubeKeywords": keywords }, () => {
                  updateKeywordList();
                  notifyContentScript(); // Reload YouTube to apply changes
              });
          }
      });

      keywordInput.value = ""; // Clear input after saving
  });

  // Remove keyword from storage
  function removeKeyword(keyword) {
      chrome.storage.sync.get("youtubeKeywords", (data) => {
          let keywords = data.youtubeKeywords || [];
          keywords = keywords.filter((k) => k !== keyword);
          chrome.storage.sync.set({ "youtubeKeywords": keywords }, () => {
              updateKeywordList();
              notifyContentScript(); // Reload YouTube after removal
          });
      });
  }

  // Clear all keywords
  clearKeywordsBtn.addEventListener("click", () => {
      chrome.storage.sync.set({ "youtubeKeywords": [] }, () => {
          updateKeywordList();
          notifyContentScript(); // Reload YouTube after clearing all
      });
  });

  // Notify content script to reload YouTube
  function notifyContentScript() {
      chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
          if (tabs[0]) {
              chrome.scripting.executeScript({
                  target: { tabId: tabs[0].id },
                  func: () => {
                      window.location.reload();
                  }
              });
          }
      });
  }

  // Load the list on popup open
  updateKeywordList();
});
