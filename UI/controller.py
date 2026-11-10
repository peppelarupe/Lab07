import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    # TODO
    def popola_dropdown(self):

        # Recuperiamo tutte le biblioteche
        biblioteche = self._model.get_biblioteche()

        # Inseriamo ogni biblioteca nel dropdown.
        # La key contiene l'ID, il text contiene il nome visualizzato.
        for biblioteca in biblioteche:
            self._view.dropdown_biblioteca.options.append(
                ft.dropdown.Option(
                    key=biblioteca.nome,
                    text=biblioteca.nome
                )
            )

        # Recuperiamo tutti i generi disponibili
        generi = self._model.get_generi()

        # Inseriamo ogni genere nel relativo dropdown
        for genere in generi:
            self._view.dropdown_genere.options.append(
                ft.dropdown.Option(genere)
            )

    # CALLBACKS DROPDOWN
    # TODO

    def seleziona_biblioteca(self, e):
        """
        Callback eseguita quando l'utente seleziona
        una biblioteca dal dropdown.
        """

        valore = e.control.value

        # Se viene scelto Nessun filtro, non applichiamo il filtro
        if valore == "__none__":
            self.biblioteca_selezionata = None

        else:
            self.biblioteca_selezionata = valore

    def seleziona_genere(self, e):

        valore = e.control.value

        # Nessun filtro corrisponde a None
        if valore == "__none__":
            self.genere_selezionato = None

        else:
            self.genere_selezionato = valore

    # AZIONE: MOSTRA LIBRI
    # TODO

    def mostra_libri(self, e):
        """
        Recupera e visualizza i libri in base
        ai filtri selezionati dall'utente.
        """

        # Richiediamo al Model i libri filtrati
        libri = self._model.get_libri_filtrati(
            self.biblioteca_selezionata,
            self.genere_selezionato
        )

        # Eliminiamo gli eventuali risultati precedenti
        self._view.lista_libri.controls.clear()

        if len(libri) == 0:

            self._view.update()

            self._view.show_alert(
                "Nessun libro trovato con i filtri selezionati."
            )

        else:

            # Per ogni libro creiamo un controllo Text
            # contenente le informazioni dell'oggetto DTO
            for libro in libri:

                self._view.lista_libri.controls.append(
                    ft.Text(str(libro))
                )

            # Aggiorniamo l'interfaccia grafica
            self._view.update()


