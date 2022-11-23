#Cambio de datos en txt
class Configuraciones():
    #Configuracion tipo 1 que configura tal cual por identificador(TAE)
    def configuracion1(self, archivo,valor_de_busqueda, cambio):
        with open(archivo) as archivo_temporal:
            datafile = archivo_temporal.readlines()

        validacion = False
        for fila,linea in enumerate(datafile): #Se recorre las lineas del datafile mientras se enumeran
            lista1=list()
            validacion_espacios = False
            for letra in linea:  #Recorre letra por letra la linea
                lista1.append(letra)
                texto = "".join(lista1)
                texto1 = texto.strip(" ")
                if texto1 == valor_de_busqueda:
                    #print(texto)
                    #print("Texto sin espacios",texto1)
                    datafile[fila] = f"{texto}{cambio}\n" #Se realiza el cambio de línea
                    #print(datafile[fila])
                    validacion = True

        if validacion is True:
            archi = open(archivo, 'w')
            for linea in datafile:  #Reescribe el datafile al txt
                archi.write(linea)

    #Configuracion tipo 2 para archivos dividos por apartados (ServBan, TJComm)
    def configuracion2(self, archivo,valor_de_busqueda,etiqueta,cambio):
        with open(archivo) as archivo_temporal:
            datafile = archivo_temporal.readlines()

        validacion = False
        apartado_encontrado = False
        for fila,linea in enumerate(datafile):                  #Se recorre las lineas del datafile mientras se enumeran
            for letra in linea:                                 #Recorre letra por letra la linea
                if valor_de_busqueda in linea:
                    apartado_encontrado = True

                if apartado_encontrado and etiqueta in linea:   #Si la comprobacion es cierta y etiqueta esta presente en el apartado
                    datafile[fila] = f"{etiqueta}={cambio}\n"   #Se realiza el cambio de línea
                    apartado_encontrado = False
                    validacion = True
                    #print(datafile[fila])

        if validacion is True:
            archi = open(archivo, 'w')
            for linea in datafile:  #Reescribe el datafile al txt
                archi.write(linea)

    #CONFIGURACION TIPO 3 para archivos tipo XML que usan etiquetas y encode utf-8(ED)
    def configuracion3(self, archivo,valor_de_busqueda, cambio):
        with open(archivo,encoding = "UTF-8") as archivo_temporal:
            datafile = archivo_temporal.readlines()

        VALIDACION = False                          #Check para validar si fue encontrado el puntero
        for fila,linea in enumerate(datafile):      #Se recorre las lineas del datafile mientras se enumeran
            lista1=list()   
            for letra in linea:                     #Recorre letra por letra la linea
                lista1.append(letra)                #Agrega cada letra a una lista
                texto = "".join(lista1)             #Une la lista en una variable
                texto1 = texto.strip(" ")           #Elimina los espacios para una comprobacion

                if texto1 == valor_de_busqueda:
                    primer_texto = texto ; lista1.clear()       #Guarda primera parte de la linea en variable y limpia la lista de la linea
                    VALIDACION = True    

            COMPROBACION=True                       #EL check para encontrar el url dentro de los parentesis
            if VALIDACION == True:
                #Creacion de segunda lista para eliminar la url antigua
                lista2=list()
                for i in lista1:
                    if i == '"' and COMPROBACION:   #Si encuntras el parentesis es por que hasta ahi llego la url
                        lista2.clear()              #Eliminas lo que tenia almacenado (la url ya que va al principio)
                        COMPROBACION = False        #Se cambia el check para no volver a eliminar cuando encuentre otro parentesis
                    else:
                        lista2.append(i)            #Continua agregando el texto sobrante a una lista

                texto2= "".join(lista2)             #Se almacena el texto sobrante a una variable
                datafile[fila] = f'{primer_texto}{cambio}{texto2}' #Se realiza el cambio de línea
                break

        if VALIDACION is True:
            archi = open(archivo, 'w', encoding="utf-8")
            for linea in datafile:  #Reescribe el datafile al txt
                archi.write(linea)

    #CONFIGURACION TIPO 4 para archivos tipo XML que usan etiquetas y encode utf-8
    def configuracion4(self, archivo,valor_de_busqueda, cambio):
        with open(archivo,encoding = "UTF-8") as archivo_temporal:
            datafile = archivo_temporal.readlines()

        VALIDACION = False                              #Check para validar si fue encontrado el puntero
        for fila,linea in enumerate(datafile):          #Se recorre las lineas del datafile mientras se enumeran
            #Creacion de segunda lista para eliminar la url antigua
            lista_original=list() ; lista2=list()       
            VALIDAR_IGUAL=True
            for i in linea:                             #Recorre letra por letra la linea
                lista_original.append(i)                #Agrega cada letra a una lista
                texto = "".join(lista_original)         #Une la lista en una variable
                texto1 = texto.strip(" ")               #Elimina los espacios para una comprobacion
                if i == "<":                            #Si encuntras el  es por que hasta ahi llego la url
                    lista2.clear()                      #Eliminas lo que tenia almacenado (la url ya que va al principio)
                    lista2.append(i)
                elif i == "=" and VALIDAR_IGUAL:
                    lista2.append(i)                    
                    VALIDAR_IGUAL=False
                else:
                    lista2.append(i)                    #Continua agregando el texto sobrante a una lista
                texto2 = "".join(lista2)
                texto3 = texto2.strip(" ")

                if texto3 == valor_de_busqueda:
                    primer_texto = texto ; lista_original.clear()       #Guarda primera parte de la linea en variable y limpia la lista de la linea
                    VALIDACION = True    

            conteo=0                                #Iterador para saber cuantas veces ha pasado parentesis (la url esta dentro de parentesis)
            if VALIDACION == True:                  #Si ya encontro la clave
                #Apartado para eliminar la url antigua
                lista_url=list()
                for x in lista_original:
                    if x == '"' and conteo != 2:    #Encontrar los parentesis para saber donde esta la ruta y si se encuentran los 2 parentesis se brica al else
                        lista_url.clear()           #Eliminas lo que tenia almacenado (la url origininal)
                        conteo+=1                   #Acumula la cantidad de parentesis pasados
                    else:
                        lista_url.append(x)         #Continua agregando el texto sobrante a una lista

                sobrante= "".join(lista_url)             #Se almacena el texto sobrante a una variable
                datafile[fila] = f'{primer_texto}{cambio}{sobrante}' #Se realiza el cambio de línea
                #print(datafile[fila])
                break

        #Reescribe el datafile
        if VALIDACION is True:
            archi = open(archivo, 'w', encoding="utf-8")
            for linea in datafile:  #Reescribe el datafile al txt
                archi.write(linea)

#CONFIGURACION TIPO 5 para archivos tipo XML que usan etiquetas y encode utf-8
    def configuracion5(self, archivo,valor_de_busqueda, cambio):
        with open(archivo,encoding = "UTF-8") as archivo_temporal:
            datafile = archivo_temporal.readlines()

        VALIDACION = False                              #Check para validar si fue encontrado el puntero
        for fila,linea in enumerate(datafile):          #Se recorre las lineas del datafile mientras se enumeran
            lista_original=linea.split(" ")
            for palabra in lista_original:
                texto_econtrado = ''.join(x for x in palabra if x.isalnum())

                lista1=list()
                for i in linea:                             #Recorre letra por letra la linea
                    lista1.append(i)                        #Agrega cada letra a una lista
                    texto = "".join(lista1)

                    if texto_econtrado == valor_de_busqueda and not VALIDACION: #Encuentra 
                        linea_encontrada = linea ; lista_original.clear()  
                        VALIDACION = True

            conteo=0                                #Iterador para saber cuantas veces ha pasado parentesis (la url esta dentro de parentesis)
            primera_parte=""
            if VALIDACION == True:                  #Si ya encontro la clave
                #Apartado para eliminar la url antigua
                lista_url=list()
                for x in linea_encontrada:
                    if x == '"' and conteo == 0:
                        lista_url.append(x)
                        primera_parte = "".join(lista_url)
                        lista_url.clear()
                        conteo+=1
                    elif x == '"' and conteo == 1:    #Encontrar los parentesis para saber donde esta la ruta y si se encuentran los 2 parentesis se brica al else
                        original = "".join(lista_url)
                        lista_url.clear()           #Eliminas lo que tenia almacenado (la url origininal)
                        lista_url.append(x)
                        conteo+=1                   #Acumula la cantidad de parentesis pasados
                    else:
                        lista_url.append(x)         #Continua agregando el texto sobrante a una lista

                sobrante= "".join(lista_url)             #Se almacena el texto sobrante a una variable

                datafile[fila] = f'{primera_parte}{cambio}{sobrante}' #Se realiza el cambio de línea
                break

        #Reescribe el datafile
        if VALIDACION is True:
            archi = open(archivo, 'w', encoding="utf-8")
            for linea in datafile:  #Reescribe el datafile al txt
                archi.write(linea)

#Configuracion tipo 6 para archivos dividos por apartados (ServBan, TJComm)
    def configuracion6(self, archivo,valor_de_busqueda,etiqueta,cambio):
        with open(archivo) as archivo_temporal:
            datafile = archivo_temporal.readlines()

        #Encuentra el apartado buscado
        validacion_para_transcribir = False
        apartado_encontrado = False
        lista_original = list()
        for fila,linea in enumerate(datafile):                  #Se recorre las lineas del datafile mientras se enumeran
            if apartado_encontrado:                             #Si el apartado fue encontrado, detener busqueda
                break

            for letra in linea:                                 #Recorre letra por letra la linea
                lista_original.append(letra)                #Agrega cada letra a una lista
                texto = "".join(lista_original)         #Une la lista en una variable
                texto1 = texto.strip(" ")

                if valor_de_busqueda in linea:
                    apartado_encontrado = True
                    linea_siguiente = datafile[fila+1]          #Una vez encontrado el apartado, guardamos la fila que esta a continuacion

        #Ecuentra la fila donde se encuentra la url dentro del apartado
        conteo = 0  ; ENCONTRADO = False ; linea_actual = fila
        while ENCONTRADO == False:
            conteo += 1
            if etiqueta not in linea_siguiente:
                linea_actual = fila + conteo
                linea_siguiente = datafile[linea_actual]
            else:
                ENCONTRADO = True
            if conteo == 10:
                print("No fue encontrado la clave")
                return 0

        if apartado_encontrado and etiqueta in linea_siguiente:
            #Divir la clave de la parte a cambiar
            recorrer_linea = list()
            for x in linea_siguiente:
                if x != "=":
                    recorrer_linea.append(x)
                else:
                    recorrer_linea.append(x)
                    break
            parte_1 = "".join(recorrer_linea)

            #Concatena el cambio
            datafile[linea_actual] = f"{parte_1}{cambio}\n"   #Se realiza el cambio de línea
            validacion_para_transcribir = True
            #print(datafile[fila])

        if validacion_para_transcribir is True:
            archi = open(archivo, 'w')
            for linea in datafile:  #Reescribe el datafile al txt
                archi.write(linea)

if __name__ == "__main__":
    objeto = Configuraciones()

    """________________________________________XPOS-AP14________________________________________"""
    #----------------------------ServBan-(configuracion 2)-------------------------------#
    """
    objeto.configuracion2(f"r:/VENTA/SERVBAN.INI","[Bines]","Url","https://qa-corr.femcom.net:5002/invoke/PE6.Pub/runGetQueryV2?")
    objeto.configuracion2(f"r:/VENTA/SERVBAN.INI","[Folio]","Url","https://qa-corr.femcom.net:5002/invoke/PE6.Pub/runGetFolio?")
    objeto.configuracion2(f"r:/VENTA/SERVBAN.INI","[Authorization]","Url","https://qa-corr.femcom.net:5002/invoke/PE6.Pub/runGetAuth?")
    objeto.configuracion2(f"r:/VENTA/SERVBAN.INI","[Acknowledge]","Url","https://qa-corr.femcom.net:5002/invoke/PE6.Pub/runGetAuthAck?")

    objeto.configuracion2(f"C:/VENTA/SERVBAN.INI","[Refund]","Url","https://qa-tdc.femcom.net:8002/invoke/PE2.Pub/runGetDev?")
    objeto.configuracion2(f"C:/VENTA/SERVBAN.INI","[AcknowledgeRefund]","Url","https://qa-tdc.femcom.net:8002/invoke/PE2.Pub/runGetDevAck?")
    objeto.configuracion2(f"C:/VENTA/SERVBAN.INI","[InitializationKeys]","Url","https://qa-tdc.femcom.net:8002/invoke/PE2.Pub/runGetInitialization?")
    
    objeto.configuracion2(f"C:/VENTA/SERVBAN.INI","[Autenticacion]","Url","http://10.184.56.206:3122/invoke/TPE.FAC.Pub/request?")
    objeto.configuracion2(f"C:/VENTA/SERVBAN.INI","[Autenticacion]","UrlValidador","http://10.184.80.20:8911/invoke/TPE.VAL.Pub/request?")
    """
    #-----------------------------TJComm-(configuracion 2)-------------------------------#
    """
    objeto.configuracion2(f"C:/VENTA/TJCOMM.INI","[Bines]","Url","https://qa-corr.femcom.net:5002/invoke/PE6.Pub/runGetQueryV2?")
    objeto.configuracion2(f"C:/VENTA/TJCOMM.INI","[Folio]","Url","https://qa-tdc.femcom.net:8002/invoke/PE2.Pub/runGetFolio?")
    objeto.configuracion2(f"C:/VENTA/TJCOMM.INI","[Authorization]","Url","https://qa-tdc.femcom.net:8002/invoke/PE2.Pub/runGetAuth?")
    objeto.configuracion2(f"C:/VENTA/TJCOMM.INI","[Acknowledge]","Url","https://qa-tdc.femcom.net:8002/invoke/PE2.Pub/runGetAuthAck?")

    objeto.configuracion2(f"C:/VENTA/TJCOMM.INI","[Refund]","Url","https://qa-tdc.femcom.net:8002/invoke/PE2.Pub/runGetDev?")
    objeto.configuracion2(f"C:/VENTA/TJCOMM.INI","[AcknowledgeRefund]","Url","https://qa-tdc.femcom.net:8002/invoke/PE2.Pub/runGetDevAck?")
    objeto.configuracion2(f"C:/VENTA/TJCOMM.INI","[InitializationKeys]","Url","https://qa-tdc.femcom.net:8002/invoke/PE2.Pub/runGetInitialization?")
    
    #------------------------------ED-----------------------------------#
    objeto.configuracion4(f'C:/ED/EDConfig.XML','<Tabulador url=','"https://10.182.92.59:3002/invoke/TPE.TSF.Pub/request?"')
    objeto.configuracion4(f'C:/ED/EDConfig.XML','<Cotizacion url=','"https://10.182.92.59:3002/invoke/TPE.TSF.Pub/request?"')
    objeto.configuracion4(f'C:/ED/EDConfig.XML','<Beneficiarios url=','"https://10.182.92.59:3002/invoke/TPE.TSF.Pub/request?"')
    objeto.configuracion4(f'C:/ED/EDConfig.XML','<Transferencia url=','"https://10.182.92.59:3002/invoke/TPE.TSF.Pub/request?"')
    objeto.configuracion4(f'C:/ED/EDConfig.XML','<Folio url=','"https://10.182.92.59:3002/invoke/TPE.TSF.Pub/request?"')
    objeto.configuracion4(f'C:/ED/EDConfig.XML','<Autorizacion url=','"https://10.182.92.59:3002/invoke/TPE.TSF.Pub/request?"')
    objeto.configuracion4(f'C:/ED/EDConfig.XML','<ACK url=','"https://10.182.92.59:3002/invoke/TPE.TSF.Pub/request?"')

    objeto.configuracion4(f'C:/ED/EDConfig.XML','<RemesaConsulta url=','"https://10.182.92.70:2002/invoke/TPE.TSF.Pub/request?"')
    objeto.configuracion4(f'C:/ED/EDConfig.XML','<RemesaGENIII url=','"https://10.182.92.70:2002/invoke/TPE.TSF.Pub/request?"')
    objeto.configuracion4(f'C:/ED/EDConfig.XML','<RemesaDesbloqueo url=','"https://10.182.92.70:2002/invoke/TPE.TSF.Pub/request?"')
    objeto.configuracion4(f'C:/ED/EDConfig.XML','<RemesaFolio url=','"https://10.182.92.70:2002/invoke/TPE.TSF.Pub/request?"')
    objeto.configuracion4(f'C:/ED/EDConfig.XML','<RemesaAutorizacion url=','"https://10.182.92.70:2002/invoke/TPE.TSF.Pub/request?"')
    objeto.configuracion4(f'C:/ED/EDConfig.XML','<RemesaACK url=','"https://10.182.92.70:2002/invoke/TPE.TSF.Pub/request?"')
    objeto.configuracion4(f'C:/ED/EDConfig.XML','<RemesaReversa url=','"https://10.182.92.70:2002/invoke/TPE.TSF.Pub/request?"')
    objeto.configuracion4(f'C:/ED/EDConfig.XML','<RemesaTransnetwork url=','"https://10.182.92.70:2002/invoke/TPE.TSF.Pub/request?"')
    
    #--------------------------------MVB----------------------------------#
    
    objeto.configuracion1(f"C:/MVB/MVB.INI","url","=https://qa-bus.femcom.net:9001/invoke/TPE.BUS.Pub/")
    objeto.configuracion1(f"C:/MVB/MVB.INI","corrTmOut","=240")

    objeto.configuracion1(f"C:/MVB/CADENAMVB.INI","url","= https://qa-bus.femcom.net:9001/invoke/TPE.BUS.Pub/")
    objeto.configuracion1(f"C:/MVB/CADENAMVB.INI","corrTmOut","= 240")
    
    #--------------------------------TAE----------------------------------#
    
    objeto.configuracion1(f"C:/XPOS/SubSystems/TAE/TAE.ini","URL_Folio","=PArdqYVPFVqD5JKFwop/NUg5JI/j3pItF9pB3zJJ+0ilUTE/AKXybl7mqRmWEsAGWkD1/3G8JoG1FcXAayRzfFPrLp7hVchC7Og3Zuuw")
    objeto.configuracion1(f"C:/XPOS/SubSystems/TAE/TAE.ini","URL_Auth","=jZDaSADDA8Zbpz0zxIkO1kkmtXHh/Ly9otIxIcTfTKzdg75dUqEtb1tu96cAP5CN4UG8lmm8Ls0FXlK7lo6g4wE=")
    objeto.configuracion1(f"C:/XPOS/SubSystems/TAE/TAE.ini","URL_Ack","=ylsyOhqCAJY/d7M2aPS7/gGWMLmaVZSBeIaFS5vfd/t+gE572sbvwBQke0FIyZ/5fpZvO112H2Fw5jgDZIrhjQ==")
    objeto.configuracion2(f"C:/XPOS/SubSystems/TAE/TAE.ini","[TAEStatus]","URL","https://qa-tae.femcom.net:9002/invoke/PE1.Pub/runGetStatus?")
    objeto.configuracion2(f"C:/XPOS/SubSystems/TAE/TAE.ini","[TAELlavero]","URLGET","https://10.182.92.67:9003/invoke/TPE.TAE.Keyring.Pub/runGetKeyring?")
    objeto.configuracion2(f"C:/XPOS/SubSystems/TAE/TAE.ini","[TAELlavero]","URLSET","https://10.182.92.67:9003/invoke/TPE.TAE.Keyring.Pub/runSetKeyring?")
    
    #-------------------------------P-LINEA----------------------------------#
    
    objeto.configuracion6(f"C:/VENTA/P_LINEA.INI","[PREDIAL]","Url","https://qa-mun.femcom.net:3001/invoke/TPE.MUN.Pub/request?")
    objeto.configuracion6(f"C:/VENTA/P_LINEA.INI","[MULTAS]","Url","https://qa-mun.femcom.net:3001/invoke/TPE.MUN.Pub/request?")
    objeto.configuracion6(f"C:/VENTA/P_LINEA.INI","[SERVICIOS]","Url","cVBla4zZn/EQD7Yg5YevTxElCfoej3esU9vERMVgglJlq6lgO/OtxxRvGz+vOUoeKzoVwIfBkK9SQ1p6GpDT6pqg")
    objeto.configuracion6(f"C:/VENTA/P_LINEA.INI","[BOLETOS]","Url","https://qa-cine.femcom.net:8001/invoke/TPE.CINES.Pub/request?")
    
    #-------------------------------VBCINE----------------------------------#
    objeto.configuracion1(f"C:/VENTA/PLN/VBCINE.XML","<URL>","https://qa-cine.femcom.net:8001/invoke/TPE.CINES.Pub/request?</URL>")

    #-------------------------------ME----------------------------------#
    
    objeto.configuracion4(f'C:/ME/MECONFIG.XML','<Folio url=','"https://qa-fcp.femcom.net:5001/invoke/TPE.FCP.Pub/request?"')
    objeto.configuracion4(f'C:/ME/MECONFIG.XML','<Autorizacion url=','"https://qa-fcp.femcom.net:5001/invoke/TPE.FCP.Pub/request?"')
    objeto.configuracion4(f'C:/ME/MECONFIG.XML','<ACK url=','"https://qa-fcp.femcom.net:5001/invoke/TPE.FCP.Pub/request?"')
    objeto.configuracion4(f'C:/ME/MECONFIG.XML','<Homonimia url=','"https://qa-fcp.femcom.net:5001/invoke/TPE.FCP.Pub/request?"')
    
    #-------------------------------GC----------------------------------#
    #Configuracion del archivo GcAConfig.ini#
    objeto.configuracion6(f'C:/GC/GcAConfig.INI','[TAEFolio]','URL','https://qa-gift.femcom.net:7002/invoke/PE3.Pub/runGetFolio?')
    objeto.configuracion6(f'C:/GC/GcAConfig.INI','[TAEAuth]','URL','https://qa-gift.femcom.net:7002/invoke/PE3.Pub/runGetActivation?')
    objeto.configuracion6(f'C:/GC/GcAConfig.INI','[TAEAck]','URL','https://qa-gift.femcom.net:7002/invoke/PE3.Pub/runGetAck?')
    objeto.configuracion6(f'C:/GC/GcAConfig.INI','[TAELlavero]','URLGET','https://qa-gift.femcom.net:7002/invoke/TPE.TAE.Keyring.Pub/runGetKeyring?')
    objeto.configuracion6(f'C:/GC/GcAConfig.INI','[TAELlavero]','URLSET','https://qa-gift.femcom.net:7002/invoke/TPE.TAE.Keyring.Pub/runSetKeyring?')
    objeto.configuracion6(f'C:/GC/GcAConfig.INI','[TAEEstatus]','URL','https://qa-gift.femcom.net:7002/invoke/PE3.Pub/runGetStatus?')
    
    # Configuracion del archivo GCConfig.ini #
    objeto.configuracion6(f'C:/GC/GCConfig.INI','[TAEFolio]','URL','https://qa-gift.femcom.net:7002/invoke/PE3.Pub/runGetFolio?')
    objeto.configuracion6(f'C:/GC/GCConfig.INI','[TAEAuth]','URL','https://qa-gift.femcom.net:7002/invoke/PE3.Pub/runGetActivation?')
    objeto.configuracion6(f'C:/GC/GCConfig.INI','[TAEAck]','URL','https://qa-gift.femcom.net:7002/invoke/PE3.Pub/runGetAck?')
    objeto.configuracion6(f'C:/GC/GCConfig.INI','[TAEEstatus]','URL','https://qa-gift.femcom.net:7002/invoke/PE3.Pub/runGetStatus?')
    
    #------------------------CONFIGURACIONES NO UTILIZADAS----------------------------------#
    #objeto.configuracion5(f'C:/ME/MECONFIG.XML','Homonimia','https://qa-fcp.femcom.net:5001/invoke/TPE.FCP.Pub/request?')
    #objeto.configuracion3(f'C:/ED/EDConfig.XML','<Tabulador url="','https://10.182.92.59:3002/invoke/TPE.TSF.Pub/request?"')
    """