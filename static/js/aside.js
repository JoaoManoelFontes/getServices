{
  const openButton = document.querySelector("[data-menu-button-open]");
  const background = document.querySelector("[data-menu-background]");
  const closeButton = document.querySelector("[data-menu-close]");
  const menu = document.querySelector("[data-menu]");

  openButton?.addEventListener("click", handleOpenMenu);

  background?.addEventListener("click", handleCloseMenu);
  closeButton?.addEventListener("click", handleCloseMenu);

  function handleOpenMenu() {
    background?.classList.remove("hidden");
    menu?.classList.add("translate-x-[320px]");
  }

  function handleCloseMenu() {
    background?.classList.add("hidden");
    menu?.classList.remove("translate-x-[320px]");
  }
}
