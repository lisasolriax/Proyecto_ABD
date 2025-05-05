import tkinter as tk
from tkinter import messagebox
from db_coneccion import get_connection
from panel_empleado import abrir_panel_empleado

ventana = tk.Tk()
ventana.title("Discos Deluxe - Bienvenido")
ventana.geometry("600x750")
ventana.configure(bg="#2c2c2b") 

fuente_titulo = ("Times New Roman", 16, "bold")
fuente_texto = ("Times New Roman", 10, "italic")

# FUNCIONES 

def mostrar_error(mensaje):
    messagebox.showerror("Error", mensaje)

def campos_vacios(campos):
    return any(not campo.get().strip() for campo in campos)

def iniciar_cliente():
    if campos_vacios([correo_cliente, contrasena_cliente]):
        mostrar_error("Por favor, completa todos los campos de inicio de sesión (cliente).")
        return

    correo = correo_cliente.get()
    contrasena = contrasena_cliente.get()

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Clientes WHERE correo=%s AND contrasena=%s", (correo, contrasena))
    cliente = cursor.fetchone()

    if cliente:
        messagebox.showinfo("Bienvenido", f"¡Hola, {cliente['nombre']}! Has iniciado sesión como Cliente.")
    else:
        mostrar_error("Correo o contraseña inválidos para cliente.")

    cursor.close()
    conn.close()

def iniciar_empleado():
    if campos_vacios([correo_empleado, contrasena_empleado]):
        mostrar_error("Por favor, completa todos los campos de inicio de sesión (empleado).")
        return

    correo = correo_empleado.get()
    contrasena = contrasena_empleado.get()

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Empleados WHERE correo=%s AND contrasena=%s", (correo, contrasena))
    empleado = cursor.fetchone()
        
    if empleado:
        messagebox.showinfo("Bienvenido", f"Has iniciado sesión como {empleado['rol'].title()}.")
        abrir_panel_empleado(empleado)
    else:
        mostrar_error("Correo o contraseña inválidos para empleado.")

    cursor.close()
    conn.close()

def registrar_cliente():
    if campos_vacios([nombre_reg, correo_reg, contrasena_reg, telefono_reg, direccion_reg]):
        mostrar_error("Por favor, completa todos los campos del registro.")
        return

    nombre = nombre_reg.get()
    correo = correo_reg.get()
    contrasena = contrasena_reg.get()
    telefono = telefono_reg.get()
    direccion = direccion_reg.get()

    conn = get_connection()
    cursor = conn.cursor()
    try:
        query = "INSERT INTO Clientes (nombre, correo, contrasena, telefono, direccion, tipo_cliente) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (nombre, correo, contrasena, telefono, direccion, "Linea"))
        conn.commit()
        messagebox.showinfo("Registro exitoso", "Cliente registrado correctamente.")
        for campo in [nombre_reg, correo_reg, contrasena_reg, telefono_reg, direccion_reg]:
            campo.delete(0, tk.END)
    except:
        mostrar_error("No se pudo registrar el cliente. Verifica que el correo no esté duplicado.")
    finally:
        cursor.close()
        conn.close()

# INTERFAZ 

def seccion(titulo):
    tk.Label(ventana, text=titulo, font=fuente_titulo, fg="#1083dc", bg="#2c2c2c").pack(pady=10)

def etiqueta(texto):
    tk.Label(ventana, text=texto, font=fuente_texto, fg="white", bg="#2c2c2c").pack()

def campo_entry():
    entry = tk.Entry(ventana, font=fuente_texto)
    entry.pack()
    return entry

# CLIENTE 
seccion("Inicio de Sesión - Cliente")
etiqueta("Correo:")
correo_cliente = campo_entry()
etiqueta("Contraseña:")
contrasena_cliente = tk.Entry(ventana, show="*", font=fuente_texto)
contrasena_cliente.pack()
tk.Button(ventana, text="Iniciar como Cliente", bg="#1163c2", fg="white",font=("Times New Roman", 10, "bold"), command=iniciar_cliente).pack(pady=8)

# REGISTRO 
seccion("¿No tienes cuenta? Regístrate - Cliente")
etiqueta("Nombre:")
nombre_reg = campo_entry()
etiqueta("Correo:")
correo_reg = campo_entry()
etiqueta("Contraseña:")
contrasena_reg = tk.Entry(ventana, show="*", font=fuente_texto)
contrasena_reg.pack()
etiqueta("Teléfono:")
telefono_reg = campo_entry()
etiqueta("Dirección:")
direccion_reg = campo_entry()
tk.Button(ventana, text="Registrarse como Cliente", bg="#1163c2", fg="white", font=("Times New Roman", 10, "bold"), command=registrar_cliente).pack(pady=12)

# EMPLEADO
seccion("Inicio de Sesión - Empleado")
etiqueta("Correo:")
correo_empleado = campo_entry()
etiqueta("Contraseña:")
contrasena_empleado = tk.Entry(ventana, show="*", font=fuente_texto)
contrasena_empleado.pack()
tk.Button(ventana, text="Iniciar como Empleado", bg="#1163c2", fg="white", font=("Times New Roman", 10, "bold"), command=iniciar_empleado).pack(pady=8)

# SALIR
tk.Button(ventana, text="Salir", bg="#cc0000", fg="white", font=("Times New Roman", 10, "bold"), command=ventana.destroy).pack(pady=10)

ventana.mainloop()