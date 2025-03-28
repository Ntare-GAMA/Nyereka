document.getElementById("security-form").addEventListener("submit", function(event) {
    event.preventDefault();
    let email = document.getElementById("email").value;
    let resultBox = document.getElementById("result");

    // Simulating security check
    let hasIssues = Math.random() > 0.5;
    if (hasIssues) {
        resultBox.innerHTML = `<p>⚠️ Security issues found for ${email}</p>
                               <ul>
                                   <li>Unverified device detected</li>
                                   <li>Suspicious login activity</li>
                               </ul>`;
    } else {
        resultBox.innerHTML = `<p>✅ No major security issues for ${email}</p>`;
    }

    resultBox.classList.remove("hidden");
});
