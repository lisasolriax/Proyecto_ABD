from db_coneccion import get_connection

def crear_empresa(corre_empresa, correo, contrasena, direccion):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    INSERT INTO Empresas_Reparto (corre_empresa, correo, contrasena, direccion)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (corre_empresa, correo, contrasena, direccion))
    conn.commit()
    cursor.close()
    conn.close()

def obtener_empresas():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Empresas_Reparto")
    empresas = cursor.fetchall()
    cursor.close()
    conn.close()
    return empresas

def actualizar_empresa(id_empresa, corre_empresa, correo, contrasena, direccion):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    UPDATE Empresas_Reparto SET corre_empresa=%s, correo=%s, contrasena=%s, direccion=%s
    WHERE id_empresa=%s
    """
    cursor.execute(query, (corre_empresa, correo, contrasena, direccion, id_empresa))
    conn.commit()
    cursor.close()
    conn.close()

def eliminar_empresa(id_empresa):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Empresas_Reparto WHERE id_empresa=%s", (id_empresa,))
    conn.commit()
    cursor.close()
    conn.close()