{
  const background = document.querySelector("[data-modal-background]");
  const modal = document.querySelector("[data-modal]");
  const openModalButton = document.querySelector("[data-open-modal]");
  const closeButton = modal.querySelector("[data-modal-close]");

  openModalButton.addEventListener("click", handleOpenModal);

  closeButton.addEventListener("click", handleCloseModal);
  background.addEventListener("click", handleCloseModal);

  function handleOpenModal() {
    background.classList.remove("hidden");
    modal.classList.remove("hidden");
  }

  function handleCloseModal() {
    background.classList.add("hidden");
    modal.classList.add("hidden");
  }
}
