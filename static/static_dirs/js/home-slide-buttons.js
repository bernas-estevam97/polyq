let btnLeft = document.getElementById('left-btn');
let btnRight = document.getElementById('right-btn');
let btnAllLeft = document.getElementById('left-all-btn');
let btnAllRight = document.getElementById('right-all-btn');


btnRight.onclick = function () {
    document.getElementById('slider-horizontal').scrollLeft += 400;
};

btnLeft.onclick = function () {
    document.getElementById('slider-horizontal').scrollLeft -= 400;
};

btnAllRight.onclick = function () {
    document.getElementById('slider-horizontal').scrollLeft += 2400;
};

btnAllLeft.onclick = function () {
    document.getElementById('slider-horizontal').scrollLeft -= 2400;
};