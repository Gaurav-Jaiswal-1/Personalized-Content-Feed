chrome.storage.onChanged.addListener((changes, area) => {
  if (area === "sync" && changes.youtubeKeywords) {
      console.log("🔄 Keywords updated, reloading YouTube...");

      chrome.tabs.query({ url: "https://www.youtube.com/*" }, (tabs) => {
          tabs.forEach(tab => {
              chrome.scripting.executeScript({
                  target: { tabId: tab.id },
                  func: () => location.reload()
              });
          });
      });
  }
});
