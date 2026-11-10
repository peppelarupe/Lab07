import flet as ft
from UI.alert import AlertManager

'''
    VIEW:
    - Rappresenta l'interfaccia utente
    - Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):
        """ Crea e aggiunge gli elementi di UI alla pagina e la aggiorna. """
        # --- Sezione 1: Intestazione ---
        self.txt_titolo = ft.Text(value="Biblioteche di Torino", size=38, weight=ft.FontWeight.BOLD)

        # --- Sezione 2: Filtraggio ---
        # TODO

        # Dropdown per la selezione della biblioteca.
        # La prima opzione permette di non applicare il filtro.
        self.dropdown_biblioteca = ft.Dropdown(
            label="Seleziona una biblioteca",
            width=350,
            options=[
                ft.dropdown.Option(
                    key="__none__",
                    text="Nessun filtro"
                )
            ],
            value="__none__",
            on_select=self.controller.seleziona_biblioteca
        )

        # Dropdown per la selezione del genere.
        # Anche qui inseriamo inizialmente Nessun filtro.
        self.dropdown_genere = ft.Dropdown(
            label="Seleziona un genere",
            width=350,
            options=[
                ft.dropdown.Option(
                    key="__none__",
                    text="Nessun filtro"
                )
            ],
            value="__none__",
            on_select=self.controller.seleziona_genere
        )

        # Carichiamo le opzioni dei due dropdown
        # richiamando il Controller.
        self.controller.popola_dropdown()


        # Sezione 3: Libri
        # TODO

        # Pulsante per avviare la ricerca dei libri
        self.btn_mostra_libri = ft.Button(
            content="Mostra Libri",
            on_click=self.controller.mostra_libri
        )

        # ListView che conterrà i libri recuperati dal database
        self.lista_libri = ft.ListView(
            height=400,
            spacing=10,
            padding=10
        )


        # --- Toggle Tema ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        # --- Layout della pagina ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            ft.Divider(),

            # Sezione 2: Filtraggio
            # TODO

            ft.Text(
                "Filtra i libri",
                size=22,
                weight=ft.FontWeight.BOLD
            ),

            ft.Row(
                controls=[
                    self.dropdown_biblioteca,
                    self.dropdown_genere
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                wrap=True
            ),

            # Sezione 3: Libri
            # TODO
            self.btn_mostra_libri,

            ft.Divider(),

            ft.Text(
                "Lista dei libri",
                size=22,
                weight=ft.FontWeight.BOLD
            ),

            self.lista_libri
        )

        self.page.scroll = "adaptive"
        self.page.update()

    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()
