var items = [
    {
        type: "text",
        title: "123",
        description: "Huntingtin has been shown to be found within the nucleus and develops some of its previously mentioned transcriptional functions",
        position: {
            left: "{{disease.coordinates.x}}",
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
        description: "Across tissue samples, Huntingtin is mainly found within the cytoplasm.<br><br>In immunoreactivity studies, Htt was found in neurons throughout the brain and localized mostly to the somatodendritic cytoplasm",
        position: {
            left: 110,
            top: 150
        },
    },
];


$(document).ready(function () {
    const getDeviceType = () => {
        const ua = navigator.userAgent;
        if (/(tablet|ipad|playbook|silk)|(android(?!.*mobi))/i.test(ua)) {
            return "tablet";
        }
        if (
            /Mobile|iP(hone|od)|Android|BlackBerry|IEMobile|Kindle|Silk-Accelerated|(hpw|web)OS|Opera M(obi|ini)/.test(
                ua
            )
        ) {
            return "mobile";
        }
        return "pc";
    };

    let options = {
        allowHtml: true
    };
    let items = [];
    let device = getDeviceType();

    console.log("device", device)

    let device_img = $.grep(img_coordinates, function (v) {
        return v.device === device;
    });
    console.log("teste", device_img)
    device_img.forEach(function (item, index) {
        let img_item = {
            type: "text",
            title: item.title,
            description: item.text,
            position: {
                left: item.x,
                top: item.y
            },
        }
        items.push(img_item)
    });
    $("#my-interactive-image").interactiveImage(items, options);
});
