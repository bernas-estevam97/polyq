document.getElementById("closePopup")?.addEventListener("click", () => {
            const url = new URL(window.location);
            url.searchParams.delete("sent");
            url.searchParams.delete("error");
            window.history.replaceState({}, document.title, url.pathname + url.search);
    });