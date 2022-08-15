# Detect_OSystem

Script en `python` que devuelve la información en red de una maquina victima

## Requisitos

* Python
* Linux

## Instrucciones

1. Darle todos los permisos a los archivos

~~~bash
$ sudo chmod 777 main.py detectSys.py
~~~

2. Ejecutar el archivo `main.py`

*Al ejecutar el archivo, mostrara información de uso*

~~~bash
$ python3 main.py

[!] uso: python3 main.py <direccion ip>
~~~

*Este retornara los datos de la maquina victima para comenzar el hacking*

~~~bash
$ python3 main.py 10.10.10.10

[*] ip: 10.10.10.10
[*] ttl: 64
[*] os: Linux
[*] open ports: [ 21, 22, 80, 587 ]
~~~

# **METR1CKA**

> [Visitanos en DevBlogs](https://metr1cka.github.io "Pagina web")

> [Mas repositorios](https://github.com/METR1CKA "Mi perfil")
