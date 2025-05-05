from db_coneccion import get_connection

def crear_cliente(nombre, correo, contrasena, telefono, direccion, tipo_cliente="linea"):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    INSERT INTO Clientes (nombre, correo, contrasena, telefono, direccion, tipo_cliente)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (nombre, correo, contrasena, telefono, direccion, tipo_cliente))
    conn.commit()
    cursor.close()
    conn.close()

def obtener_clientes():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM Clientes"
    cursor.execute(query)
    clientes = cursor.fetchall()
    cursor.close()
    conn.close()
    return clientes

def actualizar_cliente(id_cliente, nombre, correo, contrasena, telefono, direccion, tipo_cliente):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    UPDATE Clientes
    SET nombre = %s, correo = %s, contrasena = %s, telefono = %s, direccion = %s, tipo_cliente = %s
    WHERE id_cliente = %s
    """
    cursor.execute(query, (nombre, correo, contrasena, telefono, direccion, tipo_cliente, id_cliente))
    conn.commit()
    cursor.close()
    conn.close()

def eliminar_cliente(id_cliente):
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM Clientes WHERE id_cliente = %s"
    cursor.execute(query, (id_cliente,))
    conn.commit()
    cursor.close()
    conn.close()
