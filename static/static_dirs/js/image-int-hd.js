var items = [
  {
    type: "text",
    title: "Nucleus",
    description: "Huntingtin has been shown to be found within the nucleus and develops some of its previously mentioned transcriptional functions",
    position: {
      left: 270,
      top: 120
    },
    // sticky: true
  },
  {
    type: "text",
    title: "Cytoplasm",
    description: "Across tissue samples, Huntingtin is mainly found within the cytoplasm.<br><br>In immunoreactivity studies, Htt was found in neurons throughout the brain and localized mostly to the somatodendritic cytoplasm",
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
    description: "Huntingtin has been shown to be found within the nucleus and develops some of its previously mentioned transcriptional functions",
    position: {
      left: 160,
      top: 70
    },
    // sticky: true
  },
  {
    type: "text",
    title: "Cytoplasm",
    description: "Across tissue samples, Huntingtin is mainly found within the cytoplasm.<br><br>In immunoreactivity studies, Htt was found in neurons throughout the brain and localized mostly to the somatodendritic cytoplasm",
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
    description: "Huntingtin has been shown to be found within the nucleus and develops some of its previously mentioned transcriptional functions",
    position: {
      left: 260,
      top: 90
    },
    // sticky: true
  },
  {
    type: "text",
    title: "Cytoplasm",
    description:  "Across tissue samples, Huntingtin is mainly found within the cytoplasm.<br><br>In immunoreactivity studies, Htt was found in neurons throughout the brain and localized mostly to the somatodendritic cytoplasm",
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
