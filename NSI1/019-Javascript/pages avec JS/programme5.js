// Ceci est du JavaScript
var a = 0;

function clique4(variable) {
    a += parseInt(variable);
    document.getElementById("labelResultat").textContent="Mon compteur vaut : "+a.toString();
    // on cherche dans le document l'élément dont l'id est labelResultat
    // on change son contenu texte dynamiquement
}

