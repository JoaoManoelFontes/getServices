{
    const EXPANDABLE_BUTTON_VALUES = {
        "Ver Mais ↓": "Ver Menos ↑",
        "Ver Menos ↑": "Ver Mais ↓",
    };

    const expandableContainers = document.querySelectorAll(
        "[data-expandable-container]"
    );

    expandableContainers.forEach((expandableContainer) => {
        const expandableList = expandableContainer.querySelector(
            "[data-expandable-list]"
        );
        const expandableButton = expandableContainer.querySelector(
            "[data-expandable-button]"
        );

        if (expandableButton && expandableList) {
            expandableButton.addEventListener("click", () => {
                toggleExpandableContainer(expandableList, expandableButton);
            });
        }
    });

    function toggleExpandableContainer(expandableList, expandableButton) {
        const isExpanded = expandableList.classList.contains("max-h-40");

        if (isExpanded) {
            expandableList.classList.remove("max-h-40");
            expandableList.classList.add("max-h-[1000px]");
            expandableButton.textContent = "Ver Menos ↑";
        } else {
            expandableList.classList.add("max-h-40");
            expandableList.classList.remove("max-h-[1000px]");
            expandableButton.textContent = "Ver Mais ↓";
        }

        expandableList.classList.toggle("overflow-hidden");
        expandableList.classList.toggle("overflow-auto");
    }
}