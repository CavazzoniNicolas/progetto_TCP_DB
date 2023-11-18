import socket
import mysql.connector

def db_get_dipendenti(parametri):
    conn = mysql.connector.connect(
        host="127.0.0.1", 
        user = "root",
        password = "",
        database="5btepsit",
        port=3306,    
    )

    cur = conn.cursor()

    clausole = ""
    for key, value in parametri.items():
        clausole += f"and {key} = '{value}' "

    query = f"SELECT * FROM dipendenti_nicolas_cavazzoni where 1=1 {clausole}"
    cur.execute(query)
    dati = cur.fetchall()
    return dati

def db_get_zone(parametri):
    conn = mysql.connector.connect(
        host="127.0.0.1", 
        user = "root",
        password = "",
        database="5btepsit",
        port=3306,    
    )

    cur = conn.cursor()

    clausole = ""
    for key, value in parametri.items():
        clausole += f"and {key} = '{value}' "

    query = f"SELECT * FROM zona_di_lavoro_nicolas_cavazzoni where 1=1 {clausole}"
    cur.execute(query)
    dati = cur.fetchall()
    return dati

def db_elimina_dipendente(parametri):
    conn = mysql.connector.connect(
        host="127.0.0.1", 
        user = "root",
        password = "",
        database="5btepsit",
        port=3306,    
    )
    
    cur = conn.cursor()
    
    clausole = ""
    for key, value in parametri.items():
        clausole += f"and {key} = '{value}' "
    
    query = f"DELETE FROM dipendenti_nicolas_cavazzoni where 1=1 {clausole}"
    cur.execute(query)
    conn.commit()

def db_elimina_zona(parametri):
    conn = mysql.connector.connect(
        host="127.0.0.1", 
        user = "root",
        password = "",
        database="5btepsit",
        port=3306,    
    )
    
    cur = conn.cursor()
    
    clausole = ""
    for key, value in parametri.items():
        clausole += f"and {key} = '{value}' "
    
    query = f"DELETE FROM zona_di_lavoro_nicolas_cavazzoni where 1=1 {clausole}"
    cur.execute(query)
    conn.commit()

def db_inserisci_dipendente(parametri):
    conn = mysql.connector.connect(
        host="127.0.0.1", 
        user = "root",
        password = "",
        database="5btepsit",
        port=3306,    
    )
    
    cur = conn.cursor()
    
    query = f"INSERT INTO dipendenti_nicolas_cavazzoni (nome, cognome, posizione_lavoro, data_assunzione, stipendio, telefono) VALUES ('{nome}','{cognome}','{posizione_lavoro}','{data_assunzione}','{stipendio}','{telefono}')"
    cur.execute(query)
    conn.commit()

def db_inserisci_zona(parametri):
    conn = mysql.connector.connect(
        host="127.0.0.1", 
        user = "root",
        password = "",
        database="5btepsit",
        port=3306,    
    )
    
    cur = conn.cursor()
    
    query = f"INSERT INTO zona_di_lavoro_nicolas_cavazzoni (nome, numero_clienti, metri_quadri) VALUES ('{nome}','{numero_clienti}','{metri_quadri}')"
    cur.execute(query)
    conn.commit()

def db_modifica_dipendente(par):
    
    conn = mysql.connector.connect(
        host="127.0.0.1", 
        user = "root",
        password = "",
        database="5btepsit",
        port=3306,    
    )
    cur = conn.cursor()
    query = f"UPDATE dipendenti_nicolas_cavazzoni SET nome = '{nome}', cognome = '{cognome}', posizione_lavoro = '{posizione_lavoro}', data_assunzione = '{data_assunzione}', stipendio = '{stipendio}', telefono = '{telefono}' WHERE id = '{id_modifica}'"
    cur.execute(query)
    conn.commit()

def db_modifica_zona(par):
    
    conn = mysql.connector.connect(
        host="127.0.0.1", 
        user = "root",
        password = "",
        database="5btepsit",
        port=3306,    
    )
    cur = conn.cursor()
    query = f"UPDATE zona_di_lavoro_nicolas_cavazzoni SET nome = '{nome}', numero_clienti = '{numero_clienti}', metri_quadri = '{metri_quadri}' WHERE id = '{id_modifica}'"
    cur.execute(query)
    conn.commit()
if __name__ == '__main__':
    psw = 'cavazzoni123'
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("localhost", 50007))
    s.listen(10)

    conn, addr = s.accept()
    print('Connected by', addr)

    testo = "inserisci password ".encode()
    conn.send(testo)
    i = 0
    while i < 3:
        password = conn.recv(1024).decode()
        if password == psw:
            conn.send("Password esatta, inizia la comunicazione".encode())
            break
        else:
            i += 1
            tentativi_rimasti = 3 - i
            if i < 3:
                conn.send(f"ERRORE!! Password sbagliata, tentativi rimasti: {tentativi_rimasti}. Rinserisci password: ".encode())
            else:
                conn.send("ERRORE, TENTATIVI ESAURITI, CONNESSIONE CHIUSA...".encode())
                conn.close()
                exit()

    while True:
        testo = "Iniziamo ad effetuare le operazioni:\n 1.Leggi dati di una tabella \n 2. Elimina un'istanza di una tabella \n 3. Inserisci un'istanza nella tabella \n 4. Modifica un dato di una tabella \n 5. uscire.".encode()
        conn.send(testo)
        data = conn.recv(1024).decode()
        if not data:
            break
        if data == "5":

            testo = "grazie per aver usato questo codice, buona giornata...".encode()
            conn.send(testo)
            break

        if data == "1":

            testo = "Inserisci 1 per leggere un dipendente della tabella dipendenti_nicolas_cavazzoni o 2 per leggere una zona della tabella zone_di_lavoro_nicolas_cavazzoni: ".encode()
            conn.send(testo)
            scelta = conn.recv(1024).decode()

            if scelta == "1":

                testo = "Inserisci il nome del dipendente: ".encode()
                conn.send(testo)
                nome = conn.recv(1024).decode()
                par = {"nome": nome}
                result = db_get_dipendenti(par)
                conn.send(str(result).encode())
            
            else:

                testo = "Inserisci il nome della zona: ".encode()
                conn.send(testo)
                nome = conn.recv(1024).decode()
                par = {"nome": nome}
                result = db_get_zone(par)
                conn.send(str(result).encode())
        
        elif data == "2":

            testo = "Inserisci 1 per eliminare un dipendente della tabella dipendenti_nicolas_cavazzoni o 2 per eliminare una zona della tabella zone_di_lavoro_nicolas_cavazzoni: ".encode()
            conn.send(testo)
            scelta = conn.recv(1024).decode()

            if scelta == "1":

                testo = "Inserisci l'id del dipendente: ".encode()
                conn.send(testo)
                id_elimina = conn.recv(1024).decode()
                par = {"id_dipendente": id_elimina}
                db_elimina_dipendente(par)
            
            else:

                testo = "Inserisci l'id della zona: ".encode()
                conn.send(testo)
                id_elimina = conn.recv(1024).decode()
                par = {"id_zona": id_elimina}
                db_elimina_zona(par)
            
        
        elif data == "3":

            testo = "Inserisci 1 per inserire un dipendente della tabella dipendenti_nicolas_cavazzoni o 2 per inserire una zona della tabella zone_di_lavoro_nicolas_cavazzoni: ".encode()
            conn.send(testo)
            scelta = conn.recv(1024).decode()

            if scelta == "1":

                testo = "Inserisci il nome del dipendente da inserire: ".encode()
                conn.send(testo)
                nome = conn.recv(1024).decode()
                testo = "Inserisci il cognome del dipendente da inserire: ".encode()
                conn.send(testo)
                cognome = conn.recv(1024).decode()
                testo = "Inserisci dove lavora il dipendente da inserire: ".encode()
                conn.send(testo)
                posizione_lavoro = conn.recv(1024).decode()
                testo = "Inserisci la data di assunzione del dipendente da inserire: ".encode()
                conn.send(testo)
                data_assunzione = conn.recv(1024).decode()
                testo = "Inserisci lo stipendio del dipendente da inserire: ".encode()
                conn.send(testo)
                stipendio = conn.recv(1024).decode()
                testo = "Inserisci il numero di telefono del dipendente da inserire: ".encode()
                conn.send(testo)
                telefono = conn.recv(1024).decode()
                par = {"nome": nome, "cognome": cognome, "posizione_lavoro": posizione_lavoro, "data_assunzione": data_assunzione, "stipendio": stipendio, "telefono": telefono}
                db_inserisci_dipendente(par)

            else:

                testo = "Inserisci il nome della zona da inserire: ".encode()
                conn.send(testo)
                nome = conn.recv(1024).decode()
                testo = "Inserisci il numero dei clienti della zona da inserire: ".encode()
                conn.send(testo)
                numero_clienti = conn.recv(1024).decode()
                testo = "Inserisci i metri quadri della zona da inserire: ".encode()
                conn.send(testo)
                metri_quadri = conn.recv(1024).decode()
                par = {"nome": nome, "numero_clienti": numero_clienti, "metri_quadri": metri_quadri}
                db_inserisci_zona(par)

        elif data == "4":

            testo = "Inserisci 1 per modificare un dipendente della tabella dipendenti_nicolas_cavazzoni o 2 per modificare una zona della tabella zone_di_lavoro_nicolas_cavazzoni: ".encode()
            conn.send(testo)
            scelta = conn.recv(1024).decode()

            if scelta == "1":

                testo = "Inserisci l'id del dipendente di cui vuoi modificare i dati: ".encode()
                conn.send(testo)
                id_modifica = conn.recv(1024).decode()
                testo = "Inserisci il nome: ".encode()
                conn.send(testo)
                nome = conn.recv(1024).decode()
                testo = "Inserisci il cognome: ".encode()
                conn.send(testo)
                cognome = conn.recv(1024).decode()
                testo = "Inserisci la posizione di lavoro: ".encode()
                conn.send(testo)
                posizione_lavoro = conn.recv(1024).decode()
                testo = "Inserisci la data di assunzione: ".encode()
                conn.send(testo)
                data_assunzione = conn.recv(1024).decode()
                testo = "Inserisci lo stipendio: ".encode()
                conn.send(testo)
                stipendio = conn.recv(1024).decode()
                testo = "Inserisci il numero di telefono: ".encode()
                conn.send(testo)
                telefono = conn.recv(1024).decode()
                par = {"id": id_modifica, "nome": nome, "cognome": cognome, "posizione_lavoro": posizione_lavoro, "data_assunzione": data_assunzione, "stipendio": stipendio, "telefono": telefono}
                db_modifica_dipendente(par)

            else:

                testo = "Inserisci l'id della zona di cui vuoi modificare i dati: ".encode()
                conn.send(testo)
                id_modifica = conn.recv(1024).decode()
                testo = "Inserisci il nome: ".encode()
                conn.send(testo)
                nome = conn.recv(1024).decode()
                testo = "Inserisci il numero di clienti: ".encode()
                conn.send(testo)
                numero_clienti = conn.recv(1024).decode()
                testo = "Inserisci i metri quadri: ".encode()
                conn.send(testo)
                metri_quadri = conn.recv(1024).decode()
                par = {"id": id_modifica, "nome": nome, "numero_clienti": numero_clienti, "metri_quadri": metri_quadri}
                db_modifica_zona(par)

    conn.close()