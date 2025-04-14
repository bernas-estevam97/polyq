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
    let tmpOrientation;
    if (device === 'mobile'){
        if(window.innerHeight < window.innerWidth){
            device = 'tablet';
        }
    }


    let device_img = $.grep(img_coordinates, function (v) {
        return v.device === device;
    });
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
