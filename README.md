# Proyecto_ABD
un proyecto de base de datos que trabajara en una tienda de discos vinilos.
La libreria que se maneja es "tkinter".

https://github.com/lisasolriax/Proyecto_ABD.git

Clonar tu repositorio desde GitHub
1. Abre tu terminal y ejecuta
git clone https://github.com/lisasolriax/Proyecto_ABD.git
cd Proyecto_ABD

Crear y activar entorno virtual
1. creamos el entorno virtual
python -m venv proyecto_ABD
2. Habilitamos el entorno virtual
.\proyecto_ABD\scripts\activate 
3. instalamos el conector a mysql 
pip install mysql -connector-python
4. instalamos la libreria  
pip install pyqt6
5. Activar MySQL
net start mysql
6. Luego accede a la consola MySQL si quieres comprobarlo
mysql -u root -p

Subir archivos a tu repositorio desde Visual Studio Code
1. Verifica estado de Git
git status
2. Agrega archivos al staging
git add
3. Confirma los cambios
git commit -m "Mensaje claro sobre lo que cambiaste"
4. Sube los cambios a GitHub
git push origin main

como funciona el proyecto
1. en la interfaz inicio_registro.py se ingresa el inico de sesion para trabajadores y empleados.
2. para ingresar como administrador ponga lisandro@hotmail.com como correo y solriax234 como contraseña en inico de sesion - empleado.
3. se abrira la interfaz de panel_empleado y dependiendo de su rol se le otrogara las herramientas que necesita para cumplir su trabajo.

