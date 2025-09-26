document.addEventListener('DOMContentLoaded', function () {
    const openButton = document.querySelector('.contact-form'); // Button that opens the dialog
    const dialog = document.querySelector('.dialog-form'); // The dialog element
    const form = document.getElementById('form'); // Your feedback form
    const closeButton = document.querySelector('.close-button'); // Dialog close button

    // Function that checks if reCAPTCHA is working
    function checkRecaptchaReady() {
        if (!window.grecaptcha) {
            console.error("reCAPTCHA library not loaded.");
            return;
        }

        grecaptcha.ready(function () {
            console.log("✅ reCAPTCHA is ready.");
        });
    }

    // When the open button is clicked
    openButton.addEventListener('click', function () {
        dialog.show();         // Show the dialog box
        checkRecaptchaReady(); // Check if reCAPTCHA is initialized
    });

    // When the close button is clicked
    closeButton.addEventListener('click', function () {
        dialog.close(); // Close the dialog
    });
});