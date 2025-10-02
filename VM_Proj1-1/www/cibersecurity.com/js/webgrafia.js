let web1 = false

document.querySelector('.webgrafia').addEventListener('click', function () {
    web1 = !web1;
    if (web1) {
        document.querySelector('.web').setAttribute('style', 'display: block');
    } else {
        document.querySelector('.web').setAttribute('style', 'display: none');
    }
});
