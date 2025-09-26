$(document).scroll(function () {
        checkOffset();
    });

    function checkOffset() {
        if ($('#bar-right').offset().top + $('#bar-right').height() >= $('#references').offset().top + 200)
            $('#bar-right').hide(800);
        if ($(document).scrollTop() + window.innerHeight < $('#references').offset().top + 200)
            $('#bar-right').show(800); // restore when you scroll up
    }