var chiffreAffiche = 0;
var chiffreMemoire = 0;
var chiffreCourant = 0;

function cliqueChiffre(elt_id) {
    chiffreCourant = chiffreCourant * 10 + parseInt(elt_id);
    chiffreAffiche = chiffreCourant;
    document.getElementById('affichage').textContent = chiffreAffiche.toString();
}

function cliqueOperation(elt_id) {
    chiffreMemoire += chiffreCourant;
    chiffreCourant = 0;
    chiffreAffiche = chiffreMemoire;
    document.getElementById('affichage').textContent = chiffreAffiche.toString();
}
