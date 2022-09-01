var items = [
  {
    type: "text",
    title: "Nucleus",
    description: "Ataxin-7 is involved with several transcription coactivators and so taking a part in transcription",
    position: {
      left: 270,
      top: 120
    },
    // sticky: true
  },
  {
    type: "text",
    title: "Cytoplasm",
    description: "Found in the cytoskeleton. It is an essencial part of microtubule stabilization",
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
    description: "Ataxin-7 is involved with several transcription coactivators and so taking a part in transcription",
    position: {
      left: 160,
      top: 70
    },
    // sticky: true
  },
  {
    type: "text",
    title: "Cytoplasm",
    description: "Found in the cytoskeleton. It is an essencial part of microtubule stabilization",
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
    description: "Ataxin-7 is involved with several transcription coactivators and so taking a part in transcription",
    position: {
      left: 260,
      top: 90
    },
    // sticky: true
  },
  {
    type: "text",
    title: "Cytoplasm",
    description:  "Found in the cytoskeleton. It is an essencial part of microtubule stabilization",
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
