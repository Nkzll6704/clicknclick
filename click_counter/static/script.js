document.getElementById('clickButton').addEventListener('click', () => {
    fetch('/increment', {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('clickCount').innerText = data.count;
    });
});

window.addEventListener('load', () => {
    fetch('/count')
    .then(response => response.json())
    .then(data => {
        document.getElementById('clickCount').innerText = data.count;
    });
});
