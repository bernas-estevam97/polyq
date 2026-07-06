var openBtn = document.getElementById("openBtn");
var closeBtn = document.getElementById("closeBtn");
var navLinks= document.getElementById("navLinks");
    function showMenu(){
      navLinks.style.right = "0";
    }
    function hideMenu(wind_size){
      navLinks.style.right = "-240px";
    }

openBtn.addEventListener("click", showMenu);
closeBtn.addEventListener("click", hideMenu);