from db_coneccion import get_connection

def crear_metodo_pago(metodo_de_pago):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Metodos_Pago (metodo_de_pago) VALUES (%s)", (metodo_de_pago,))
    conn.commit()
    cursor.close()
    conn.close()

def obtener_metodos_pago():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Metodos_Pago")
    metodos = cursor.fetchall()
    cursor.close()
    conn.close()
    return metodos

def actualizar_metodo_pago(id_pago, metodo_de_pago):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE Metodos_Pago SET metodo_de_pago=%s WHERE id_pago=%s", (metodo_de_pago, id_pago))
    conn.commit()
    cursor.close()
    conn.close()

def eliminar_metodo_pago(id_pago):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Metodos_Pago WHERE id_pago=%s", (id_pago,))
    conn.commit()
    cursor.close()
    conn.close()
