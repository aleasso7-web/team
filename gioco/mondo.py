# ==================================================
#  LA MAPPA DEL MONDO
#  File: gioco/mondo.py
#
#  Qui dentro c'è la lista dei luoghi del gioco.
#  Un "dizionario" è una scatola con tanti scomparti
#  contrassegnati da nomi.  { nome: contenuto }
# ==================================================

luoghi = {

    # il primo luogo: il villaggio (qui inizia il gioco)
    "villaggio": {
        "descrizione": "Un villaggio tranquillo. Le case hanno i tetti rossi e c'è un pozzo in piazza.",
        "usi": ["foresta", "lago", "montagna"],   # da qui puoi andare a...
    },

    # la foresta
    "foresta": {
        "descrizione": "Una foresta fitta e scura. Gli alberi sono altissimi e si sentono uccelli.",
        "usi": ["villaggio", "montagna"],
    },

    # il lago
    "lago": {
        "descrizione": "Un lago blu e calmo. L'acqua brilla come uno specchio.",
        "usi": ["villaggio"],
    },

    # la montagna
    "montagna": {
        "descrizione": "Una montagna alta con la cima coperta di neve. Si vede un castello in lontananza... ma non c'è ancora una strada per arrivarci!",
        "usi": ["villaggio", "foresta"],
    },
}
