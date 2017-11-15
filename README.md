# blog
Aplicación Flask de prueba

## Software necesario
* Python 2.7 (lenguaje de programación)
* pip (gestor de paquetes de python)
* git (sistema de control de versiones)
* virtualenv (paquete de python encargado de generar entornos aislados de desarrollo, instalar con: __pip install virtualenv__
* editor de codigo de preferencia (visual studio code, sublime text, notepad++)

## Configuración

### Instalar Python
1. Link de descarga: https://www.python.org/ftp/python/2.7.14/python-2.7.14.msi
2. Configurar path de windows agregandole la siguiente entrada: __;C:\Python27;C:\Python27\Scripts;__
3. Abrir una consola (cmd) y escribir python, si se abre la shell de python la instalación ha sido correcta.

### Instalar pip
1. Descargar el siguiente instalador https://bootstrap.pypa.io/get-pip.py
2. Ejecutar el archivo get-pip.py desde el cmd: __python get-pip.py__ (Quizas necesites permisos de administrador)

### Instalar git
1. Descargar binario desde:  https://git-scm.com/downloads
2. Instalar

### Instalar virtualenv
1. En un cmd escribir: __pip install virtualenv__

### Clonar repositorio de código fuente con git
1. Configurar una cuenta en github
2. Abrir un cmd y en una ruta del sistema donde quieras guardar el proyecto escribir: __git clone https://github.com/javierhuerta/blog.git__

### Configurar proyecto en modo desarrollo
> Para las siguientes instrucciones utilice la consola de windows (cmd)

1. Ingresar al proyecto clonado con git: __cd blog__
2. Crear un entorno virtual (usando virtualenv) dentro del proyecto clonado: __virtualenv venv__
3. Activar virtualenv: __venv\Scripts\activate__
4. Instalar requerimientos del proyecto con pip: __pip install -r requirements.txt__
5. Levantar servidor de prueba: __python wsgi.py__
6. Revisar en el navegador la ruta: http://127.0.0.1:5000

