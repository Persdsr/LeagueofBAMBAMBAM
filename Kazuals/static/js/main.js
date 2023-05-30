
let mainImageContainer = document.getElementById("mainImageContainer");
let thumbnailContainer = document.getElementById("thumbnailContainer");

mainImageContainer.addEventListener("click", function() {
  if (thumbnailContainer.style.display === "none") {
    thumbnailContainer.style.display = "block";
  } else {
    thumbnailContainer.style.display = "none";
  }
});