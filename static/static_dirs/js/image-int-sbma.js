var items = [
  {
    type: "text",
    title: "Nucleus",
    description: "Androgen-receptor is found in the nucleus bound to ligands or in the form of RACK1 post-interaction",
    position: {
      left: 270,
      top: 120
    },
    // sticky: true
  },
  {
    type: "text",
    title: "Cytoplasm",
    description: "Mainly found in the cytoplasm, in the membrane, as a receptor",
    position: {
      left: 90,
      top: 190
    },
  },
];

var options = {
  allowHtml: true
};

var itemsPhone = [
  {
    type: "text",
    title: "Nucleus",
    description: "Androgen-receptor is found in the nucleus bound to ligands or in the form of RACK1 post-interaction",
    position: {
      left: 160,
      top: 70
    },
    // sticky: true
  },
  {
    type: "text",
    title: "Cytoplasm",
    description: "Mainly found in the cytoplasm, in the membrane, as a receptor",
    position: {
      left: 50,
      top: 110
    },
  },
];

var itemsAlmostTablet = [
  {
    type: "text",
    title: "Nucleus",
    description: "Androgen-receptor is found in the nucleus bound to ligands or in the form of RACK1 post-interaction",
    position: {
      left: 260,
      top: 90
    },
    // sticky: true
  },
  {
    type: "text",
    title: "Cytoplasm",
    description:  "Mainly found in the cytoplasm, in the membrane, as a receptor",
    position: {
      left: 110,
      top: 150
    },
  },
];


var options = {
  allowHtml: true
};


  $(document).ready(function() {
    if ($(window).width()>=751) {
      $("#my-interactive-image").interactiveImage(items, options);
    } else if ($(window).width()<=483){
      $("#my-interactive-image").interactiveImage(itemsPhone, options);
    } else if ($(window).width()>483 && $(window).width()<751){
      $("#my-interactive-image").interactiveImage(itemsAlmostTablet, options);
    }
  });
