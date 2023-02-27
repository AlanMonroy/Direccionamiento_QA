"""import scapy.all as scapy

def escanear(direccion_ip):
    solicitud_arp = scapy.ARP(pdst=direccion_ip)
    broadcast = scapy.Ether()
    scapy.ls(scapy.Ether())

def encontrar(direccion_ip):
    solicitud_arp = scapy.ARP(pdst=direccion_ip)
    print(solicitud_arp.summary())

def escanear_1(direccion_ip):
    solicitud_arp = scapy.ARP(pdst=direccion_ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    # Fusionamos
    solicitud_arp_broadcast = broadcast/solicitud_arp
    respuesta = scapy.srp(solicitud_arp_broadcast, timeout=1)[0]
    print("IP\t\t\tMAC Address\n-----------------------------------------")
    for element in respuesta:
        print(element[1].psrc + '\t\t' + element[1].hwsrc)

escanear_1("10.200.22.1/24")"""

#escanear("10.200.10.59/24")
#encontrar("10.200.10.1/24")
import who_is_on_my_wifi
#Mostrar página de ayuda:
#who_is_on_my_wifi.help()
#Ver licencia:
#who_is_on_my_wifi.license()
#Mostrar la página de contacto:
#who_is_on_my_wifi.contact()
#Ver los dispositivos conectados:
#print(who_is_on_my_wifi.who())
#Mostrar información del dispositivo:
#who_is_on_my_wifi.device()
import os
import time
def encontrar_dispositivos():
    print(who_is_on_my_wifi.who())

def conectar():
    contraseña = "Comercio03"
    #net use h: \\10.200.22.140\c / user: administradoroxxo
    #os.system("net use \\10.200.10.59\c /user:QA " + contraseña)
    #os.system("net use \\10.200.10.59\c /user:QA Comercio03")
    #os.system("net use \\10.200.10.59\c /user:QA Comercio03")
    #os.system('cmd /c "net use \\10.200.10.59\c /user:QA Comercio03"')
    #os.system('cmd /c "ipconfig"')
    os.system("net use \\\\10.200.10.59\c /user:QA Comercio03")


def desconectar():
    os.system("net use \\\\10.200.10.59\c /delete")
    #net use * /delete or net use * /d /y
    #net use k: /delete

def buscar():
    ruta = "//10.200.10.59/c/XPOS/Logs/traceProcess.log"
    with open(ruta) as archivo:
        contenido = archivo.readlines()
        for i in contenido:
            print(i)

#conectar()
#os.system("net use")
#buscar()
encontrar_dispositivos()
#desconectar()

"""Voy a integrar psexec en python pero inicie pruebas desde CMD, instale PSTools dentro de C, y lo agregue 
a las variables de entorno, por el momento tengo un detalle de que no tengo permisos para ejecutar comandos sin 
que el host me lo permita."""

