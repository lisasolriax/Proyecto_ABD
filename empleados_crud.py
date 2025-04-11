from db_coneccion import get_connection

def crear_empleado(nombre, correo, contrasena, telefono, direccion, rol, id_empresa_reparto):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    INSERT INTO Empleados (nombre, correo, contrasena, telefono, direccion, rol, id_empresa_reparto)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (nombre, correo, contrasena, telefono, direccion, rol, id_empresa_reparto))
    conn.commit()
    cursor.close()
    conn.close()

def obtener_empleados():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Empleados")
    empleados = cursor.fetchall()
    cursor.close()
    conn.close()
    return empleados

def actualizar_empleado(id_empleado, nombre, correo, contrasena, telefono, direccion, rol, id_empresa_reparto):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    UPDATE Empleados SET nombre=%s, correo=%s, contrasena=%s, telefono=%s, direccion=%s, rol=%s, id_empresa_reparto=%s
    WHERE id_empleado=%s
    """
    cursor.execute(query, (nombre, correo, contrasena, telefono, direccion, rol, id_empresa_reparto, id_empleado))
    conn.commit()
    cursor.close()
    conn.close()

def eliminar_empleado(id_empleado):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Empleados WHERE id_empleado=%s", (id_empleado,))
    conn.commit()
    cursor.close()
    conn.close()
