var items = [
  {
    type: "text",
    title: "Nucleus",
    description: "The C-terminus of the α1A subunit (α1ACT) can translocate to the nucleus and act as a gene regulator",
    position: {
      left: 270,
      top: 120
    },
    // sticky: true
  },
  {
    type: "text",
    title: "Cell membrane",
    description: "As a multi-pass membrane protein, voltage-dependent P/Q-type calcium channel subunit alpha-1A is located in the cell membranes",
    position: {
      left: 70,
      top: 170
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
    description: "The C-terminus of the α1A subunit (α1ACT) can translocate to the nucleus and act as a gene regulator",
    position: {
      left: 160,
      top: 70
    },
    // sticky: true
  },
  {
    type: "text",
    title: "Cell membrane",
    description: "As a multi-pass membrane protein, voltage-dependent P/Q-type calcium channel subunit alpha-1A is located in the cell membranes",
    position: {
      left: 30,
      top: 110
    },
  },
];

var itemsAlmostTablet = [
  {
    type: "text",
    title: "Nucleus",
    description: "The C-terminus of the α1A subunit (α1ACT) can translocate to the nucleus and act as a gene regulator",
    position: {
      left: 260,
      top: 90
    },
    // sticky: true
  },
  {
    type: "text",
    title: "Cell membrane",
    description:  "As a multi-pass membrane protein, voltage-dependent P/Q-type calcium channel subunit alpha-1A is located in the cell membranes",
    position: {
      left: 90,
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
