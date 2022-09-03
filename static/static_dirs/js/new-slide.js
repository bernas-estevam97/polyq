const slider = document.querySelector('.img-slider');
const nextBtn = document.querySelector('.next-button');
const prevBtn = document.querySelector('.prev-button');
const slides = document.querySelectorAll('.slide');
const slideBtns = document.querySelectorAll('.btn');
const numberOfSlides = slides.length;
var slideNumber = 0;
let btnNumber = 0;
let currentSlide = 1;

nextBtn.addEventListener('click', () =>{
  slides.forEach((slide) =>{
    slide.classList.remove('active');
  });
  slideBtns.forEach((btn) =>{
    btn.classList.remove('active');
  });
  slideNumber++;

  if (slideNumber > (numberOfSlides - 1)){
    slideNumber = 0;
  }

  slides[slideNumber].classList.add('active');
  slideBtns[slideNumber].classList.add('active');
});

prevBtn.addEventListener("click", () =>{
  slides.forEach((slide) =>{
    slide.classList.remove('active');
  });
  slideBtns.forEach((btn) =>{
    btn.classList.remove('active');
  });
  slideNumber--;

  if (slideNumber < 0){
    slideNumber = numberOfSlides - 1;
  }

  slides[slideNumber].classList.add('active');
  slideBtns[slideNumber].classList.add('active');
});

// SLIDER AUTOPLAY
var playSlider;

var repeater = () => {
  playSlider = setInterval(function(){
    slides.forEach((slide) =>{
      slide.classList.remove('active');
    });
    slideBtns.forEach((btn) =>{
      btn.classList.remove('active');
    });
    slideNumber++;

    if (slideNumber > (numberOfSlides - 1)){
      slideNumber = 0;
    }

    slides[slideNumber].classList.add('active');
    slideBtns[slideNumber].classList.add('active');
  }, 10000);
}
repeater();

// Stop autoplay on mouseover

slider.addEventListener("mouseover", () => {
  clearInterval(playSlider);
});

slider.addEventListener("mouseout", () => {
  repeater();
});


// clickable slide icons

const navBtn = document.querySelector('.navigation');
const btns = Array.from(navBtn.children);


navBtn.addEventListener("click", e => {
  const targetBtn = e.target.closest('button');

  if (!targetBtn) return;


  const targetIndex = btns.findIndex(btn => btn === targetBtn);
  const targetSlide = slides[targetIndex];

  // updateDots(currentBtn, targetBtn);

  slides.forEach((slide) =>{
    slide.classList.remove('active');
  });
  slideBtns.forEach((btn) =>{
    btn.classList.remove('active');
  });
  slideNumber = targetIndex;

  targetSlide.classList.add('active');
  targetBtn.classList.add('active');
})
