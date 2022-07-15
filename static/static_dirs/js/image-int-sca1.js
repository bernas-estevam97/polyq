var items = [
  {
    type: "text",
    title: "Nucleus",
    description: "Ataxin-1 is directly involved in the transcription machinery and RNA processing, it is so abundantly seen in the nucleus.<br><br> Ataxin-1 is recruited to the nucleus through its nuclear localization signal.",
    position: {
      left: 270,
      top: 120
    },
    // sticky: true
  },
  {
    type: "text",
    title: "Cytoplasm",
    description: "Ataxin-1 may be found in the cytoplasm and involved in some protein-protein interactions within Purkinje cells",
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
    description: "Ataxin-1 is directly involved in the transcription machinery and RNA processing, it is so abundantly seen in the nucleus.<br><br> Ataxin-1 is recruited to the nucleus through its nuclear localization signal.",
    position: {
      left: 160,
      top: 70
    },
    // sticky: true
  },
  {
    type: "text",
    title: "Cytoplasm",
    description: "Ataxin-1 may be found in the cytoplasm and involved in some protein-protein interactions within Purkinje cells",
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
    description: "Ataxin-1 is directly involved in the transcription machinery and RNA processing, it is so abundantly seen in the nucleus.<br><br> Ataxin-1 is recruited to the nucleus through its nuclear localization signal.",
    position: {
      left: 260,
      top: 90
    },
    // sticky: true
  },
  {
    type: "text",
    title: "Cytoplasm",
    description:  "Ataxin-1 may be found in the cytoplasm and involved in some protein-protein interactions within Purkinje cells",
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
