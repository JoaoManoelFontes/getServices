function confirmDelete(horarioId, ano, mes) {

    const url = `/horarios/deletar/${ano}/${mes}/${horarioId}/`;

    document.getElementById('delete-confirm').href = url;

    document.getElementById('confirm-delete-modal').checked = true;
}