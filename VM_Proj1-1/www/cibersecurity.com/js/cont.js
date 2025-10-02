let cont1 = false

document.querySelector('.escondido1').addEventListener('click', function () {
    cont1 = !cont1;
    if (cont1) {
        document.querySelector('.appear1').setAttribute('style', 'display: block');
    } else {
        document.querySelector('.appear1').setAttribute('style', 'display: none');
    }
});

let cont2 = false

document.querySelector('.escondido2').addEventListener('click', function () {
    cont2 = !cont2;
    if (cont2) {
        document.querySelector('.appear3').setAttribute('style', 'display: block');
    } else {
        document.querySelector('.appear3').setAttribute('style', 'display: none');
    }
}); 