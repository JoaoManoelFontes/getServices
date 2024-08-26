{
  const appointments = document.querySelectorAll(
    "[data-appointment-container]"
  );

  appointments.forEach((appointment) => {
    const approveButton = document.querySelector("[data-approve-appointment]");
    const cancelButton = document.querySelector("[data-cancel-appointment]");

    const approveInput = document.querySelector("[data-approve-input]");
    const cancelInput = document.querySelector("[data-cancel-input]");

    approveButton.addEventListener("click", () => {
      approveInput.click();
      approveButton.closest("form").submit();
    });

    cancelButton.addEventListener("click", () => {
      cancelInput.click();
      cancelButton.closest("form").submit();
    });
  });
}
