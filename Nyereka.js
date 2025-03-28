document.getElementById("security-form").addEventListener("submit", async function(event) {
    event.preventDefault();
    let email = document.getElementById("email").value;
    let resultBox = document.getElementById("result");

    resultBox.innerHTML = "🔍 Checking security...";

    try {
        let response = await fetch("http://localhost:5000/api/security-check", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ email })
        });

        let data = await response.json();

        if (data.error) {
            resultBox.innerHTML = `❌ ${data.error}`;
            return;
        }

        if (data.hasSecurityIssues) {
            resultBox.innerHTML = `<p>⚠️ Security issues found for ${email}</p>
                                   <ul>${data.issues.map(issue => `<li>${issue.description}</li>`).join('')}</ul>`;
        } else {
            resultBox.innerHTML = `✅ No major security issues detected for ${email}`;
        }
    } catch (error) {
        resultBox.innerHTML = "❌ Failed to check security. Please try again.";
    }
});
