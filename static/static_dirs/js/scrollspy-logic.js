let indicator = document.getElementById('indicator');

    var spy = new ScrollSpy(
        {
            contexts_class: 'scrollspy'
        }
    );

    spy.Indicator({
        element: indicator
    });