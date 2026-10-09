// "On this page" navigation for disease pages.
// The current section is the last one whose top has passed a reading line 30% down the
// viewport. A short section (e.g. Introduction) therefore stays active until the next
// heading actually reaches the line, instead of losing to whichever section fills more
// of the screen. Builds the same markup the old ScrollSpy library did, so the CSS is unchanged.
(function () {
    const sections = Array.from(document.querySelectorAll('section.scrollspy'));
    const container = document.getElementById('indicator');
    if (!sections.length || !container) return;

    const READING_LINE = 0.3;
    const list = document.createElement('ul');
    list.className = 'scrollspy-indicator-container';

    const items = sections.map(function (section) {
        const item = document.createElement('li');
        item.className = 'spy-clickable';
        item.textContent = section.getAttribute('spy-title');
        item.tabIndex = 0;
        item.setAttribute('role', 'link');
        // scroll-padding-top in modern.css keeps the heading clear of the sticky header
        const go = function () { section.scrollIntoView({ behavior: 'smooth', block: 'start' }); };
        item.addEventListener('click', go);
        item.addEventListener('keydown', function (e) {
            if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); go(); }
        });
        list.appendChild(item);
        return item;
    });
    container.replaceChildren(list);

    // Cheap enough (one measurement per section) to run on every scroll event.
    function update() {
        const line = window.innerHeight * READING_LINE;
        let current = 0;
        sections.forEach(function (section, i) {
            if (section.getBoundingClientRect().top <= line) current = i;
        });
        // Short sections at the end can never reach the line: at the bottom, the last one wins.
        const atBottom = window.innerHeight + window.scrollY >= document.documentElement.scrollHeight - 2;
        if (atBottom) current = sections.length - 1;
        items.forEach(function (item, i) {
            item.classList.toggle('spy-active', i === current);
            if (i === current) item.setAttribute('aria-current', 'location');
            else item.removeAttribute('aria-current');
        });
    }

    window.addEventListener('scroll', update, { passive: true });
    window.addEventListener('resize', update);
    window.addEventListener('load', update);  // images loading shift section positions
    update();
})();
