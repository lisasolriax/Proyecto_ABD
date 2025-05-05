import tkinter as tk
from tkinter import ttk, messagebox
from clientes_crud import *
from productos_crud import *
from empleados_crud import *
from ordenes_crud import *
from metodos_pago_crud import *

def abrir_panel_empleado(empleado):
    app = PanelAdministrador(empleado)
    app.mainloop()

class PanelAdministrador(tk.Tk):
    def __init__(self, empleado):
        super().__init__()
        self.title(f"Panel - {empleado['rol'].title()}")
        self.geometry("900x600")
        self.configure(bg="#2c2c2b")
        self.empleado = empleado
        
        self.tabla_actual = None

        self.crear_widgets()

    def crear_widgets(self):
        frame_lateral = tk.Frame(self, bg="#2c2c2b")
        frame_lateral.pack(side="left", fill="y")

        rol = self.empleado['rol'].lower()

        opciones_por_rol = {
            "administrador": [
                ("Gestión de Empleados", self.cargar_empleados),
                ("Gestión de Clientes", self.cargar_clientes),
                ("Gestión de Métodos de Pago", self.cargar_metodos_pago),
                ("Gestión de Productos", self.cargar_productos),
                ("Gestión de Órdenes", self.cargar_ordenes),
            ],
            "vendedor": [
                ("Gestión de Clientes", self.cargar_clientes),
                ("Gestión de Métodos de Pago", self.cargar_metodos_pago),
                ("Gestión de Productos", self.cargar_productos),
                ("Gestión de Órdenes", self.cargar_ordenes),
            ],
            "almacenista": [
                ("Gestión de Productos", self.cargar_productos),
            ],
            "repartidor": [
                ("Ver Pedidos Asignados", self.cargar_ordenes),
                ("Actualizar Estado de Entrega", self.cargar_ordenes),
            ]
        }

        botones = opciones_por_rol.get(rol, [])

        for texto, comando in botones:
            tk.Button(frame_lateral, text=texto, width=30, height=2, bg="#1163c2", fg="white",font=("Times New Roman", 10, "bold"), command=comando).pack(pady=5)

        self.tree = ttk.Treeview(self)
        self.tree.pack(fill="both", expand=True, padx=10, pady=(10, 5))

        self.frame_botones = tk.Frame(self, bg="#2c2c2b")
        self.frame_botones.pack(side="bottom", pady=10)
        self.crear_botones_inferiores()

    def crear_botones_inferiores(self):
        rol = self.empleado['rol'].lower()

        for widget in self.frame_botones.winfo_children():
            widget.destroy()

        if rol in ["administrador", "vendedor", "almacenista"]:
            tk.Button(self.frame_botones, text="agregar",bg="#1163c2", fg="white",font=("Times New Roman", 10, "bold"), width=15, command=self.agregar_dato).pack(side="left", padx=10)
            tk.Button(self.frame_botones, text="actualizar",bg="#1163c2", fg="white",font=("Times New Roman", 10, "bold"), width=15, command=self.actualizar_dato).pack(side="left", padx=10)
        if rol in ["administrador", "vendedor"]:
            tk.Button(self.frame_botones, text="borrar", bg="#1163c2", fg="white",font=("Times New Roman", 10, "bold"), width=15, command=self.borrar_dato).pack(side="left", padx=10)
        if rol == "repartidor":
            tk.Button(self.frame_botones, text="actualizar estado de entrega", bg="#1163c2", fg="white",font=("Times New Roman", 10, "bold"), width=25, command=self.actualizar_dato).pack(side="left", padx=10)

    def cargar_clientes(self):
        self.tabla_actual = "clientes"
        datos = obtener_clientes()
        self.actualizar_treeview(datos)

    def cargar_productos(self):
        self.tabla_actual = "productos"
        datos = obtener_productos()
        self.actualizar_treeview(datos)

    def cargar_empleados(self):
        self.tabla_actual = "empleados"
        datos = obtener_empleados()
        self.actualizar_treeview(datos)

    def cargar_ordenes(self):
        self.tabla_actual = "ordenes"
        datos = obtener_ordenes()
        self.actualizar_treeview(datos)

    def cargar_metodos_pago(self):
        self.tabla_actual = "metodos_pago"
        datos = obtener_metodos_pago()
        self.actualizar_treeview(datos)

    def actualizar_treeview(self, datos):
        self.tree.delete(*self.tree.get_children())
        
        if not datos:
            columnas_por_tabla = {
                 "clientes": ["id_cliente", "nombre", "correo", "contrasena", "telefono", "direccion", "tipo_cliente"],
                 "productos": ["id_producto", "titulo", "artista", "genero", "precio", "cantidad", "fecha_lanzamiento"],
                 "empleados": ["id_empleado", "nombre", "correo", "contrasena", "telefono", "direccion", "rol", "fecha_contratacion"],
                 "ordenes": ["id_orden", "id_cliente", "total", "tipo_compra", "id_pago", "estado"],
                 "metodos_pago": ["id_pago", "metodo_de_pago"]
            }

            columnas = columnas_por_tabla.get(self.tabla_actual, [])
            self.tree["columns"] = columnas
            self.tree["show"] = "headings"

            for col in columnas:
                self.tree.heading(col, text=col)
                self.tree.column(col, width=120)
            return
        
        columnas = list(datos[0].keys())
        self.tree["columns"] = columnas
        self.tree["show"] = "headings"

        for col in columnas:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)

        for fila in datos:
            self.tree.insert("", "end", values=list(fila.values()))

    def agregar_dato(self):
        self.abrir_ventana_formulario("agregar")

    def actualizar_dato(self):
        self.abrir_ventana_formulario("actualizar")

    def borrar_dato(self):
        item = self.tree.focus()
        if not item:
            messagebox.showwarning("Error", "Selecciona un elemento para eliminar.")
            return
        fila = self.tree.item(item)["values"]
        id_valor = fila[0]

        if messagebox.askyesno("Confirmar", f"¿Seguro que deseas borrar {self.tabla_actual} con ID {id_valor}?"):
            if self.tabla_actual == "clientes":
                eliminar_cliente(id_valor)
            elif self.tabla_actual == "productos":
                eliminar_producto(id_valor)
            elif self.tabla_actual == "empleados":
                eliminar_empleado(id_valor)
            elif self.tabla_actual == "ordenes":
                eliminar_orden(id_valor)
            elif self.tabla_actual == "metodos_pago":
                eliminar_metodo_pago(id_valor)

            messagebox.showinfo("Eliminado", "El registro fue eliminado correctamente.")
            getattr(self, f"cargar_{self.tabla_actual}")()

    def abrir_ventana_formulario(self, tipo):
        ventana = tk.Toplevel(self)
        ventana.title(f"{tipo.title()} {self.tabla_actual.title()}")
        ventana.geometry("400x500")
        ventana.configure(bg="#2c2c2b")

        campos = list(self.tree["columns"])
        entradas = {}

        campos_auto = {
            "empleados": ["id_empleado", "fecha_contratacion"],
            "clientes": ["id_cliente"],
            "ordenes": ["id_orden"],
            "metodos_pago": ["id_metodo"]
        }

        ignorar = campos_auto.get(self.tabla_actual, [])
        valores_actuales = {}

        if tipo == "actualizar":
            item = self.tree.focus()
            if not item:
                messagebox.showwarning("Advertencia", "Selecciona un elemento para actualizar.")
                ventana.destroy()
                return
            valores = self.tree.item(item)["values"]
            valores_actuales = dict(zip(campos, valores))

        for campo in campos:
            if tipo == "agregar" and campo in ignorar:
                continue

            if self.empleado['rol'].lower() == "repartidor" and campo != "estado_entrega":
                continue

            tk.Label(ventana, text=campo.title(), bg="#F5F5F5").pack(pady=5)
            entrada = tk.Entry(ventana)
            entrada.pack()

            if tipo == "actualizar":
                entrada.insert(0, str(valores_actuales.get(campo, "")))
                if campo == campos[0]:
                    entrada.config(state="disabled")

            entradas[campo] = entrada

        def guardar():
            datos = {}
            for campo, entrada in entradas.items():
                if entrada["state"] != "disabled":
                    valor = entrada.get().strip()
                    if valor == "":
                        messagebox.showerror("Error", "Completa todos los campos.")
                        return
                    datos[campo] = valor
                else:
                    datos[campo] = valores_actuales.get(campo)

            if tipo == "agregar":
                self.insertar_en_tabla(datos)
            else:
                self.actualizar_en_tabla(datos)

            ventana.destroy()
            getattr(self, f"cargar_{self.tabla_actual}")()

        tk.Button(ventana, text="Guardar", bg="#4CAF50", fg="white", command=guardar).pack(pady=20)

    def insertar_en_tabla(self, datos):
        if self.tabla_actual == "clientes":
            crear_cliente(
                datos["nombre"],
                datos["correo"],
                datos["contrasena"],
                datos["telefono"],
                datos["direccion"],
                datos["tipo_cliente"]
            )
        elif self.tabla_actual == "productos":
            crear_producto(
                datos["id_producto"],
                datos["titulo"],
                datos["artista"],
                datos["genero"],
                datos["precio"],
                datos["cantidad"],
                datos["fecha_lanzamiento"]
            )
        elif self.tabla_actual == "empleados":
            crear_empleado(
                datos["nombre"],
                datos["correo"],
                datos["contrasena"],
                datos["telefono"],
                datos["direccion"],
                datos["rol"]
            )
        elif self.tabla_actual == "ordenes":
            crear_orden(
                datos["id_cliente"],
                datos["total"],
                datos["tipo_compra"],
                datos["id_pago"],
                datos["estado"]                
            )
        elif self.tabla_actual == "metodos_pago":
            crear_metodo_pago(
                datos["metodo_de_pago"]
            )

    def actualizar_en_tabla(self, datos):
        if self.tabla_actual == "clientes":
            actualizar_cliente(
                datos["id_cliente"],
                datos["nombre"],
                datos["correo"],
                datos["contrasena"],
                datos["telefono"],
                datos["direccion"],
                datos["tipo_cliente"]
            )
        elif self.tabla_actual == "productos":
            actualizar_producto(
                datos["id_producto"],
                datos["titulo"],
                datos["artista"],
                datos["genero"],
                datos["precio"],
                datos["cantidad"],
                datos["fecha_lanzamiento"]
            )
        elif self.tabla_actual == "empleados":
            actualizar_empleado(
                datos["id_empleado"],
                datos["nombre"],
                datos["correo"],
                datos["contrasena"],
                datos["telefono"],
                datos["direccion"],
                datos["rol"]
            )
        elif self.tabla_actual == "ordenes":
            actualizar_orden(
                datos["id_orden"],
                datos["id_cliente"],
                datos["total"],
                datos["tipo_compra"],
                datos["id_pago"],
                datos["estado"]
            )
        elif self.tabla_actual == "metodos_pago":
            actualizar_metodo_pago(
                datos["id_pago"],
                datos["metodo_de_pago"]
            )