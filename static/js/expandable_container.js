{
  const EXPANDALBE_BUTTON_VALUES = {
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

    expandableButton.addEventListener("click", () => {
      toogleExpandableContainer(expandableList, expandableButton);
    });
  });

  function toogleExpandableContainer(expandableList, expandableButton) {
    expandableButton.innerText =
      EXPANDALBE_BUTTON_VALUES[expandableButton.innerText];
    expandableList.classList.toggle("max-h-60");
    expandableList.classList.toggle("max-h-80");
    expandableList.classList.toggle("overflow-hidden");
    expandableList.classList.toggle("overflow-auto");
  }
}
