from algoritmos_configuracion import Configuraciones
from Conexion_MongoDB import MongoDB
import json

class Manage:
	def direccionamiento_online(self,ambiente,lista,ruta):
		configuraciones_nivel_1 = ['VENTA/PLN/VBCINE.XML','MVB/MVB.INI','MVB/CADENAMVB.INI']
		configuraciones_nivel_2 = ['VENTA/SERVBAN.INI','XPOS/SubSystems/TAE/TAE.ini','VENTA/TJCOMM.INI']
		configuraciones_nivel_4 = ['ED/EDConfig.XML']
		configuraciones_nivel_6 = ['VENTA/P_LINEA.INI','GC/GcAConfig.INI','GC/GCConfig.INI']

		mongo=MongoDB('admin','701562') ; data = mongo.get_db()
		llamar_configuracion = Configuraciones()
		for i in data:
			if i['CATEGORIA'] in lista:
				if ambiente == 'AP14':
					if i['CATEGORIA'] in configuraciones_nivel_1:
						llamar_configuracion.configuracion1(ruta + i['CATEGORIA'], i['CLAVE'],i['URL_AP14'])
						#print(ruta + i['CATEGORIA'], i['CLAVE'],i['URL_AP14'])
					elif i['CATEGORIA'] in configuraciones_nivel_2:
						llamar_configuracion.configuracion2(ruta + i['CATEGORIA'], i['CLAVE'],i['SUB_CLAVE'],i['URL_AP14'])
						#print(ruta + i['CATEGORIA'], i['CLAVE'],i['SUB_CLAVE'],i['URL_AP14'])
					elif i['CATEGORIA'] in configuraciones_nivel_4:
						llamar_configuracion.configuracion4(ruta + i['CATEGORIA'], i['CLAVE'],i['URL_AP14'])
						#print(ruta + i['CATEGORIA'], i['CLAVE'],i['URL_AP14'])
					elif i['CATEGORIA'] in configuraciones_nivel_6:
						llamar_configuracion.configuracion6(ruta + i['CATEGORIA'], i['CLAVE'],i['SUB_CLAVE'],i['URL_AP14'])
				elif ambiente == 'QA10':
					if i['CATEGORIA'] in configuraciones_nivel_1:
						llamar_configuracion.configuracion1(ruta + i['CATEGORIA'], i['CLAVE'],i['URL_QA10'])
					elif i['CATEGORIA'] in configuraciones_nivel_2:
						llamar_configuracion.configuracion2(ruta + i['CATEGORIA'], i['CLAVE'],i['SUB_CLAVE'],i['URL_QA10'])
					elif i['CATEGORIA'] in configuraciones_nivel_4:
						llamar_configuracion.configuracion4(ruta + i['CATEGORIA'], i['CLAVE'],i['URL_QA10'])
					elif i['CATEGORIA'] in configuraciones_nivel_6:
						llamar_configuracion.configuracion6(ruta + i['CATEGORIA'], i['CLAVE'],i['SUB_CLAVE'],i['URL_QA10'])
				elif ambiente == 'QA8':
					if i['CATEGORIA'] in configuraciones_nivel_1:
						llamar_configuracion.configuracion1(ruta + i['CATEGORIA'], i['CLAVE'],i['URL_QA8'])
					elif i['CATEGORIA'] in configuraciones_nivel_2:
						llamar_configuracion.configuracion2(ruta + i['CATEGORIA'], i['CLAVE'],i['SUB_CLAVE'],i['URL_QA8'])
					elif i['CATEGORIA'] in configuraciones_nivel_4:
						llamar_configuracion.configuracion4(ruta + i['CATEGORIA'], i['CLAVE'],i['URL_QA8'])
					elif i['CATEGORIA'] in configuraciones_nivel_6:
						llamar_configuracion.configuracion6(ruta + i['CATEGORIA'], i['CLAVE'],i['SUB_CLAVE'],i['URL_QA8'])

	
	def direccionamiento_offline(self,ambiente,lista):
	#data
		data = [{"_id":{"$oid": "62f168a42140f66d23ec2d4f"},
		"CATEGORIA": "VENTA/SERVBAN.INI",
		"CLAVE": "[Bines]",
		"SUB_CLAVE": "Url",
		"URL_AP14": "https://qa-corr.femcom.net:5002/invoke/PE6.Pub/runGetQueryV2?",
		"URL_QA10": "http://10.184.80.20:8904/invoke/PE6.Pub/runGetQueryV2?",
		"URL_QA8": "http://10.184.40.110:8904/invoke/PE6.Pub/runGetQueryV2?"},
		{"_id":{"$oid": "62f168a42140f66d23ec2d50"},
		"CATEGORIA": "VENTA/SERVBAN.INI",
		"CLAVE": "[Folio]",
		"SUB_CLAVE": "Url",
		"URL_AP14": "https://qa-corr.femcom.net:5002/invoke/PE6.Pub/runGetFolio?",
		"URL_QA10": "http://10.184.80.20:8904/invoke/PE6.Pub/runGetFolio?",
		"URL_QA8": "http://10.184.40.110:8904/invoke/PE6.Pub/runGetFolio?"},
		{"_id":{"$oid": "62f168a42140f66d23ec2d51"},
		"CATEGORIA": "VENTA/SERVBAN.INI",
		"CLAVE": "[Authorization]",
		"SUB_CLAVE": "Url",
		"URL_AP14": "https://qa-corr.femcom.net:5002/invoke/PE6.Pub/runGetAuth?",
		"URL_QA10": "http://10.184.80.20:8904/invoke/PE6.Pub/runGetAuth?",
		"URL_QA8": "http://10.184.40.110:8904/invoke/PE6.Pub/runGetAuth?"},
		{"_id":{"$oid": "62f168a42140f66d23ec2d52"},
		"CATEGORIA": "VENTA/SERVBAN.INI",
		"CLAVE": "[Acknowledge]",
		"SUB_CLAVE": "Url",
		"URL_AP14": "https://qa-corr.femcom.net:5002/invoke/PE6.Pub/runGetAuthAck?",
		"URL_QA10": "http://10.184.80.20:8904/invoke/PE6.Pub/runGetAuthAck?",
		"URL_QA8": "http://10.184.40.110:8904/invoke/PE6.Pub/runGetAuthAck?"},
		{"_id":{"$oid": "62f168a42140f66d23ec2d53"},
		"CATEGORIA": "VENTA/SERVBAN.INI",
		"CLAVE": "[Refund]",
		"SUB_CLAVE": "Url",
		"URL_AP14": "https://qa-tdc.femcom.net:8002/invoke/PE2.Pub/runGetDev?",
		"URL_QA10": "http://10.184.80.20:8890/invoke/PE2.Pub/runGetDev?",
		"URL_QA8": "http://10.184.40.110:8890/invoke/PE2.Pub/runGetDev?"},
		{"_id":{"$oid": "62f168a42140f66d23ec2d54"},
		"CATEGORIA": "VENTA/SERVBAN.INI",
		"CLAVE": "[AcknowledgeRefund]",
		"SUB_CLAVE": "Url",
		"URL_AP14": "https://qa-tdc.femcom.net:8002/invoke/PE2.Pub/runGetDevAck?",
		"URL_QA10": "http://10.184.80.20:8890/invoke/PE2.Pub/runGetDevAck?",
		"URL_QA8": "http://10.184.40.110:8890/invoke/PE2.Pub/runGetDevAck?"},
		{"_id":{"$oid": "62f168a42140f66d23ec2d55"},
		"CATEGORIA": "VENTA/SERVBAN.INI",
		"CLAVE": "[InitializationKeys]",
		"SUB_CLAVE": "Url",
		"URL_AP14": "https://qa-tdc.femcom.net:8002/invoke/PE2.Pub/runGetInitialization?",
		"URL_QA10": "http://10.184.80.20:8890/invoke/PE2.Pub/runGetInitialization?",
		"URL_QA8": "http://10.184.40.110:8890/invoke/PE2.Pub/runGetInitialization?"},
		{"_id":{"$oid": "62f168a42140f66d23ec2d56"},
		"CATEGORIA": "VENTA/SERVBAN.INI",
		"CLAVE": "[Autenticacion]",
		"SUB_CLAVE": "Url",
		"URL_AP14": "http://10.185.179.37:3122/invoke/TPE.FAC.Pub/request?",
		"URL_QA10": "http://10.185.179.37:3122/invoke/TPE.FAC.Pub/request?",
		"URL_QA8": "http://10.185.179.37:3122/invoke/TPE.FAC.Pub/request?"},
		{"_id": {"$oid": "62f168a42140f66d23ec2d57"},
		"CATEGORIA": "VENTA/SERVBAN.INI",
		"CLAVE": "[Autenticacion]",
		"SUB_CLAVE": "UrlValidador",
		"URL_AP14": "http://10.184.80.20:8911/invoke/TPE.VAL.Pub/request?",
		"URL_QA10": "http://10.184.80.20:8911/invoke/TPE.VAL.Pub/request?",
		"URL_QA8": "http://10.184.80.20:8911/invoke/TPE.VAL.Pub/request?"},
		{"_id":{"$oid": "62f168a42140f66d23ec2d58"},
		"CATEGORIA": "XPOS/SubSystems/TAE/TAE.ini",
		"CLAVE": "[TAEComm]",
		"SUB_CLAVE": "URL_Folio",
		"URL_AP14": "PArdqYVPFVqD5JKFwop/NUg5JI/j3pItF9pB3zJJ+0ilUTE/AKXybl7mqRmWEsAGWkD1/3G8JoG1FcXAayRzfFPrLp7hVchC7Og3Zuuw",
		"URL_QA10": "w2S/JVn9npGggrJi1a6v2Xw0YAjoFEg5fyvQqnsQACdWIy2WZPL8EG5N8FCnCn5pwZ5IuSJ0Fb4eOkjlbF0KxVbQIAOgAgG9",
		"URL_QA8": "ilbBxdbvGZfmVDP4L67Xy37jbJ3+1PXiDaKoDi3kuw3EDVsq6xs/jn/5YQjryqFY6ykQLFpKbNNMDbWERb928BX8GzxYkB8piQ=="},
		{"_id":{"$oid": "62f168a42140f66d23ec2d59"},
		"CATEGORIA": "XPOS/SubSystems/TAE/TAE.ini",
		"CLAVE": "[TAEComm]",
		"SUB_CLAVE": "URL_Auth",
		"URL_AP14": "jZDaSADDA8Zbpz0zxIkO1kkmtXHh/Ly9otIxIcTfTKzdg75dUqEtb1tu96cAP5CN4UG8lmm8Ls0FXlK7lo6g4wE=",
		"URL_QA10": "SHMgH/weG13sEAROjS4Wa3qjMBXDr2xPk8oPDZ/ayemdgSjMWv38uj9NL3kbljCClrtqE1IMBvWi2R0=",
		"URL_QA8": "yIQe0vRNsFKf+vr9kbyC3izHOO1CWf1pG+XrPoU0aN7zxaZVQYcQI9/Hj0HVFRIkc3a0h5j8JEeLEt9N"},
		{"_id":{"$oid": "62f168a42140f66d23ec2d5a"},
		"CATEGORIA": "XPOS/SubSystems/TAE/TAE.ini",
		"CLAVE": "[TAEComm]",
		"SUB_CLAVE": "URL_Ack",
		"URL_AP14": "ylsyOhqCAJY/d7M2aPS7/gGWMLmaVZSBeIaFS5vfd/t+gE572sbvwBQke0FIyZ/5fpZvO112H2Fw5jgDZIrhjQ==",
		"URL_QA10": "qfvMCocpfFS52qiqI/YXVP4MJtHp5jGQBTMiX7WhM2eWdLJ6CO3HjDNQe4+QW/82PBLZL5mss4n4Mw==",
		"URL_QA8": "KY+ku5x6vdYlbkVy5J7UOXeL3do5CfcY5DmC95Giik7xTjN2AwsaRn+kgGoq/+hHA/leljVxL+BQ4Xo="},
		{"_id":{"$oid": "62f168a42140f66d23ec2d5b"},
		"CATEGORIA": "XPOS/SubSystems/TAE/TAE.ini",
		"CLAVE": "[TAEStatus]",
		"SUB_CLAVE": "URL",
		"URL_AP14": "https://qa-tae.femcom.net:9002/invoke/PE1.Pub/runGetStatus?",
		"URL_QA10": "http://10.184.80.20:8888/invoke/PE1.Pub/runGetStatus?",
		"URL_QA8": "http://10.184.40.110:8888/invoke/PE1.Pub/runGetStatus?"},
		{"_id":{"$oid": "62f168a42140f66d23ec2d5c"},
		"CATEGORIA": "XPOS/SubSystems/TAE/TAE.ini",
		"CLAVE": "[TAELlavero]",
		"SUB_CLAVE": "URLGET",
		"URL_AP14": "https://10.182.92.67:9003/invoke/TPE.TAE.Keyring.Pub/runGetKeyring?",
		"URL_QA10": "http://10.184.80.20:8895/invoke/TPE.TAE.Keyring.Pub/runGetKeyring?",
		"URL_QA8": "http://10.184.40.110:8895/invoke/TPE.TAE.Keyring.Pub/runGetKeyring?"},
		{"_id":{"$oid": "62f168a42140f66d23ec2d5d"},
		"CATEGORIA": "XPOS/SubSystems/TAE/TAE.ini",
		"CLAVE": "[TAELlavero]",
		"SUB_CLAVE": "URLSET",
		"URL_AP14": "https://10.182.92.67:9003/invoke/TPE.TAE.Keyring.Pub/runSetKeyring?",
		"URL_QA10": "http://10.184.80.20:8895/invoke/TPE.TAE.Keyring.Pub/runSetKeyring?",
		"URL_QA8": "http://10.184.40.110:8895/invoke/TPE.TAE.Keyring.Pub/runSetKeyring?"},
		{"_id":{"$oid": "62f168a42140f66d23ec2d5e"},
		"CATEGORIA": "VENTA/TJCOMM.INI",
		"CLAVE": "[Bines]",
		"SUB_CLAVE": "Url",
		"URL_AP14": "https://qa-corr.femcom.net:5002/invoke/PE6.Pub/runGetQueryV2?",
		"URL_QA10": "http://10.184.80.20:8904/invoke/PE6.Pub/runGetQueryV2?",
		"URL_QA8": "http://10.184.40.110:8904/invoke/PE6.Pub/runGetQueryV2?"},
		{"_id":{"$oid": "62f168a52140f66d23ec2d5f"},
		"CATEGORIA": "VENTA/TJCOMM.INI",
		"CLAVE": "[Folio]",
		"SUB_CLAVE": "Url",
		"URL_AP14": "https://qa-tdc.femcom.net:8002/invoke/PE2.Pub/runGetFolio?",
		"URL_QA10": "http://10.184.80.20:8890/invoke/PE2.Pub/runGetFolio?",
		"URL_QA8": "http://10.184.40.110:8890/invoke/PE2.Pub/runGetFolio?"},
		{"_id":{"$oid": "62f168a52140f66d23ec2d60"},
		"CATEGORIA": "VENTA/TJCOMM.INI",
		"CLAVE": "[Authorization]",
		"SUB_CLAVE": "Url",
		"URL_AP14": "https://qa-tdc.femcom.net:8002/invoke/PE2.Pub/runGetAuth?",
		"URL_QA10": "http://10.184.80.20:8890/invoke/PE2.Pub/runGetAuth?",
		"URL_QA8": "http://10.184.40.110:8890/invoke/PE2.Pub/runGetAuth?"},
		{"_id":{"$oid": "62f168a52140f66d23ec2d61"},
		"CATEGORIA": "VENTA/TJCOMM.INI",
		"CLAVE": "[Acknowledge]",
		"SUB_CLAVE": "Url",
		"URL_AP14": "https://qa-tdc.femcom.net:8002/invoke/PE2.Pub/runGetAuthAck?",
		"URL_QA10": "http://10.184.80.20:8890/invoke/PE2.Pub/runGetAuthAck?",
		"URL_QA8": "http://10.184.40.110:8890/invoke/PE2.Pub/runGetAuthAck?"},
		{"_id":{"$oid": "62f168a52140f66d23ec2d62"},
		"CATEGORIA": "VENTA/TJCOMM.INI",
		"CLAVE": "[Refund]",
		"SUB_CLAVE": "Url",
		"URL_AP14": "https://qa-tdc.femcom.net:8002/invoke/PE2.Pub/runGetDev?",
		"URL_QA10": "http://10.184.80.20:8890/invoke/PE2.Pub/runGetDev?",
		"URL_QA8": "http://10.184.40.110:8890/invoke/PE2.Pub/runGetDev?"},
		{"_id":{"$oid": "62f168a52140f66d23ec2d63"},
		"CATEGORIA": "VENTA/TJCOMM.INI",
		"CLAVE": "[AcknowledgeRefund]",
		"SUB_CLAVE": "Url",
		"URL_AP14": "https://qa-tdc.femcom.net:8002/invoke/PE2.Pub/runGetDevAck?",
		"URL_QA10": "http://10.184.80.20:8890/invoke/PE2.Pub/runGetDevAck?",
		"URL_QA8": "http://10.184.40.110:8890/invoke/PE2.Pub/runGetDevAck?"},
		{"_id":{"$oid": "62f168a52140f66d23ec2d64"},
		"CATEGORIA": "VENTA/TJCOMM.INI",
		"CLAVE": "[InitializationKeys]",
		"SUB_CLAVE": "Url",
		"URL_AP14": "https://qa-tdc.femcom.net:8002/invoke/PE2.Pub/runGetInitialization?",
		"URL_QA10": "http://10.184.80.20:8890/invoke/PE2.Pub/runGetInitialization?",
		"URL_QA8": "http://10.184.40.110:8890/invoke/PE2.Pub/runGetInitialization?"},
		{"_id":{"$oid": "62f168a52140f66d23ec2d65"},
		"CATEGORIA": "VENTA/P_LINEA.INI",
		"CLAVE": "[PREDIAL]",
		"SUB_CLAVE": "Url",
		"URL_AP14": "https://qa-mun.femcom.net:3001/invoke/TPE.MUN.Pub/request?",
		"URL_QA10": "http://10.184.80.20:8897/invoke/TPE.MUN.Pub/request?",
		"URL_QA8": "http://10.184.40.110:8897/invoke/TPE.MUN.Pub/request?"},
		{"_id":{"$oid": "62f168a52140f66d23ec2d66"},
		"CATEGORIA": "VENTA/P_LINEA.INI",
		"CLAVE": "[MULTAS]",
		"SUB_CLAVE": "Url",
		"URL_AP14": "https://qa-mun.femcom.net:3001/invoke/TPE.MUN.Pub/request?",
		"URL_QA10": "http://10.184.80.20:8897/invoke/TPE.MUN.Pub/request?",
		"URL_QA8": "http://10.184.40.110:8897/invoke/TPE.MUN.Pub/request?"},
		{"_id":{"$oid": "62f168a52140f66d23ec2d67"},
		"CATEGORIA": "VENTA/P_LINEA.INI",
		"CLAVE": "[SERVICIOS]",
		"SUB_CLAVE": "Url",
		"URL_AP14": "cVBla4zZn/EQD7Yg5YevTxElCfoej3esU9vERMVgglJlq6lgO/OtxxRvGz+vOUoeKzoVwIfBkK9SQ1p6GpDT6pqg",
		"URL_QA10": "iekLY0i6FpdO3CkeRGtTbcNUZMbqLTrBFyziec+lIdKmFyT5DuGU2QIDBzKcU/mxv/WhOgnHbUPvVEf1",
		"URL_QA8": "tm0v9iE7CFwegvKYSlzPNOPgkF1aoi4crzTaFG9TcUX4GRF12IhoJd5D5djBPz9c2S1LFsaq92q6aiBX1w=="},
		{"_id":{"$oid": "62f168a52140f66d23ec2d68"},
		"CATEGORIA": "VENTA/P_LINEA.INI",
		"CLAVE": "[BOLETOS]",
		"SUB_CLAVE": "Url",
		"URL_AP14": "https://qa-cine.femcom.net:8001/invoke/TPE.CINES.Pub/request?",
		"URL_QA10": "http://10.184.80.20:8914/invoke/TPE.CINES.Pub/request?",
		"URL_QA8": "http://10.184.40.110:8914/invoke/TPE.CINES.Pub/request?"},
		{"_id":{"$oid": "62f168a52140f66d23ec2d69"},
		"CATEGORIA": "ED/EDConfig.XML",
		"CLAVE": "<Tabulador url=",
		"SUB_CLAVE": 0,
		"URL_AP14": "\"https://10.182.92.59:3002/invoke/TPE.TSF.Pub/request?\"",
		"URL_QA10": "\"http://10.184.80.20:8907/invoke/TPE.TSF.Pub/request?\"",
		"URL_QA8": "\"http://10.184.40.110:8907/invoke/TPE.TSF.Pub/request?\""},
		{"_id":{"$oid": "62f168a52140f66d23ec2d6a"},
		"CATEGORIA": "ED/EDConfig.XML",
		"CLAVE": "<Cotizacion url=",
		"SUB_CLAVE": 0,
		"URL_AP14": "\"https://10.182.92.59:3002/invoke/TPE.TSF.Pub/request?\"",
		"URL_QA10": "\"http://10.184.80.20:8907/invoke/TPE.TSF.Pub/request?\"",
		"URL_QA8": "\"http://10.184.40.110:8907/invoke/TPE.TSF.Pub/request?\""},
		{"_id":{"$oid": "62f168a52140f66d23ec2d6b"},
		"CATEGORIA": "ED/EDConfig.XML",
		"CLAVE": "<Beneficiarios url=",
		"SUB_CLAVE": 0,
		"URL_AP14": "\"https://10.182.92.59:3002/invoke/TPE.TSF.Pub/request?\"",
		"URL_QA10": "\"http://10.184.80.20:8907/invoke/TPE.TSF.Pub/request?\"",
		"URL_QA8": "\"http://10.184.40.110:8907/invoke/TPE.TSF.Pub/request?\""},
		{"_id":{"$oid": "62f168a52140f66d23ec2d6c"},
		"CATEGORIA": "ED/EDConfig.XML",
		"CLAVE": "<Transferencia url=",
		"SUB_CLAVE": 0,
		"URL_AP14": "\"https://10.182.92.59:3002/invoke/TPE.TSF.Pub/request?\"",
		"URL_QA10": "\"http://10.184.80.20:8907/invoke/TPE.TSF.Pub/request?\"",
		"URL_QA8": "\"http://10.184.40.110:8907/invoke/TPE.TSF.Pub/request?\""},
		{"_id":{"$oid": "62f168a52140f66d23ec2d6d"},
		"CATEGORIA": "ED/EDConfig.XML",
		"CLAVE": "<Folio url=",
		"SUB_CLAVE": 0,
		"URL_AP14": "\"https://10.182.92.59:3002/invoke/TPE.TSF.Pub/request?\"",
		"URL_QA10": "\"http://10.184.80.20:8907/invoke/TPE.TSF.Pub/request?\"",
		"URL_QA8": "\"http://10.184.40.110:8907/invoke/TPE.TSF.Pub/request?\""},
		{"_id":{"$oid": "62f168a62140f66d23ec2d6e"},
		"CATEGORIA": "ED/EDConfig.XML",
		"CLAVE": "<Autorizacion url=",
		"SUB_CLAVE": 0,
		"URL_AP14": "\"https://10.182.92.59:3002/invoke/TPE.TSF.Pub/request?\"",
		"URL_QA10": "\"http://10.184.80.20:8907/invoke/TPE.TSF.Pub/request?\"",
		"URL_QA8": "\"http://10.184.40.110:8907/invoke/TPE.TSF.Pub/request?\""},
		{"_id":{"$oid": "62f168a62140f66d23ec2d6f"},
		"CATEGORIA": "ED/EDConfig.XML",
		"CLAVE": "<ACK url=",
		"SUB_CLAVE": 0,
		"URL_AP14": "\"https://10.182.92.59:3002/invoke/TPE.TSF.Pub/request?\"",
		"URL_QA10": "\"http://10.184.80.20:8907/invoke/TPE.TSF.Pub/request?\"",
		"URL_QA8": "\"http://10.184.40.110:8907/invoke/TPE.TSF.Pub/request?\""},
		{"_id":{"$oid": "62f168a62140f66d23ec2d70"},
		"CATEGORIA": "ED/EDConfig.XML",
		"CLAVE": "<RemesaConsulta url=",
		"SUB_CLAVE": 0,
		"URL_AP14": "\"https://10.182.92.70:2002/invoke/TPE.TSF.Pub/request?\"",
		"URL_QA10": "\"http://10.184.80.20:8917/invoke/TPE.TSF.Pub/request?\"",
		"URL_QA8": "\"http://10.184.40.110:8917/invoke/TPE.TSF.Pub/request?\""},
		{"_id":{"$oid": "62f168a62140f66d23ec2d71"},
		"CATEGORIA": "ED/EDConfig.XML",
		"CLAVE": "<RemesaGENIII url=",
		"SUB_CLAVE": 0,
		"URL_AP14": "\"https://10.182.92.70:2002/invoke/TPE.TSF.Pub/request?\"",
		"URL_QA10": "\"http://10.184.80.20:8917/invoke/TPE.TSF.Pub/request?\"",
		"URL_QA8": "\"http://10.184.40.110:8917/invoke/TPE.TSF.Pub/request?\""},
		{"_id":{"$oid": "62f168a62140f66d23ec2d72"},
		"CATEGORIA": "ED/EDConfig.XML",
		"CLAVE": "<RemesaDesbloqueo url=",
		"SUB_CLAVE": 0,
		"URL_AP14": "\"https://10.182.92.70:2002/invoke/TPE.TSF.Pub/request?\"",
		"URL_QA10": "\"http://10.184.80.20:8917/invoke/TPE.TSF.Pub/request?\"",
		"URL_QA8": "\"http://10.184.40.110:8917/invoke/TPE.TSF.Pub/request?\""},
		{"_id":{"$oid": "62f168a62140f66d23ec2d73"},
		"CATEGORIA": "ED/EDConfig.XML",
		"CLAVE": "<RemesaFolio url=",
		"SUB_CLAVE": 0,
		"URL_AP14": "\"https://10.182.92.70:2002/invoke/TPE.TSF.Pub/request?\"",
		"URL_QA10": "\"http://10.184.80.20:8917/invoke/TPE.TSF.Pub/request?\"",
		"URL_QA8": "\"http://10.184.40.110:8917/invoke/TPE.TSF.Pub/request?\""},
		{"_id":{"$oid": "62f168a62140f66d23ec2d74"},
		"CATEGORIA": "ED/EDConfig.XML",
		"CLAVE": "<RemesaAutorizacion url=",
		"SUB_CLAVE": 0,
		"URL_AP14": "\"https://10.182.92.70:2002/invoke/TPE.TSF.Pub/request?\"",
		"URL_QA10": "\"http://10.184.80.20:8917/invoke/TPE.TSF.Pub/request?\"",
		"URL_QA8": "\"http://10.184.40.110:8917/invoke/TPE.TSF.Pub/request?\""},
		{"_id":{"$oid": "62f168a62140f66d23ec2d75"},
		"CATEGORIA": "ED/EDConfig.XML",
		"CLAVE": "<RemesaACK url=",
		"SUB_CLAVE": 0,
		"URL_AP14": "\"https://10.182.92.70:2002/invoke/TPE.TSF.Pub/request?\"",
		"URL_QA10": "\"http://10.184.80.20:8917/invoke/TPE.TSF.Pub/request?\"",
		"URL_QA8": "\"http://10.184.40.110:8917/invoke/TPE.TSF.Pub/request?\""},
		{"_id":{"$oid": "62f168a62140f66d23ec2d76"},
		"CATEGORIA": "ED/EDConfig.XML",
		"CLAVE": "<RemesaReversa url=",
		"SUB_CLAVE": 0,
		"URL_AP14": "\"https://10.182.92.70:2002/invoke/TPE.TSF.Pub/request?\"",
		"URL_QA10": "\"http://10.184.80.20:8917/invoke/TPE.TSF.Pub/request?\"",
		"URL_QA8": "\"http://10.184.40.110:8917/invoke/TPE.TSF.Pub/request?\""},
		{"_id":{"$oid": "62f168a62140f66d23ec2d77"},
		"CATEGORIA": "ED/EDConfig.XML",
		"CLAVE": "<RemesaTransnetwork url=",
		"SUB_CLAVE": 0,
		"URL_AP14": "\"https://10.182.92.70:2002/invoke/TPE.TSF.Pub/request?\"",
		"URL_QA10": "\"http://10.184.80.20:8917/invoke/TPE.TSF.Pub/request?\"",
		"URL_QA8": "\"http://10.184.40.110:8917/invoke/TPE.TSF.Pub/request?\""},
		{"_id":{"$oid": "62f168a62140f66d23ec2d78"},
		"CATEGORIA": "VENTA/PLN/VBCINE.XML",
		"CLAVE": "<URL>",
		"SUB_CLAVE": 0,
		"URL_AP14": "https://qa-cine.femcom.net:8001/invoke/TPE.CINES.Pub/request?</URL>",
		"URL_QA10": "http://10.184.80.20:8914/invoke/TPE.CINES.Pub/request?</URL>",
		"URL_QA8": "http://10.184.40.110:8914/invoke/TPE.CINES.Pub/request?</URL>"},
		{"_id": {"$oid": "62f168a62140f66d23ec2d79"},
		"CATEGORIA": "MVB/MVB.INI",
		"CLAVE": "url",
		"SUB_CLAVE": 0,
		"URL_AP14": "=https://qa-bus.femcom.net:9001/invoke/TPE.BUS.Pub/",
		"URL_QA10": "=http://10.184.80.20:8891/invoke/TPE.BUS.Pub/",
		"URL_QA8": "=http://10.184.40.110:8891/invoke/TPE.BUS.Pub/"},
		{"_id":{"$oid": "62f168a62140f66d23ec2d7a"},
		"CATEGORIA": "MVB/MVB.INI",
		"CLAVE": "corrTmOut",
		"SUB_CLAVE": 0,
		"URL_AP14": "=240",
		"URL_QA10": "=240",
		"URL_QA8": "=240"},
		{"_id": {"$oid": "62f168a62140f66d23ec2d7b"},
		"CATEGORIA": "MVB/CADENAMVB.INI",
		"CLAVE": "url",
		"SUB_CLAVE": 0,
		"URL_AP14": "= https://qa-bus.femcom.net:9001/invoke/TPE.BUS.Pub/",
		"URL_QA10": "= http://10.184.80.20:8891/invoke/TPE.BUS.Pub/",
		"URL_QA8": "= http://10.184.40.110:8891/invoke/TPE.BUS.Pub/"},
		{"_id": {"$oid": "62f168a62140f66d23ec2d7c"},
		"CATEGORIA": "MVB/CADENAMVB.INI",
		"CLAVE": "corrTmOut",
		"SUB_CLAVE": 0,
		"URL_AP14": "= 240",
		"URL_QA10": "= 240",
		"URL_QA8": "= 240"},
		{"_id": {"$oid": "62f168a62140f66d23ec2d7d"},
		"CATEGORIA": "GC/GcAConfig.INI",
		"CLAVE": "[TAEFolio]",
		"SUB_CLAVE": "URL",
		"URL_AP14": "https://qa-gift.femcom.net:7002/invoke/PE3.Pub/runGetFolio?",
		"URL_QA10": "http://10.184.80.20:8896/invoke/PE3.Pub/runGetFolio?",
		"URL_QA8": "http://10.184.40.110:8896/invoke/PE3.Pub/runGetFolio?"},
		{"_id": {"$oid": "62f168a72140f66d23ec2d7e"},
		"CATEGORIA": "GC/GcAConfig.INI",
		"CLAVE": "[TAEAuth]",
		"SUB_CLAVE": "URL",
		"URL_AP14": "https://qa-gift.femcom.net:7002/invoke/PE3.Pub/runGetActivation?",
		"URL_QA10": "http://10.184.80.20:8896/invoke/PE3.Pub/runGetActivation?",
		"URL_QA8": "http://10.184.40.110:8896/invoke/PE3.Pub/runGetActivation?"},
		{"_id": {"$oid": "62f168a72140f66d23ec2d7f"},
		"CATEGORIA": "GC/GcAConfig.INI",
		"CLAVE": "[TAEAck]",
		"SUB_CLAVE": "URL",
		"URL_AP14": "https://qa-gift.femcom.net:7002/invoke/PE3.Pub/runGetAck?",
		"URL_QA10": "http://10.184.80.20:8896/invoke/PE3.Pub/runGetAck?",
		"URL_QA8": "http://10.184.40.110:8896/invoke/PE3.Pub/runGetAck?"},
		{"_id": {"$oid": "62f168a72140f66d23ec2d80"},
		"CATEGORIA": "GC/GcAConfig.INI",
		"CLAVE": "[TAELlavero]",
		"SUB_CLAVE": "URLGET",
		"URL_AP14": "https://qa-gift.femcom.net:7002/invoke/TPE.TAE.Keyring.Pub/runGetKeyring?",
		"URL_QA10": "http://10.184.80.20:8896/invoke/TPE.TAE.Keyring.Pub/runGetKeyring?",
		"URL_QA8": "http://10.184.40.110:8896/invoke/TPE.TAE.Keyring.Pub/runGetKeyring?"},
		{"_id": {"$oid": "62f168a72140f66d23ec2d81"},
		"CATEGORIA": "GC/GcAConfig.INI",
		"CLAVE": "[TAELlavero]",
		"SUB_CLAVE": "URLSET",
		"URL_AP14": "https://qa-gift.femcom.net:7002/invoke/TPE.TAE.Keyring.Pub/runSetKeyring?",
		"URL_QA10": "http://10.184.80.20:8896/invoke/TPE.TAE.Keyring.Pub/runSetKeyring?",
		"URL_QA8": "http://10.184.40.110:8896/invoke/TPE.TAE.Keyring.Pub/runSetKeyring?"},
		{"_id": {"$oid": "62f168a72140f66d23ec2d82"},
		"CATEGORIA": "GC/GcAConfig.INI",
		"CLAVE": "[TAEEstatus]",
		"SUB_CLAVE": "URL",
		"URL_AP14": "https://qa-gift.femcom.net:7002/invoke/PE3.Pub/runGetStatus?",
		"URL_QA10": "http://10.184.80.20:8896/invoke/PE3.Pub/runGetStatus?",
		"URL_QA8": "http://10.184.40.110:8896/invoke/PE3.Pub/runGetStatus?"},
		{"_id": {"$oid": "62f168a72140f66d23ec2d83"},
		"CATEGORIA": "GC/GCConfig.INI",
		"CLAVE": "[TAEFolio]",
		"SUB_CLAVE": "URL",
		"URL_AP14": "https://qa-gift.femcom.net:7002/invoke/PE3.Pub/runGetFolio?",
		"URL_QA10": "http://10.184.80.20:8896/invoke/PE3.Pub/runGetFolio?",
		"URL_QA8": "http://10.184.40.110:8896/invoke/PE3.Pub/runGetFolio?"},
		{"_id": {"$oid": "62f168a72140f66d23ec2d84"},
		"CATEGORIA": "GC/GCConfig.INI",
		"CLAVE": "[TAEAuth]",
		"SUB_CLAVE": "URL",
		"URL_AP14": "https://qa-gift.femcom.net:7002/invoke/PE3.Pub/runGetActivation?",
		"URL_QA10": "http://10.184.80.20:8896/invoke/PE3.Pub/runGetActivation?",
		"URL_QA8": "http://10.184.40.110:8896/invoke/PE3.Pub/runGetActivation?"},
		{"_id": {"$oid": "62f168a72140f66d23ec2d85"},
		"CATEGORIA": "GC/GCConfig.INI",
		"CLAVE": "[TAEAck]",
		"SUB_CLAVE": "URL",
		"URL_AP14": "https://qa-gift.femcom.net:7002/invoke/PE3.Pub/runGetAck?",
		"URL_QA10": "http://10.184.80.20:8896/invoke/PE3.Pub/runGetAck?",
		"URL_QA8": "http://10.184.40.110:8896/invoke/PE3.Pub/runGetAck?"},
		{"_id": {"$oid": "62f168a72140f66d23ec2d86"},
		"CATEGORIA": "GC/GCConfig.INI",
		"CLAVE": "[TAEEstatus]",
		"SUB_CLAVE": "URL",
		"URL_AP14": "https://qa-gift.femcom.net:7002/invoke/PE3.Pub/runGetStatus?",
		"URL_QA10": "http://10.184.80.20:8896/invoke/PE3.Pub/runGetStatus?",
		"URL_QA8": "http://10.184.40.110:8896/invoke/PE3.Pub/runGetStatus?"}]

		configuraciones_nivel_1 = ['VENTA/PLN/VBCINE.XML','MVB/MVB.INI','MVB/CADENAMVB.INI']
		configuraciones_nivel_2 = ['VENTA/SERVBAN.INI','XPOS/SubSystems/TAE/TAE.ini','VENTA/TJCOMM.INI']
		configuraciones_nivel_4 = ['ED/EDConfig.XML']
		configuraciones_nivel_6 = ['VENTA/P_LINEA.INI','GC/GcAConfig.INI','GC/GCConfig.INI']

		llamar_configuracion = Configuraciones()
		ruta = 'C:/'
		for i in data:
			if i['CATEGORIA'] in lista:
				if ambiente == 'AP14':
					if i['CATEGORIA'] in configuraciones_nivel_1:
						llamar_configuracion.configuracion1(ruta + i['CATEGORIA'], i['CLAVE'],i['URL_AP14'])
					elif i['CATEGORIA'] in configuraciones_nivel_2:
						llamar_configuracion.configuracion2(ruta + i['CATEGORIA'], i['CLAVE'], i['SUB_CLAVE'],i['URL_AP14'])
					elif i['CATEGORIA'] in configuraciones_nivel_4:
						llamar_configuracion.configuracion4(ruta + i['CATEGORIA'], i['CLAVE'],i['URL_AP14'])
					elif i['CATEGORIA'] in configuraciones_nivel_6:
						llamar_configuracion.configuracion6(ruta + i['CATEGORIA'], i['CLAVE'], i['SUB_CLAVE'],i['URL_AP14'])
				elif ambiente == 'QA10':
					if i['CATEGORIA'] in configuraciones_nivel_1:
						llamar_configuracion.configuracion1(ruta + i['CATEGORIA'], i['CLAVE'],i['URL_QA10'])
					elif i['CATEGORIA'] in configuraciones_nivel_2:
						llamar_configuracion.configuracion2(ruta + i['CATEGORIA'], i['CLAVE'], i['SUB_CLAVE'],i['URL_QA10'])
					elif i['CATEGORIA'] in configuraciones_nivel_4:
						llamar_configuracion.configuracion4(ruta + i['CATEGORIA'], i['CLAVE'],i['URL_QA10'])
					elif i['CATEGORIA'] in configuraciones_nivel_6:
						llamar_configuracion.configuracion6(ruta + i['CATEGORIA'], i['CLAVE'], i['SUB_CLAVE'],i['URL_QA10'])
				elif ambiente == 'QA8':
					if i['CATEGORIA'] in configuraciones_nivel_1:
						llamar_configuracion.configuracion1(ruta + i['CATEGORIA'], i['CLAVE'],i['URL_QA8'])
					elif i['CATEGORIA'] in configuraciones_nivel_2:
						llamar_configuracion.configuracion2(ruta + i['CATEGORIA'], i['CLAVE'], i['SUB_CLAVE'],i['URL_QA8'])
					elif i['CATEGORIA'] in configuraciones_nivel_4:
						llamar_configuracion.configuracion4(ruta + i['CATEGORIA'], i['CLAVE'],i['URL_QA8'])
					elif i['CATEGORIA'] in configuraciones_nivel_6:
						llamar_configuracion.configuracion6(ruta + i['CATEGORIA'], i['CLAVE'], i['SUB_CLAVE'],i['URL_QA8'])

	def direccionamiento_offline_json(self,ambiente,lista):
		try:
			with open('data.json','r') as archivo:
				data = json.load(archivo)
		except Exception as e:
			return False

		configuraciones_nivel_1 = ['VENTA/PLN/VBCINE.XML','MVB/MVB.INI','MVB/CADENAMVB.INI']
		configuraciones_nivel_2 = ['VENTA/SERVBAN.INI','XPOS/SubSystems/TAE/TAE.ini','VENTA/TJCOMM.INI']
		configuraciones_nivel_4 = ['ED/EDConfig.XML']
		configuraciones_nivel_6 = ['VENTA/P_LINEA.INI','GC/GcAConfig.INI','GC/GCConfig.INI']

		llamar_configuracion = Configuraciones()
		ruta = 'C:/'
		for i in data:
			if i['CATEGORIA'] in lista:
				if ambiente == 'AP14':
					if i['CATEGORIA'] in configuraciones_nivel_1:
						llamar_configuracion.configuracion1(ruta + i['CATEGORIA'], i['CLAVE'],i['URL_AP14'])
					elif i['CATEGORIA'] in configuraciones_nivel_2:
						llamar_configuracion.configuracion2(ruta + i['CATEGORIA'], i['CLAVE'], i['SUB_CLAVE'],i['URL_AP14'])
					elif i['CATEGORIA'] in configuraciones_nivel_4:
						llamar_configuracion.configuracion4(ruta + i['CATEGORIA'], i['CLAVE'],i['URL_AP14'])
					elif i['CATEGORIA'] in configuraciones_nivel_6:
						llamar_configuracion.configuracion6(ruta + i['CATEGORIA'], i['CLAVE'], i['SUB_CLAVE'],i['URL_AP14'])
				elif ambiente == 'QA10':
					if i['CATEGORIA'] in configuraciones_nivel_1:
						llamar_configuracion.configuracion1(ruta + i['CATEGORIA'], i['CLAVE'],i['URL_QA10'])
					elif i['CATEGORIA'] in configuraciones_nivel_2:
						llamar_configuracion.configuracion2(ruta + i['CATEGORIA'], i['CLAVE'], i['SUB_CLAVE'],i['URL_QA10'])
					elif i['CATEGORIA'] in configuraciones_nivel_4:
						llamar_configuracion.configuracion4(ruta + i['CATEGORIA'], i['CLAVE'],i['URL_QA10'])
					elif i['CATEGORIA'] in configuraciones_nivel_6:
						llamar_configuracion.configuracion6(ruta + i['CATEGORIA'], i['CLAVE'], i['SUB_CLAVE'],i['URL_QA10'])
				elif ambiente == 'QA8':
					if i['CATEGORIA'] in configuraciones_nivel_1:
						llamar_configuracion.configuracion1(ruta + i['CATEGORIA'], i['CLAVE'],i['URL_QA8'])
					elif i['CATEGORIA'] in configuraciones_nivel_2:
						llamar_configuracion.configuracion2(ruta + i['CATEGORIA'], i['CLAVE'], i['SUB_CLAVE'],i['URL_QA8'])
					elif i['CATEGORIA'] in configuraciones_nivel_4:
						llamar_configuracion.configuracion4(ruta + i['CATEGORIA'], i['CLAVE'],i['URL_QA8'])
					elif i['CATEGORIA'] in configuraciones_nivel_6:
						llamar_configuracion.configuracion6(ruta + i['CATEGORIA'], i['CLAVE'], i['SUB_CLAVE'],i['URL_QA8'])
	
if __name__ == '__main__':
	llamar_manage = Manage()
	lista_claves=['VENTA/SERVBAN.INI','XPOS/SubSystems/TAE/TAE.ini','VENTA/TJCOMM.INI',
	'VENTA/P_LINEA.INI','ED/EDConfig.XML','VENTA/PLN/VBCINE.XML','MVB/MVB.INI','MVB/CADENAMVB.INI','GC/GcAConfig.INI','GC/GCConfig.INI']
	#llamar_manage.direccionamiento_offline('QA8',lista_claves)
