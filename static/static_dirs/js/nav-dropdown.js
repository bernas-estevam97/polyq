    /* When the user clicks on the button,
    toggle between hiding and showing the dropdown content */
    function myFunction() {
        document.getElementById("myDropdown").classList.toggle("show");
    }

    function myFunctionLittle() {
        document.getElementById("myDropdownLittle").classList.toggle("show");
    }

    // Close the dropdown if the user clicks outside of it
    window.onclick = function (event) {
        if (!event.target.matches('.dropbtn')) {
            var dropdowns = document.getElementsByClassName("dropdown-content");
            var i;
            for (i = 0; i < dropdowns.length; i++) {
                var openDropdown = dropdowns[i];
                if (openDropdown.classList.contains('show')) {
                    openDropdown.classList.remove('show');
                }
            }
        }
        if (!event.target.matches('.dropbtn-little')) {
            var dropLittle = document.getElementsByClassName("dropdown-content-little");
            var r;
            for (r = 0; r < dropLittle.length; r++) {
                var openDropLittle = dropLittle[r];
                if (openDropLittle.classList.contains('show')) {
                    openDropLittle.classList.remove('show');
                }
            }
        }
    }