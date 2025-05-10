from CRUD_Y_CONEXION.db_coneccion import get_connection

def crear_orden(id_cliente, total, tipo_compra, id_pago, estado="Pendiente"):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    INSERT INTO Ordenes (id_cliente, total, tipo_compra, id_pago, estado)
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(query, (id_cliente, total, tipo_compra, id_pago, estado))
    conn.commit()
    cursor.close()
    conn.close()

def obtener_ordenes():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Ordenes")
    ordenes = cursor.fetchall()
    cursor.close()
    conn.close()
    return ordenes

def actualizar_orden(id_orden, id_cliente, total, tipo_compra, id_pago, estado):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    UPDATE Ordenes
    SET id_cliente = %s, total = %s, tipo_compra = %s, id_pago = %s, estado = %s
    WHERE id_orden = %s
    """
    cursor.execute(query, (id_cliente, total, tipo_compra, id_pago, estado, id_orden))
    conn.commit()
    cursor.close()
    conn.close()

def eliminar_orden(id_orden):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Ordenes WHERE id_orden = %s", (id_orden,))
    conn.commit()
    cursor.close()
    conn.close()
