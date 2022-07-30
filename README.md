# Detect_OSystem

Un pequeño script en `python` para ver la información de una maquina victima, especificamente de red

## Requisitos

* Python
* Linux

## Instrucciones

1. Darle todos los permisos a los archivos

~~~bash
$ sudo chmod 777 main.py detectSys.py
~~~

2. Ejecutar el archivo `main.py` 

~~~bash
$ python3 main.py

[!] uso: python3 main.py <direccion ip>
~~~

~~~bash
$ python3 main.py 10.10.10.1

[*] ip: 10.10.10.1
[*] ttl: 64
[*] os: Linux

~~~