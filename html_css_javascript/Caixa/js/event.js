var handednessBtn = document.getElementById('handednessBtn');
var video = document.getElementById('video1');

var img1 = document.getElementById("img-1");
var img1Mirrored = document.getElementById("img-1-mirrored");

handednessBtn.addEventListener("click", function(){ mirror(video, img1, img1Mirrored, handednessBtn); });

function mirror(vid, img, imgMirrored, btn) {
    if (vid.className == "") {
        vid.className = "mirror";
        img.classList.add("hidden");
        imgMirrored.classList.remove("hidden");
        btn.innerHTML = "I'm right-handed!"
    }
    else {
        vid.className = "";
        imgMirrored.classList.add("hidden");
        img.classList.remove("hidden");
        btn.innerHTML = "I'm left-handed!"
    }
}


