from db_config import get_connection

def crear_producto(id_producto, titulo, artista, genero, precio, cantidad, fecha_de_lanzamiento):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO Productos (id_producto, titulo, artista, genero, precio, cantidad, fecha_de_lanzamiento) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (id_producto, titulo, artista, genero, precio, cantidad, fecha_de_lanzamiento))
    conn.commit()
    cursor.close()
    conn.close()

def obtener_productos():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Productos")
    productos = cursor.fetchall()
    cursor.close()
    conn.close()
    return productos

def actualizar_producto(id_producto, titulo, artista, genero, precio, cantidad, fecha_de_lanzamiento):
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE Productos SET titulo=%s, artista=%s, genero=%s, precio=%s, cantidad=%s, fecha_de_lanzamiento=%s WHERE id_producto=%s"
    cursor.execute(query, (titulo, artista, genero, precio, cantidad, fecha_de_lanzamiento, id_producto))
    conn.commit()
    cursor.close()
    conn.close()

def eliminar_producto(id_producto):
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM Productos WHERE id_producto=%s"
    cursor.execute(query, (id_producto,))
    conn.commit()
    cursor.close()
    conn.close()
