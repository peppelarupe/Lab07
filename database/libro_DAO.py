from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    # TODO

    def get_generi(self):

        #Recupera tutti i generi presenti nel database. DISTINCT evita di avere generi ripetuti.

        generi = []

        connessione = DBConnect.get_connection()

        if connessione is None:
            return generi

        cursor = None

        try:
            cursor = connessione.cursor()

            query = """
                SELECT DISTINCT genere
                FROM libro
                WHERE genere IS NOT NULL
                ORDER BY genere
            """

            cursor.execute(query)

            risultati = cursor.fetchall()

            # Ogni risultato contiene un solo valore: il genere
            for row in risultati:
                generi.append(row[0])

        finally:
            if cursor is not None:
                cursor.close()

            connessione.close()

        return generi

    def get_libri_filtrati(self, biblioteca: str | None, genere: str | None):
        """
        Recupera i libri applicando i filtri opzionali
        relativi alla biblioteca e al genere.

        Se un parametro è None, il relativo filtro non viene applicato.
        """

        libri = []

        connessione = DBConnect.get_connection()

        if connessione is None:
            return libri

        cursor = None

        try:
            cursor = connessione.cursor()

            # COALESCE permette di gestire i filtri opzionali: se il parametro è None, viene utilizzato il valore della colonna.
            query = """
                    SELECT libro.id, libro.titolo, libro.autore, libro.genere,
                           libro.anno_pubblicazione, libro.id_biblioteca
                    FROM libro, biblioteca
                    WHERE libro.id_biblioteca = biblioteca.id
                    AND biblioteca.nome = COALESCE(%s, biblioteca.nome)
                    AND libro.genere = COALESCE(%s, libro.genere)
                """

            # Passiamo i valori separatamente dalla query SQL
            cursor.execute(query, (biblioteca, genere))

            # Recuperiamo tutti i libri che soddisfano i filtri
            risultati = cursor.fetchall()

            # Trasformiamo ogni record in un oggetto Libro
            for row in risultati:

                libro = Libro(
                    row[0],  # id
                    row[1],  # titolo
                    row[2],  # autore
                    row[3],  # genere
                    row[4],  # anno_pubblicazione
                    row[5]   # id_biblioteca
                )

                libri.append(libro)

        finally:
            if cursor is not None:
                cursor.close()

            connessione.close()

        return libri