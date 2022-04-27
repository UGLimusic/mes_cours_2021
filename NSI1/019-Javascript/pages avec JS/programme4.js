// Ceci est du JavaScript (JS)
var a = 0;  // en JS, une variable globale peut être modifiée à n'importe quelle endroit du programme,
            // même dans une fonction !

function clique3(variable) {
    a += parseInt(variable); // parseInt convertit des chaines de caractères en entier, comme le int de Python
}

function affiche() {
    alert(a);
}

