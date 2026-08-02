# ==================================================
#  LA GRANDE AVVENTURA DI ALE
#  File: gioco/main.py  (il motore del gioco)
#
#  ATTENZIONE: usiamo SOLO comandi semplici:
#  - print()      -> scrive cose sullo schermo
#  - input()      -> chiede una risposta al giocatore
#  - if/elif/else -> decisioni
#  - while        -> ripete finché una cosa è vera
#  - liste [..]   -> contenitori di cose
#  - dizionari {..} -> scatole con scomparti con nome
#  - def ...:     -> crea una funzione (una "ricetta")
#  NIENTE classi, niente librerie complicate.
#  Tutto è scritto in italiano. Buona lettura!
# ==================================================

# --- GLI ALTRI FILE DEL GIOCO ---
# mondo.py   contiene la mappa (i luoghi)
# oggetti.py contiene gli oggetti
import mondo
import oggetti

# --- LE VARIABILI DEL GIOCATORE ---
# (una variabile è una scatola con un nome)
posizione = "villaggio"   # dove si trova il giocatore
inventario = []           # gli oggetti che ha con sé (lista vuota)
gioco_aperto = True       # True = gioco in corso

# ==================================================
#  LE FUNZIONI (le "ricette" del gioco)
# ==================================================

# Messaggio di benvenuto
def benvenuto():
    print("=" * 50)
    print("   LA GRANDE AVVENTURA DI ALE")
    print("   Un gioco scritto in Python semplice")
    print("=" * 50)
    print("Scrivi  aiuto  per vedere i comandi.")

# Mostra il luogo dove sei
def guarda():
    luogo = mondo.luoghi[posizione]              # prendo i dati del luogo
    print("Sei a:", posizione.upper())
    print(luogo["descrizione"])
    print("Da qui puoi andare a:", ", ".join(luogo["usi"]))

# Prova ad andare in un altro luogo
def vai(dove):
    global posizione                             # serve per cambiare la variabile
    luogo = mondo.luoghi[posizione]
    if dove in luogo["usi"]:                     # controllo se posso andarci
        posizione = dove
        print("Sei andato a:", posizione.upper())
        guarda()
    else:
        print("Non puoi andare a", dove, "da qui.")

# Prova a prendere un oggetto
def prendi(cosa):
    if oggetti.posizioni.get(cosa) == posizione: # l'oggetto è qui?
        inventario.append(cosa)                  # lo aggiungo all'inventario
        oggetti.posizioni[cosa] = "preso"        # nel mondo ora non c'è più
        print("Hai preso:", cosa, "-", oggetti.descrizioni.get(cosa, ""))
    else:
        print("Non vedi", cosa, "qui.")

# Mostra l'inventario
def vedi_inventario():
    if inventario:
        print("Hai con te:", ", ".join(inventario))
    else:
        print("Non hai ancora niente.")

# ==================================================
#  IL CICLO PRINCIPALE DEL GIOCO
#  (while = ripeti finché il gioco è aperto)
# ==================================================
benvenuto()

while gioco_aperto:

    # chiedo un comando al giocatore
    comando = input("> ")
    comando = comando.lower()        # tutto minuscolo
    parole = comando.split()         # divido la frase in parole

    if not parole:                   # se non ha scritto niente
        continue                     # ricomincia il ciclo

    prima = parole[0]                # la prima parola è il comando

    # --- I COMANDI ---
    if prima == "aiuto":
        print("I comandi sono:  guarda  |  vai [luogo]  |  prendi [oggetto]  |  inventario  |  esci")

    elif prima == "guarda":
        guarda()

    elif prima == "vai":
        if len(parole) < 2:
            print("Scrivi anche il luogo. Esempio:  vai foresta")
        else:
            vai(parole[1])

    elif prima == "prendi":
        if len(parole) < 2:
            print("Scrivi anche l'oggetto. Esempio:  prendi mela")
        else:
            prendi(parole[1])

    elif prima == "inventario":
        vedi_inventario()

    elif prima == "esci":
        print("Grazie per aver giocato! A presto!")
        gioco_aperto = False

    else:
        print("Non capisco:", prima, "- scrivi  aiuto  per i comandi.")

# fine del gioco
print("Fine dell'avventura.")
