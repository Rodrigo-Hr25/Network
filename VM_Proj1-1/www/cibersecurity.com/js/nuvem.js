let enabled = false

document.querySelector('.magico').addEventListener('click', function () {
    enabled = !enabled;
    if (enabled) {
        document.querySelector('.appear').setAttribute('style', 'display: block');
    } else {
        document.querySelector('.appear').setAttribute('style', 'display: none');
    }
});



