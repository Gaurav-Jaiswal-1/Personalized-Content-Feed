document.addEventListener('DOMContentLoaded', function() {
  // Adjust the API URL if needed
  const apiUrl = "http://localhost:5000/content/recommend";

  // Example user ID; in a real-world scenario, get this from your authentication flow
  const payload = { user_id: "101" };

  fetch(apiUrl, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
  })
  .then(response => response.json())
  .then(data => {
      console.log("Recommended content:", data);
      // Populate the popup UI with the recommended content
      const contentDiv = document.getElementById("content");
      data.forEach(item => {
          const p = document.createElement("p");
          p.textContent = item.title;
          contentDiv.appendChild(p);
      });
  })
  .catch(error => console.error("Error:", error));
});
