const objectives = document.querySelectorAll(".qaa");

objectives.forEach((qaa) => {
  qaa.addEventListener("click", () => {
    qaa.classList.toggle("active");
  })
} )
