document.getElementById("video-form").addEventListener("submit", function (e) {
  e.preventDefault();

  let youtubeUrl = document.getElementById("youtube-url").value;
  console.log("Submitting YouTube URL: " + youtubeUrl);

  // Show the spinner
  let spinner = document.getElementById("loading-spinner");
  spinner.style.display = "block";

  // Hide the video element initially
  let videoElement = document.getElementById("video");
  videoElement.style.display = "none";

  fetch("/process", {
    method: "POST",
    body: new URLSearchParams({
      youtube_url: youtubeUrl,
    }),
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Failed to process the video.");
      }
      return response.blob();
    })
    .then((data) => {
      console.log("Received processed video.");
      videoElement.src = URL.createObjectURL(data);
      videoElement.style.display = "block";
      videoElement.load();
      videoElement.play();
    })
    .catch((error) => {
      console.error("Error during processing:", error);
      alert("An error occurred while processing your video. Please try again.");
    })
    .finally(() => {
      // Hide the spinner
      spinner.style.display = "none";
    });
});
