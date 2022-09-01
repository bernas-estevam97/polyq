var items = [
  {
    type: "text",
    title: "Nucleus",
    description: "TBP is exclusively found in the nucleus where it takes part in the process of transcrption initiation with RNA polymerases I to III",
    position: {
      left: 270,
      top: 120
    },
    // sticky: true
  }
];


var itemsPhone = [
  {
    type: "text",
    title: "Nucleus",
    description: "TBP is exclusively found in the nucleus where it takes part in the process of transcrption initiation with RNA polymerases I to III",
    position: {
      left: 160,
      top: 70
    },
    // sticky: true
  }
];

var itemsAlmostTablet = [
  {
    type: "text",
    title: "Nucleus",
    description: "TBP is exclusively found in the nucleus where it takes part in the process of transcrption initiation with RNA polymerases I to III",
    position: {
      left: 260,
      top: 90
    },
    // sticky: true
  }
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
