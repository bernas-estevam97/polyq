function successCallBack(){
    console.log("Recaptcha ready!")
}



window.onload = function() {
    var recaptcha = document.forms["form"]["g-recaptcha-response"];
    recaptcha.required = true;
    recaptcha.oninvalid = function(e) {
// do something
        alert("Please complete the captcha");
}
}