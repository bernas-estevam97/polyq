$(document).ready(function () {
    const options = {
        allowHtml: true
    };

    // Store all coordinates in memory
    const all_img_coordinates = img_coordinates; // Already defined from Django

    let currentResolutionType = getResolutionType();

    // Initial render
    renderInteractiveImage();

    // Re-render on resolution group change
    $(window).on('resize', debounce(function () {
        const newResolutionType = getResolutionType();
        if (newResolutionType !== currentResolutionType) {
            currentResolutionType = newResolutionType;
            renderInteractiveImage();
        }
    }, 200)); // 200ms debounce to prevent excessive redraws

    // === Helper Functions ===

    function getResolutionType() {
        const width = window.innerWidth;
        if (width > 1246) return 'pc';
        if (width > 500) return 'tablet';
        return 'mobile';  // matches your existing field value
    }

    function renderInteractiveImage() {
    const resolution = getResolutionType();

    // ✅ Remove all previously rendered nodes/annotations
    $('.hotspot.icon-radio-checked, .item, .unsupported-screen').remove();

    // ✅ Filter your coordinates for the current resolution
    const items = all_img_coordinates
        .filter(item => item.resolution === resolution)
        .map(item => ({
            type: "text",
            title: item.title,
            description: item.text,
            position: {
                left: item.x,
                top: item.y
            }
        }));

    // ✅ Re-initialize the plugin with the new filtered items
    $("#my-interactive-image").interactiveImage(items, options);
    console.log(`Rendered for: ${resolution}`);
}


    function debounce(fn, delay) {
        let timeout;
        return function () {
            clearTimeout(timeout);
            timeout = setTimeout(fn, delay);
        };
    }
});
