# DOCKER
- Es una maquina virtual: "Ordenador dentro de un ordenador"
- Puedes usar varios sistemas operativos sin dañar tu equipo
- Sistema de contenedores 
- Ejemplos de programas: VirtualBox, VMware, Hyper-V

- Plataforma creada con el fin de **desarrollar, implementar y ejecutar aplicaciones dentro de contenedores**



### VENTAJAS

- Nos olvidamos de "En mi ordenador funciona..." 
- Mucho más ligero y escalable que una máquina virtual. 
- Trabajar en equipos de desarrollo. 
- La idea es emular durante el desarrollo lo máximo posible nuestro entorno de producción.



### PROCESO DE CREACIÓN

**Dockerfile**: Un Dockerfile es un archivo de texto plano que contiene una serie de instrucciones necesarias para crear una imagen. 
- Instrucciones para montar el coche 

**Docker image**: Las imágenes de Docker son esencialmente una instantánea de un contenedor. Las imágenes se crean con el comando **build**, que crean un contenedor. 
- Coche montado 

**Container**: es una imagen de Docker cuando empieza a funcionar, es decir, cuando cobra vida. 
- Coche en marcha



### COMANDOS

- Crear y ejecutar un contenedor nuevo a partir de una imagen de Docker: **docker run**
- Ver todos los contenedores de tu sistema, tanto los que están ejecutándose como los que están detenidos: **docker ps -a**
- Ponerle nombre: **--name web-server**
- Le pone el nombre web-server
- Eliminar contenedores: **docker rm**
- Buscar contenedores específicos: **docker ps -a | grep**
- Buscar información sobre el comando stop dentro de la ayuda de Docker: **docker help | grep stop**
- Crea y ejecuta un contenedor de Nginx (un servidor web) con un nombre personalizado y acceso desde tu navegador: **docker run --name web-server -p 80:80 nginx** (Mapea el puerto 80 del host (tu PC) al puerto 80 del contenedor)
- Inicia un contenedor que esta detenido: **docker start**
- Detiene un contenedor que está en ejecución: **docker stop**
- Reinicia un contenedor, es decir, lo detiene si está corriendo y lo vuelve a iniciar automáticamente: **docker restart**
- Programar tareas para que se ejecuten automáticamente en momentos específicos, sin intervención humana: **crontab**
- Entrar en el contenedor: **docker exec**
- Listar imagenes: **docker images**
- Elimina imagen de Docker: ***docker image rm**
- Construir imagenes: **docker build -t** el -t etiqueta la imagen con un nombre
- Descarga la última versión oficial de Python: **docker pull python**
- Ver todos los comandos docker pull que has ejecutado previamente: **history | grep "docker pull"** Muy útil si quieres repetir, revisar o depurar descargas de imágenes Docker



## DOCKER HUB

Nos permite descargar y subir imágenes de Docker de forma sencilla.

Podemos compararlo con GitHub, donde gestionamos nuestro código fuente. Sin embargo, en el caso de Docker Hub, en lugar de código, trabajamos con imágenes de contenedores, que podemos obtener o publicar según nuestras necesidades



### Dockerfile

Documento de texto que contiene todas las instrucciones necesarias para construir una imagen de Docker

*FROM python:3.11-Slim*     --> IMAGEN BASE, elegimos una imagen oficial de Python
*WORKDIR /app*              --> Define dónde se harán todas las operaciones dentro del contenedor

*COPY . .*                  --> Copiamos el resto del código de la aplicación

*CMD ["python", "main.py"]* --> Definimos el comando que arranca la aplicación




### Construimos la imagen (montamos coche)

Con el Dockerfile en tu directorio, puedes construir y ejecutar la imagen.

**-t** Etiqueta la imagen con el nombre mi-app:latest.
**.** Busca el Dockerfile en el directorio actual.
**docker build -t mi-app:latest**


### Ejecutamos el contenedor(arrancamos coche)

Una vez construida la imagen ya podemos arrancar nuestro contenedor 
**-d** ejecuta en modo detached (segundo plano): **docker run --help | grep detach**



*Servidor de development*: entorno donde los programadores prueban su aplicación mientras la están creando; no es un servidor real
*Kernel:* núcleo del sistema operativo; hace de puente entre el hardware y los programas; quien coordina todo
*Ubuntu*: distribucion de Linux llamada Debian




