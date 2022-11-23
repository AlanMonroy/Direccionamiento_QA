from pymongo import MongoClient
import bson.json_util as json_util

class MongoDB:
	def __init__(self, usuario, contraseña):
		#Establece conexion
		client = MongoClient(f"mongodb+srv://{usuario}:{contraseña}@cluster0.ta9pi.mongodb.net/test?retryWrites=true&w=majority")
		#client = MongoClient(f"mongodb+srv://{usuario}:{contraseña}@cluster0.ta9pi.mongodb.net/?retryWrites=true&w=majority&connectTimeoutMS=1200000")
		self.db = client.get_database("Configuracion_ambiente")		#Guarda la db
		try:
		    x=client.server_info()
		except Exception as e:
			return (f"No se pudo establecer conexión con la base de datos") 

	def registrar(self, collection, categoria, clave, sub_clave=0, url_ap14=0,url_qa10=0,url_qa8=0):
		collection = self.db[collection] #Guarda el collection
		#print(collection)

		nuevo_dato = {"CATEGORIA": categoria,"CLAVE": clave,"SUB_CLAVE": sub_clave,"URL_AP14":url_ap14,"URL_QA10":url_qa10,"URL_QA8":url_qa8}

		collection.insert_one(nuevo_dato)
		return f"Registro completado"

	def get_url(self,collection,categoria,clave,sub_clave):
		collection = self.db[collection]

		valor = collection.find_one({"CATEGORIA":categoria,"CLAVE":clave,"SUB_CLAVE":sub_clave})
		url_obtenida = valor["URL"]
		return url_obtenida

	def get_all_url(self,collection,categoria):
		collection = self.db[collection]

		diccionario = collection.find({"CATEGORIA":categoria})
		return diccionario

	def actualizar(self, collection, categoria, clave, sub_clave=0, filtro=0,url=0):
		collection = self.db[collection]
		collection.update_one({"CATEGORIA":categoria,"CLAVE":clave,"SUB_CLAVE":sub_clave},{"$set":{filtro:url}})

	def vaciar_collection(self,collection):
		collection = self.db[collection]
		collection.delete_many({})

		return f"Colección vaciada"

	def descargar_DB(self):
		collection = self.db['DIRECCIONAMIENTO']
		database = collection.find()

		with open("data.json", "w") as outfile:
		    outfile.write(json_util.dumps(database, indent=7))

	def get_db(self):
		collection = self.db['DIRECCIONAMIENTO']
		database = collection.find()
		return database

if __name__ == "__main__":
	objeto = MongoDB("admin","701562")
	#objeto.descargar_DB()

	# ELIMINAR TODOS LOS REGISTROS DE UNA COLECCION #
	#objeto.vaciar_collection("DIRECCIONAMIENTO")

	# ACTUALIZAR #
	#objeto.actualizar("DIRECCIONAMIENTO","C:/VENTA/SERVBAN.INI","[Autenticacion]","Url","URL_QA8","http://10.185.179.37:3122/invoke/TPE.FAC.Pub/request?")
	#objeto.actualizar("DIRECCIONAMIENTO","C:/VENTA/SERVBAN.INI","[Autenticacion]","Url","URL_AP14","http://10.185.179.37:3122/invoke/TPE.FAC.Pub/request?") #2022-23-09

	# REALIZAR REGISTROS #

	#AP14 - TOTAL REGISTRO = 56
	#SERVBAN - 9
	"""
	objeto.registrar(collection="DIRECCIONAMIENTO",categoria="VENTA/SERVBAN.INI",clave="[Bines]",sub_clave="Url",
		url_ap14="https://qa-corr.femcom.net:5002/invoke/PE6.Pub/runGetQueryV2?",
		url_qa10="http://10.184.80.20:8904/invoke/PE6.Pub/runGetQueryV2?",
		url_qa8="http://10.184.40.110:8904/invoke/PE6.Pub/runGetQueryV2?")
	objeto.registrar(collection="DIRECCIONAMIENTO",categoria="VENTA/SERVBAN.INI",clave="[Folio]",sub_clave="Url",
		url_ap14="https://qa-corr.femcom.net:5002/invoke/PE6.Pub/runGetFolio?",
		url_qa10="http://10.184.80.20:8904/invoke/PE6.Pub/runGetFolio?",
		url_qa8="http://10.184.40.110:8904/invoke/PE6.Pub/runGetFolio?")
	objeto.registrar(collection="DIRECCIONAMIENTO",categoria="VENTA/SERVBAN.INI",clave="[Authorization]",sub_clave="Url",
		url_ap14="https://qa-corr.femcom.net:5002/invoke/PE6.Pub/runGetAuth?",
		url_qa10="http://10.184.80.20:8904/invoke/PE6.Pub/runGetAuth?",
		url_qa8="http://10.184.40.110:8904/invoke/PE6.Pub/runGetAuth?")
	objeto.registrar(collection="DIRECCIONAMIENTO",categoria="VENTA/SERVBAN.INI",clave="[Acknowledge]",sub_clave="Url",
		url_ap14="https://qa-corr.femcom.net:5002/invoke/PE6.Pub/runGetAuthAck?",
		url_qa10="http://10.184.80.20:8904/invoke/PE6.Pub/runGetAuthAck?",
		url_qa8="http://10.184.40.110:8904/invoke/PE6.Pub/runGetAuthAck?")

	objeto.registrar(collection="DIRECCIONAMIENTO",categoria="VENTA/SERVBAN.INI",clave="[Refund]",sub_clave="Url",
		url_ap14="https://qa-tdc.femcom.net:8002/invoke/PE2.Pub/runGetDev?",
		url_qa10="http://10.184.80.20:8890/invoke/PE2.Pub/runGetDev?",
		url_qa8="http://10.184.40.110:8890/invoke/PE2.Pub/runGetDev?")
	objeto.registrar(collection="DIRECCIONAMIENTO",categoria="VENTA/SERVBAN.INI",clave="[AcknowledgeRefund]",sub_clave="Url",
		url_ap14="https://qa-tdc.femcom.net:8002/invoke/PE2.Pub/runGetDevAck?",
		url_qa10="http://10.184.80.20:8890/invoke/PE2.Pub/runGetDevAck?",
		url_qa8="http://10.184.40.110:8890/invoke/PE2.Pub/runGetDevAck?")
	objeto.registrar(collection="DIRECCIONAMIENTO",categoria="VENTA/SERVBAN.INI",clave="[InitializationKeys]",sub_clave="Url",
		url_ap14="https://qa-tdc.femcom.net:8002/invoke/PE2.Pub/runGetInitialization?",
		url_qa10="http://10.184.80.20:8890/invoke/PE2.Pub/runGetInitialization?",
		url_qa8="http://10.184.40.110:8890/invoke/PE2.Pub/runGetInitialization?")

	objeto.registrar(collection="DIRECCIONAMIENTO",categoria="VENTA/SERVBAN.INI",clave="[Autenticacion]",sub_clave="Url",
		url_ap14="http://10.185.179.37:3122/invoke/TPE.FAC.Pub/request?",
		url_qa10="http://10.185.179.37:3122/invoke/TPE.FAC.Pub/request?",
		url_qa8="http://10.185.179.37:3122/invoke/TPE.FAC.Pub/request?")
	objeto.registrar(collection="DIRECCIONAMIENTO",categoria="VENTA/SERVBAN.INI",clave="[Autenticacion]",sub_clave="UrlValidador",
		url_ap14="http://10.184.80.20:8911/invoke/TPE.VAL.Pub/request?",
		url_qa10="http://10.184.80.20:8911/invoke/TPE.VAL.Pub/request?",
		url_qa8='http://10.184.80.20:8911/invoke/TPE.VAL.Pub/request?')
	
	#TAE - 6
	objeto.registrar(collection="DIRECCIONAMIENTO",categoria="XPOS/SubSystems/TAE/TAE.ini",clave="[TAEComm]",sub_clave="URL_Folio",
		url_ap14='PArdqYVPFVqD5JKFwop/NUg5JI/j3pItF9pB3zJJ+0ilUTE/AKXybl7mqRmWEsAGWkD1/3G8JoG1FcXAayRzfFPrLp7hVchC7Og3Zuuw',
		url_qa10='w2S/JVn9npGggrJi1a6v2Xw0YAjoFEg5fyvQqnsQACdWIy2WZPL8EG5N8FCnCn5pwZ5IuSJ0Fb4eOkjlbF0KxVbQIAOgAgG9',
		url_qa8='ilbBxdbvGZfmVDP4L67Xy37jbJ3+1PXiDaKoDi3kuw3EDVsq6xs/jn/5YQjryqFY6ykQLFpKbNNMDbWERb928BX8GzxYkB8piQ==')
	objeto.registrar(collection="DIRECCIONAMIENTO",categoria="XPOS/SubSystems/TAE/TAE.ini",clave="[TAEComm]",sub_clave="URL_Auth",
		url_ap14="jZDaSADDA8Zbpz0zxIkO1kkmtXHh/Ly9otIxIcTfTKzdg75dUqEtb1tu96cAP5CN4UG8lmm8Ls0FXlK7lo6g4wE=",
		url_qa10='SHMgH/weG13sEAROjS4Wa3qjMBXDr2xPk8oPDZ/ayemdgSjMWv38uj9NL3kbljCClrtqE1IMBvWi2R0=',
		url_qa8='yIQe0vRNsFKf+vr9kbyC3izHOO1CWf1pG+XrPoU0aN7zxaZVQYcQI9/Hj0HVFRIkc3a0h5j8JEeLEt9N')
	objeto.registrar(collection="DIRECCIONAMIENTO",categoria="XPOS/SubSystems/TAE/TAE.ini",clave="[TAEComm]",sub_clave="URL_Ack",
		url_ap14="ylsyOhqCAJY/d7M2aPS7/gGWMLmaVZSBeIaFS5vfd/t+gE572sbvwBQke0FIyZ/5fpZvO112H2Fw5jgDZIrhjQ==",
		url_qa10='qfvMCocpfFS52qiqI/YXVP4MJtHp5jGQBTMiX7WhM2eWdLJ6CO3HjDNQe4+QW/82PBLZL5mss4n4Mw==',
		url_qa8='KY+ku5x6vdYlbkVy5J7UOXeL3do5CfcY5DmC95Giik7xTjN2AwsaRn+kgGoq/+hHA/leljVxL+BQ4Xo=')
	objeto.registrar(collection="DIRECCIONAMIENTO",categoria="XPOS/SubSystems/TAE/TAE.ini",clave="[TAEStatus]",sub_clave="URL",
		url_ap14="https://qa-tae.femcom.net:9002/invoke/PE1.Pub/runGetStatus?",
		url_qa10='http://10.184.80.20:8888/invoke/PE1.Pub/runGetStatus?',
		url_qa8='http://10.184.40.110:8888/invoke/PE1.Pub/runGetStatus?')
	objeto.registrar(collection="DIRECCIONAMIENTO",categoria="XPOS/SubSystems/TAE/TAE.ini",clave="[TAELlavero]",sub_clave="URLGET",
		url_ap14="https://10.182.92.67:9003/invoke/TPE.TAE.Keyring.Pub/runGetKeyring?",
		url_qa10='http://10.184.80.20:8895/invoke/TPE.TAE.Keyring.Pub/runGetKeyring?',
		url_qa8='http://10.184.40.110:8895/invoke/TPE.TAE.Keyring.Pub/runGetKeyring?')
	objeto.registrar(collection="DIRECCIONAMIENTO",categoria="XPOS/SubSystems/TAE/TAE.ini",clave="[TAELlavero]",sub_clave="URLSET",
		url_ap14="https://10.182.92.67:9003/invoke/TPE.TAE.Keyring.Pub/runSetKeyring?",
		url_qa10='http://10.184.80.20:8895/invoke/TPE.TAE.Keyring.Pub/runSetKeyring?',
		url_qa8='http://10.184.40.110:8895/invoke/TPE.TAE.Keyring.Pub/runSetKeyring?')
	
	#TJCOMM - 7
	objeto.registrar(collection="DIRECCIONAMIENTO",categoria="VENTA/TJCOMM.INI",clave="[Bines]",sub_clave="Url",
		url_ap14="https://qa-corr.femcom.net:5002/invoke/PE6.Pub/runGetQueryV2?",
		url_qa10='http://10.184.80.20:8904/invoke/PE6.Pub/runGetQueryV2?',
		url_qa8='http://10.184.40.110:8904/invoke/PE6.Pub/runGetQueryV2?')
	objeto.registrar(collection="DIRECCIONAMIENTO",categoria="VENTA/TJCOMM.INI",clave="[Folio]",sub_clave="Url",
		url_ap14="https://qa-tdc.femcom.net:8002/invoke/PE2.Pub/runGetFolio?",
		url_qa10='http://10.184.80.20:8890/invoke/PE2.Pub/runGetFolio?',
		url_qa8='http://10.184.40.110:8890/invoke/PE2.Pub/runGetFolio?')
	objeto.registrar(collection="DIRECCIONAMIENTO",categoria="VENTA/TJCOMM.INI",clave="[Authorization]",sub_clave="Url",
		url_ap14="https://qa-tdc.femcom.net:8002/invoke/PE2.Pub/runGetAuth?",
		url_qa10='http://10.184.80.20:8890/invoke/PE2.Pub/runGetAuth?',
		url_qa8='http://10.184.40.110:8890/invoke/PE2.Pub/runGetAuth?')
	objeto.registrar(collection="DIRECCIONAMIENTO",categoria="VENTA/TJCOMM.INI",clave="[Acknowledge]",sub_clave="Url",
		url_ap14="https://qa-tdc.femcom.net:8002/invoke/PE2.Pub/runGetAuthAck?",
		url_qa10='http://10.184.80.20:8890/invoke/PE2.Pub/runGetAuthAck?',
		url_qa8='http://10.184.40.110:8890/invoke/PE2.Pub/runGetAuthAck?')

	objeto.registrar(collection="DIRECCIONAMIENTO",categoria="VENTA/TJCOMM.INI",clave="[Refund]",sub_clave="Url",
		url_ap14="https://qa-tdc.femcom.net:8002/invoke/PE2.Pub/runGetDev?",
		url_qa10='http://10.184.80.20:8890/invoke/PE2.Pub/runGetDev?',
		url_qa8='http://10.184.40.110:8890/invoke/PE2.Pub/runGetDev?')
	objeto.registrar(collection="DIRECCIONAMIENTO",categoria="VENTA/TJCOMM.INI",clave="[AcknowledgeRefund]",sub_clave="Url",
		url_ap14="https://qa-tdc.femcom.net:8002/invoke/PE2.Pub/runGetDevAck?",
		url_qa10='http://10.184.80.20:8890/invoke/PE2.Pub/runGetDevAck?',
		url_qa8='http://10.184.40.110:8890/invoke/PE2.Pub/runGetDevAck?')
	objeto.registrar(collection="DIRECCIONAMIENTO",categoria="VENTA/TJCOMM.INI",clave="[InitializationKeys]",sub_clave="Url",
		url_ap14="https://qa-tdc.femcom.net:8002/invoke/PE2.Pub/runGetInitialization?",
		url_qa10='http://10.184.80.20:8890/invoke/PE2.Pub/runGetInitialization?',
		url_qa8='http://10.184.40.110:8890/invoke/PE2.Pub/runGetInitialization?')

	#P_LINEA - 4
	objeto.registrar(collection="DIRECCIONAMIENTO",categoria="VENTA/P_LINEA.INI",clave="[PREDIAL]",sub_clave="Url",
		url_ap14="https://qa-mun.femcom.net:3001/invoke/TPE.MUN.Pub/request?",
		url_qa10='http://10.184.80.20:8897/invoke/TPE.MUN.Pub/request?',
		url_qa8='http://10.184.40.110:8897/invoke/TPE.MUN.Pub/request?')
	objeto.registrar(collection="DIRECCIONAMIENTO",categoria="VENTA/P_LINEA.INI",clave="[MULTAS]",sub_clave="Url",
		url_ap14="https://qa-mun.femcom.net:3001/invoke/TPE.MUN.Pub/request?",
		url_qa10='http://10.184.80.20:8897/invoke/TPE.MUN.Pub/request?',
		url_qa8='http://10.184.40.110:8897/invoke/TPE.MUN.Pub/request?')
	objeto.registrar(collection="DIRECCIONAMIENTO",categoria="VENTA/P_LINEA.INI",clave="[SERVICIOS]",sub_clave="Url",
		url_ap14="cVBla4zZn/EQD7Yg5YevTxElCfoej3esU9vERMVgglJlq6lgO/OtxxRvGz+vOUoeKzoVwIfBkK9SQ1p6GpDT6pqg",
		url_qa10='iekLY0i6FpdO3CkeRGtTbcNUZMbqLTrBFyziec+lIdKmFyT5DuGU2QIDBzKcU/mxv/WhOgnHbUPvVEf1',
		url_qa8='tm0v9iE7CFwegvKYSlzPNOPgkF1aoi4crzTaFG9TcUX4GRF12IhoJd5D5djBPz9c2S1LFsaq92q6aiBX1w==')
	objeto.registrar(collection="DIRECCIONAMIENTO",categoria="VENTA/P_LINEA.INI",clave="[BOLETOS]",sub_clave="Url",
		url_ap14="https://qa-cine.femcom.net:8001/invoke/TPE.CINES.Pub/request?",
		url_qa10='http://10.184.80.20:8914/invoke/TPE.CINES.Pub/request?',
		url_qa8='http://10.184.40.110:8914/invoke/TPE.CINES.Pub/request?')

	#ED - 15
	objeto.registrar(collection="DIRECCIONAMIENTO",categoria='ED/EDConfig.XML',clave='<Tabulador url=',
		url_ap14='"https://10.182.92.59:3002/invoke/TPE.TSF.Pub/request?"',
		url_qa10='"http://10.184.80.20:8907/invoke/TPE.TSF.Pub/request?"',
		url_qa8='"http://10.184.40.110:8907/invoke/TPE.TSF.Pub/request?"')
	objeto.registrar(collection="DIRECCIONAMIENTO",categoria='ED/EDConfig.XML',clave='<Cotizacion url=',
		url_ap14='"https://10.182.92.59:3002/invoke/TPE.TSF.Pub/request?"',
		url_qa10='"http://10.184.80.20:8907/invoke/TPE.TSF.Pub/request?"',
		url_qa8='"http://10.184.40.110:8907/invoke/TPE.TSF.Pub/request?"')
	objeto.registrar(collection="DIRECCIONAMIENTO",categoria='ED/EDConfig.XML',clave='<Beneficiarios url=',
		url_ap14='"https://10.182.92.59:3002/invoke/TPE.TSF.Pub/request?"',
		url_qa10='"http://10.184.80.20:8907/invoke/TPE.TSF.Pub/request?"',
		url_qa8='"http://10.184.40.110:8907/invoke/TPE.TSF.Pub/request?"')
	objeto.registrar(collection="DIRECCIONAMIENTO",categoria='ED/EDConfig.XML',clave='<Transferencia url=',
		url_ap14='"https://10.182.92.59:3002/invoke/TPE.TSF.Pub/request?"',
		url_qa10='"http://10.184.80.20:8907/invoke/TPE.TSF.Pub/request?"',
		url_qa8='"http://10.184.40.110:8907/invoke/TPE.TSF.Pub/request?"')
	objeto.registrar(collection="DIRECCIONAMIENTO",categoria='ED/EDConfig.XML',clave='<Folio url=',
		url_ap14='"https://10.182.92.59:3002/invoke/TPE.TSF.Pub/request?"',
		url_qa10='"http://10.184.80.20:8907/invoke/TPE.TSF.Pub/request?"',
		url_qa8='"http://10.184.40.110:8907/invoke/TPE.TSF.Pub/request?"')
	objeto.registrar(collection="DIRECCIONAMIENTO",categoria='ED/EDConfig.XML',clave='<Autorizacion url=',
		url_ap14='"https://10.182.92.59:3002/invoke/TPE.TSF.Pub/request?"',
		url_qa10='"http://10.184.80.20:8907/invoke/TPE.TSF.Pub/request?"',
		url_qa8='"http://10.184.40.110:8907/invoke/TPE.TSF.Pub/request?"')
	objeto.registrar(collection="DIRECCIONAMIENTO",categoria='ED/EDConfig.XML',clave='<ACK url=',
		url_ap14='"https://10.182.92.59:3002/invoke/TPE.TSF.Pub/request?"',
		url_qa10='"http://10.184.80.20:8907/invoke/TPE.TSF.Pub/request?"',
		url_qa8='"http://10.184.40.110:8907/invoke/TPE.TSF.Pub/request?"')

	objeto.registrar(collection="DIRECCIONAMIENTO",categoria='ED/EDConfig.XML',clave='<RemesaConsulta url=',
		url_ap14='"https://10.182.92.70:2002/invoke/TPE.TSF.Pub/request?"',
		url_qa10='"http://10.184.80.20:8917/invoke/TPE.TSF.Pub/request?"',
		url_qa8='"http://10.184.40.110:8917/invoke/TPE.TSF.Pub/request?"')
	objeto.registrar(collection="DIRECCIONAMIENTO",categoria='ED/EDConfig.XML',clave='<RemesaGENIII url=',
		url_ap14='"https://10.182.92.70:2002/invoke/TPE.TSF.Pub/request?"',
		url_qa10='"http://10.184.80.20:8917/invoke/TPE.TSF.Pub/request?"',
		url_qa8='"http://10.184.40.110:8917/invoke/TPE.TSF.Pub/request?"')
	objeto.registrar(collection="DIRECCIONAMIENTO",categoria='ED/EDConfig.XML',clave='<RemesaDesbloqueo url=',
		url_ap14='"https://10.182.92.70:2002/invoke/TPE.TSF.Pub/request?"',
		url_qa10='"http://10.184.80.20:8917/invoke/TPE.TSF.Pub/request?"',
		url_qa8='"http://10.184.40.110:8917/invoke/TPE.TSF.Pub/request?"')
	objeto.registrar(collection="DIRECCIONAMIENTO",categoria='ED/EDConfig.XML',clave='<RemesaFolio url=',
		url_ap14='"https://10.182.92.70:2002/invoke/TPE.TSF.Pub/request?"',
		url_qa10='"http://10.184.80.20:8917/invoke/TPE.TSF.Pub/request?"',
		url_qa8='"http://10.184.40.110:8917/invoke/TPE.TSF.Pub/request?"')
	objeto.registrar(collection="DIRECCIONAMIENTO",categoria='ED/EDConfig.XML',clave='<RemesaAutorizacion url=',
		url_ap14='"https://10.182.92.70:2002/invoke/TPE.TSF.Pub/request?"',
		url_qa10='"http://10.184.80.20:8917/invoke/TPE.TSF.Pub/request?"',
		url_qa8='"http://10.184.40.110:8917/invoke/TPE.TSF.Pub/request?"')
	objeto.registrar(collection="DIRECCIONAMIENTO",categoria='ED/EDConfig.XML',clave='<RemesaACK url=',
		url_ap14='"https://10.182.92.70:2002/invoke/TPE.TSF.Pub/request?"',
		url_qa10='"http://10.184.80.20:8917/invoke/TPE.TSF.Pub/request?"',
		url_qa8='"http://10.184.40.110:8917/invoke/TPE.TSF.Pub/request?"')
	objeto.registrar(collection="DIRECCIONAMIENTO",categoria='ED/EDConfig.XML',clave='<RemesaReversa url=',
		url_ap14='"https://10.182.92.70:2002/invoke/TPE.TSF.Pub/request?"',
		url_qa10='"http://10.184.80.20:8917/invoke/TPE.TSF.Pub/request?"',
		url_qa8='"http://10.184.40.110:8917/invoke/TPE.TSF.Pub/request?"')
	objeto.registrar(collection="DIRECCIONAMIENTO",categoria='ED/EDConfig.XML',clave='<RemesaTransnetwork url=',
		url_ap14='"https://10.182.92.70:2002/invoke/TPE.TSF.Pub/request?"',
		url_qa10='"http://10.184.80.20:8917/invoke/TPE.TSF.Pub/request?"',
		url_qa8='"http://10.184.40.110:8917/invoke/TPE.TSF.Pub/request?"')

	#VBCINE - 1 
	objeto.registrar(collection="DIRECCIONAMIENTO",categoria="VENTA/PLN/VBCINE.XML",clave="<URL>",
		url_ap14="https://qa-cine.femcom.net:8001/invoke/TPE.CINES.Pub/request?</URL>",
		url_qa10='http://10.184.80.20:8914/invoke/TPE.CINES.Pub/request?</URL>',
		url_qa8='http://10.184.40.110:8914/invoke/TPE.CINES.Pub/request?</URL>')

	#MVB - 4
	objeto.registrar(collection="DIRECCIONAMIENTO",categoria="MVB/MVB.INI",clave="url",
		url_ap14="=https://qa-bus.femcom.net:9001/invoke/TPE.BUS.Pub/",
		url_qa10='=http://10.184.80.20:8891/invoke/TPE.BUS.Pub/',
		url_qa8='=http://10.184.40.110:8891/invoke/TPE.BUS.Pub/')
	objeto.registrar(collection="DIRECCIONAMIENTO",categoria="MVB/MVB.INI",clave="corrTmOut",
		url_ap14="=240",
		url_qa10='=240',
		url_qa8='=240')

	objeto.registrar(collection="DIRECCIONAMIENTO",categoria="MVB/CADENAMVB.INI",clave="url",
		url_ap14="= https://qa-bus.femcom.net:9001/invoke/TPE.BUS.Pub/",
		url_qa10='= http://10.184.80.20:8891/invoke/TPE.BUS.Pub/',
		url_qa8='= http://10.184.40.110:8891/invoke/TPE.BUS.Pub/')
	objeto.registrar(collection="DIRECCIONAMIENTO",categoria="MVB/CADENAMVB.INI",clave="corrTmOut",
		url_ap14="= 240",
		url_qa10='= 240',
		url_qa8='= 240')

	#GC - 10 # Configuracion del archivo GcAonfig.ini #
	objeto.registrar(collection="DIRECCIONAMIENTO",categoria='GC/GcAConfig.INI',clave='[TAEFolio]',sub_clave='URL',
		url_ap14='https://qa-gift.femcom.net:7002/invoke/PE3.Pub/runGetFolio?',
		url_qa10='http://10.184.80.20:8896/invoke/PE3.Pub/runGetFolio?',
		url_qa8='http://10.184.40.110:8896/invoke/PE3.Pub/runGetFolio?')
	objeto.registrar(collection="DIRECCIONAMIENTO",categoria='GC/GcAConfig.INI',clave='[TAEAuth]',sub_clave='URL',
		url_ap14='https://qa-gift.femcom.net:7002/invoke/PE3.Pub/runGetActivation?',
		url_qa10='http://10.184.80.20:8896/invoke/PE3.Pub/runGetActivation?',
		url_qa8='http://10.184.40.110:8896/invoke/PE3.Pub/runGetActivation?')
	objeto.registrar(collection="DIRECCIONAMIENTO",categoria='GC/GcAConfig.INI',clave='[TAEAck]',sub_clave='URL',
		url_ap14='https://qa-gift.femcom.net:7002/invoke/PE3.Pub/runGetAck?',
		url_qa10='http://10.184.80.20:8896/invoke/PE3.Pub/runGetAck?',
		url_qa8='http://10.184.40.110:8896/invoke/PE3.Pub/runGetAck?')
	objeto.registrar(collection="DIRECCIONAMIENTO",categoria='GC/GcAConfig.INI',clave='[TAELlavero]',sub_clave='URLGET',
		url_ap14='https://qa-gift.femcom.net:7002/invoke/TPE.TAE.Keyring.Pub/runGetKeyring?',
		url_qa10='http://10.184.80.20:8896/invoke/TPE.TAE.Keyring.Pub/runGetKeyring?',
		url_qa8='http://10.184.40.110:8896/invoke/TPE.TAE.Keyring.Pub/runGetKeyring?')
	objeto.registrar(collection="DIRECCIONAMIENTO",categoria='GC/GcAConfig.INI',clave='[TAELlavero]',sub_clave='URLSET',
		url_ap14='https://qa-gift.femcom.net:7002/invoke/TPE.TAE.Keyring.Pub/runSetKeyring?',
		url_qa10='http://10.184.80.20:8896/invoke/TPE.TAE.Keyring.Pub/runSetKeyring?',
		url_qa8='http://10.184.40.110:8896/invoke/TPE.TAE.Keyring.Pub/runSetKeyring?')
	objeto.registrar(collection="DIRECCIONAMIENTO",categoria='GC/GcAConfig.INI',clave='[TAEEstatus]',sub_clave='URL',
		url_ap14='https://qa-gift.femcom.net:7002/invoke/PE3.Pub/runGetStatus?',
		url_qa10='http://10.184.80.20:8896/invoke/PE3.Pub/runGetStatus?',
		url_qa8='http://10.184.40.110:8896/invoke/PE3.Pub/runGetStatus?')

	# Configuracion del archivo GCConfig.ini #
	objeto.registrar(collection="DIRECCIONAMIENTO",categoria='GC/GCConfig.INI',clave='[TAEFolio]',sub_clave='URL',
		url_ap14='https://qa-gift.femcom.net:7002/invoke/PE3.Pub/runGetFolio?',
		url_qa10='http://10.184.80.20:8896/invoke/PE3.Pub/runGetFolio?',
		url_qa8='http://10.184.40.110:8896/invoke/PE3.Pub/runGetFolio?')
	objeto.registrar(collection="DIRECCIONAMIENTO",categoria='GC/GCConfig.INI',clave='[TAEAuth]',sub_clave='URL',
		url_ap14='https://qa-gift.femcom.net:7002/invoke/PE3.Pub/runGetActivation?',
		url_qa10='http://10.184.80.20:8896/invoke/PE3.Pub/runGetActivation?',
		url_qa8='http://10.184.40.110:8896/invoke/PE3.Pub/runGetActivation?')
	objeto.registrar(collection="DIRECCIONAMIENTO",categoria='GC/GCConfig.INI',clave='[TAEAck]',sub_clave='URL',
		url_ap14='https://qa-gift.femcom.net:7002/invoke/PE3.Pub/runGetAck?',
		url_qa10='http://10.184.80.20:8896/invoke/PE3.Pub/runGetAck?',
		url_qa8='http://10.184.40.110:8896/invoke/PE3.Pub/runGetAck?')
	objeto.registrar(collection="DIRECCIONAMIENTO",categoria='GC/GCConfig.INI',clave='[TAEEstatus]',sub_clave='URL',
		url_ap14='https://qa-gift.femcom.net:7002/invoke/PE3.Pub/runGetStatus?',
		url_qa10='http://10.184.80.20:8896/invoke/PE3.Pub/runGetStatus?',
		url_qa8='http://10.184.40.110:8896/invoke/PE3.Pub/runGetStatus?')
	"""