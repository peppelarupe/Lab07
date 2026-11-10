from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    # TODO

    def get_all_biblioteche(self):
        """
        Recupera tutte le biblioteche dal database
        e restituisce una lista di oggetti Biblioteca.
        """

        # Lista che conterrà gli oggetti Biblioteca
        biblioteche = []

        # Otteniamo una connessione dal pool
        connessione = DBConnect.get_connection()

        # Se non è stato possibile connettersi, restituiamo una lista vuota
        if connessione is None:
            return biblioteche

        cursor = None

        try:
            # Creiamo il cursor per eseguire le query SQL
            cursor = connessione.cursor()

            query = """
                SELECT id, nome, indirizzo
                FROM biblioteca
            """

            cursor.execute(query)
            risultati = cursor.fetchall()

            # Per ogni record creiamo un oggetto Biblioteca
            for row in risultati:
                biblioteca = Biblioteca(
                    row[0],
                    row[1],
                    row[2]
                )

                # Aggiungiamo l'oggetto alla lista
                biblioteche.append(biblioteca)

        finally:
            # Chiudiamo il cursor dopo aver terminato le operazioni
            if cursor is not None:
                cursor.close()

            connessione.close()
        return biblioteche
