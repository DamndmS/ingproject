const grid = document.querySelector('.grid');


grid.addEventListener('click', (e) => {
    const cell = e.target.closest('.cell');
    if (!cell) return;

    cell.classList.toggle('clicked');
});

document.getElementById('regen').addEventListener('click', () => {
    const n = document.getElementById('size').value;
    window.location.href = '/?n=' + n;
});

document.getElementById('reset').addEventListener('click', () => {
    document.querySelectorAll('cell').forEach(cell => {
        cell.classList.remove('clicked');
    });
});


