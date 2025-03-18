document.getElementById("name").addEventListener("input", function() {
    document.getElementById("greeting").textContent = "Hello, " + this.value + "!";
});

function processText() {
    let text = document.getElementById("text").value;
    let voice = document.getElementById("voice").value;
    let age = document.getElementById("age").value;
    let speed = document.getElementById("speed").value;

    fetch("/process", {
        method: "POST",
        body: new URLSearchParams({ text, voice, age, speed }),
        headers: { "Content-Type": "application/x-www-form-urlencoded" }
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("correctedText").textContent = data.corrected_text;
        document.getElementById("audioSource").src = data.audio_url;
        document.getElementById("audioPlayer").load();
    });
}