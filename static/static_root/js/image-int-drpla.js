var items = [
  {
    type: "text",
    title: "Nucleus",
    description: "Atrophin-1 is found within the nucleus since it is involved in transcriptional activity.",
    position: {
      left: 270,
      top: 120
    },
    // sticky: true
  },
  {
    type: "text",
    title: "Cytoplasm",
    description: "As it involved in apoptotic processes, it can be found in the cell cytoplasm",
    position: {
      left: 90,
      top: 190
    },
  },
  {
    type: "text",
    title: "Perinuclear regions",
    description: "Interaction with FAT1 occurs in this region",
    position: {
      left: 230,
      top: 90
    },
  },
  {
    type: "text",
    title: "Cell Junctions",
    description: "Colocalization with FAT1 in these junctions",
    position: {
      left: 100,
      top: 110
    },
  },
];


var itemsPhone = [
  {
    type: "text",
    title: "Nucleus",
    description: "Atrophin-1 is found within the nucleus since it is involved in transcriptional activity.",
    position: {
      left: 160,
      top: 60
    },
    // sticky: true
  },
  {
    type: "text",
    title: "Cytoplasm",
    description: "As it involved in apoptotic processes, it can be found in the cell cytoplasm",
    position: {
      left: 100,
      top: 140
    },
  },
  {
    type: "text",
    title: "Perinuclear regions",
    description: "Interaction with FAT1 occurs in this region",
    position: {
      left: 110,
      top: 70
    },
  },
  {
    type: "text",
    title: "Cell Junctions",
    description: "Colocalization with FAT1 in these junctions",
    position: {
      left: 25,
      top: 115
    },
  },
];


var itemsAlmostTablet = [
  {
    type: "text",
    title: "Nucleus",
    description: "Atrophin-1 is found within the nucleus since it is involved in transcriptional activity.",
    position: {
      left: 270,
      top: 100
    },
    // sticky: true
  },
  {
    type: "text",
    title: "Cytoplasm",
    description: "As it involved in apoptotic processes, it can be found in the cell cytoplasm",
    position: {
      left: 170,
      top: 170
    },
  },
  {
    type: "text",
    title: "Perinuclear regions",
    description: "Interaction with FAT1 occurs in this region",
    position: {
      left: 210,
      top: 90
    },
  },
  {
    type: "text",
    title: "Cell Junctions",
    description: "Colocalization with FAT1 in these junctions",
    position: {
      left: 90,
      top: 130
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
