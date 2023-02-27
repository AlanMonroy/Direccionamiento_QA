# Creador: Roberto Alan Rodriguez Monroy
from tkinter import *
from tkinter import ttk, filedialog, messagebox
from Conexion_MongoDB import MongoDB
from manage_data import Manage


class Login:
    def __init__(self, ventana, title):
        fondo = 'black'; letra = 'white'; color_check = 'black'
        self.window = ventana
        self.window.title(title)
        self.window.resizable(False, False)
        self.window.configure(background=fondo)
        self.window.wm_attributes("-transparentcolor", "#60b26c")   # 60b26c
        self.window.wm_attributes("-alpha", .85)

        notebook = ttk.Notebook(self.window)
        notebook.grid(row=0, column=0)

        #   estilo = style()
        ttk.Style().configure("TFrame", background=fondo)

        # Frames del Notebook
        self.ventana1 = ttk.Frame(notebook, width=400, height=280)
        self.ventana2 = ttk.Frame(notebook, width=400, height=280)
        self.ventana3 = ttk.Frame(notebook, width=400, height=280)

        self.ventana1.pack(fill='both', expand=True)
        self.ventana2.pack(fill='both', expand=True)
        self.ventana3.pack(fill='both', expand=True)

        # Agregar frames al notebook
        notebook.add(self.ventana1, text='Online')
        notebook.add(self.ventana2, text='Offline')
        notebook.add(self.ventana3, text="Validación IP")

        frame2 = Frame(self.window, bg=fondo)

        #   CREDITOS    #
        frame2.grid(row=10, column=0)
        label2 = Label(frame2, text="Creado por Roberto Alan Rodriguez Monroy", fg="white", bg=fondo, font=("Arial", 8))
        label2.grid(row=10, column=0, padx=10, columnspan=2)
        self.mostrar_ventana2()
        self.ventana1_seleccion()

    #VENTANA 2 (OFFLINE)
    def mostrar_ventana2(self):
        configuraciones = ["AP14", "QA10", 'QA8']
        fondo = 'black'; letra = 'white'; color_check = 'black'
        self.ventana2_1 = Frame(self.ventana2, bg=fondo)
        self.ventana2_1.place(x=100, y=10)

        boton_cargar = Button(self.ventana2_1, text="Cargar DB online", fg="white", font=("Semi Bold", 10),
                              bg="black", cursor='hand2', command=self.cargar_database)
        boton_cargar.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        self.comb_configuraciones_2 = ttk.Combobox(self.ventana2_1, values=configuraciones, state="readonly",
                                                   font=("Tahoma", 12), foreground="black", width=5)
        self.comb_configuraciones_2.current(0)
        self.comb_configuraciones_2.grid(row=2, column=0, padx=10, pady=10, columnspan=2)

        self.SERVBAN_2 = BooleanVar(); self.TJCOMM_2 = BooleanVar(); self.ED_2 = BooleanVar(); self.MVB_2 = BooleanVar()
        self.TAE_2 = BooleanVar(); self.P_LINEA_2 = BooleanVar(); self.VBCINE_2 = BooleanVar(); self.GC_2 = BooleanVar()

        self.TODOS_2 = BooleanVar()
        self.check_TODOS_2 = Checkbutton(self.ventana2_1, text="Todos", bg=fondo, fg=letra, selectcolor=color_check,
                                         variable=self.TODOS_2, onvalue=True, offvalue=False, command=self.funcion2_2)
        self.check_TODOS_2.grid(row=3, column=0, padx=10, columnspan=2)
        self.check_TODOS_2.select()

        self.frame_base_2 = Frame(self.ventana2_1, bg=fondo)
        self.frame_base_2.grid(row=4, column=0, padx=10, columnspan=2)

        self.check_servban_2 = Checkbutton(self.frame_base_2, text="ServBan", bg=fondo, fg=letra, selectcolor=color_check, variable= self.SERVBAN_2, onvalue=True, offvalue=False)
        self.check_servban_2.grid(row=4, column=0,padx=10, sticky="w")

        self.check_tae_2 = Checkbutton(self.frame_base_2, text="TAE", bg=fondo, fg=letra,selectcolor=color_check, variable=self.TAE_2, onvalue=True, offvalue=False)
        self.check_tae_2.grid(row=4, column=1, padx=10, sticky="w")

        self.check_tjcomm_2 = Checkbutton(self.frame_base_2, text="TJCOMM", bg=fondo, fg=letra,selectcolor=color_check, variable=self.TJCOMM_2, onvalue=True, offvalue=False)
        self.check_tjcomm_2.grid(row=5, column=0,padx=10, sticky="w")

        self.check_P_LINEA_2 = Checkbutton(self.frame_base_2, text="P_LINEA", bg=fondo, fg=letra,selectcolor=color_check, variable= self.P_LINEA_2, onvalue=True, offvalue=False)
        self.check_P_LINEA_2.grid(row=5, column=1, padx=10, sticky="w")

        self.check_ED_2 = Checkbutton(self.frame_base_2, text="ED", bg=fondo, fg=letra,selectcolor=color_check, variable=self.ED_2, onvalue=True, offvalue=False)
        self.check_ED_2.grid(row=6, column=0, padx=10, sticky="w")

        self.check_VBCINE_2 = Checkbutton(self.frame_base_2, text="VBCINE", bg=fondo, fg=letra, selectcolor=color_check, variable=self.VBCINE_2, onvalue=True, offvalue=False)
        self.check_VBCINE_2.grid(row=6, column=1, padx=10, sticky="w")

        self.check_MVB_2 = Checkbutton(self.frame_base_2, text="MVB", bg=fondo, fg=letra,selectcolor=color_check, variable=self.MVB_2, onvalue=True, offvalue=False)
        self.check_MVB_2.grid(row=7, column=0, padx=10, sticky="w")

        self.check_GC_2 = Checkbutton(self.frame_base_2, text="GC", bg=fondo, fg=letra,selectcolor=color_check, variable=self.GC_2, onvalue=True, offvalue=False)
        self.check_GC_2.grid(row=7, column=1, padx=10, sticky="w")

        boton_2 = Button(self.ventana2_1, text="Direccionar", fg="black", activeforeground='white', activebackground='black', font=("Semi Bold", 10), bg="white", cursor='hand2', command=self.funcion_configurar_2)
        boton_2.grid(row=8, column=0, columnspan=2, padx=10, pady=20)

        self.check_servban_2.select() ; self.check_tae_2.select() ; self.check_tjcomm_2.select() ; self.check_P_LINEA_2.select()
        self.check_ED_2.select() ; self.check_VBCINE_2.select() ; self.check_MVB_2.select() ; self.check_GC_2.select()

        self.ventana2_1.bind("<Return>", self.funcion1_2)   #   Funcion al presionar <Enter> (No funciona idk)


    def ventana1_seleccion(self):
        fondo = 'black'; letra = 'white' ; color_check = 'black' 
        self.ventana1_1 = Frame(self.ventana1, bg=fondo)
        self.ventana1_1.place(x=0,y=30)

        label1 = Label(self.ventana1_1,text="Configuración solo disponible con VPN",fg=letra,bg=fondo,font=("Arial",10))
        label1.grid(row=0,column=0,padx=10,pady=5,columnspan=2)

        label2 = Label(self.ventana1_1,text="- Requieres de una conexión con la computadora -",fg=letra,bg=fondo,font=("Arial",10))
        label2.grid(row=1,column=0,padx=10,pady=5,columnspan=2)

        boton_ip = Button(self.ventana1_1, text= "Seleccionar unidad",fg="black",font=("Semi Bold",10),bg="white",cursor='hand2',command=self.ruta_computadora)
        boton_ip.grid(row=2,column=0,padx=140,pady=50 )

    def regresar(self):
        self.ventana1_1.destroy()
        self.ventana1_seleccion()

# VENTANA 1 #
    def mostrar_ventana1(self):
        fondo = 'black'; letra = 'white' ; color_check = 'black' 
        configuraciones=["AP14", "QA10",'QA8']
        self.ventana1_1.destroy()
 
        self.ventana1_1 = Frame(self.ventana1, bg=fondo)
        self.ventana1_1.place(x=100,y=10)

        boton_back = Button(self.ventana1_1, text= "<",fg="white",font=("Semi Bold",10),bg="black",cursor='hand2',command=self.regresar)
        boton_back.place(x=0,y=0)

        self.comb_configuraciones = ttk.Combobox(self.ventana1_1,values = configuraciones,state = "readonly",font = ("Tahoma", 12), foreground = "black", width = 5)
        self.comb_configuraciones.current(0)
        self.comb_configuraciones.grid( row=2, column = 0, padx=10, pady=20,columnspan=2)

        self.SERVBAN = BooleanVar(); self.TJCOMM = BooleanVar(); self.ED = BooleanVar(); self.MVB = BooleanVar()
        self.TAE = BooleanVar(); self.P_LINEA = BooleanVar(); self.VBCINE = BooleanVar() ; self.GC = BooleanVar()

        self.TODOS = BooleanVar()
        self.check_TODOS = Checkbutton(self.ventana1_1, text= "Todos", bg=fondo, fg=letra,selectcolor=color_check,variable= self.TODOS, onvalue=True, offvalue=False, command=self.funcion2)
        self.check_TODOS.grid(row=3,column=0,padx=10, columnspan=2)
        self.check_TODOS.select()

        self.frame_base = Frame(self.ventana1_1, bg=fondo)
        self.frame_base.grid(row=4,column=0,padx=10,columnspan=2)

        self.check_servban = Checkbutton(self.frame_base, text= "ServBan", bg=fondo, fg=letra,selectcolor=color_check, variable= self.SERVBAN, onvalue=True, offvalue=False)
        self.check_servban.grid(row=4,column=0,padx=10, sticky="w")

        self.check_tae = Checkbutton(self.frame_base, text= "TAE", bg=fondo, fg=letra,selectcolor=color_check,variable= self.TAE, onvalue=True, offvalue=False)
        self.check_tae.grid(row=4,column=1,padx=10,sticky="w")

        self.check_tjcomm = Checkbutton(self.frame_base, text= "TJCOMM",bg=fondo, fg=letra,selectcolor=color_check, variable= self.TJCOMM, onvalue=True, offvalue=False)
        self.check_tjcomm.grid(row=5,column=0,padx=10,sticky="w")

        self.check_P_LINEA = Checkbutton(self.frame_base, text= "P_LINEA", bg=fondo, fg=letra,selectcolor=color_check, variable= self.P_LINEA, onvalue=True, offvalue=False)
        self.check_P_LINEA.grid(row=5,column=1,padx=10,sticky="w")

        self.check_ED = Checkbutton(self.frame_base, text= "ED", bg=fondo, fg=letra,selectcolor=color_check, variable= self.ED, onvalue=True, offvalue=False)
        self.check_ED.grid(row=6,column=0,padx=10,sticky="w")

        self.check_VBCINE = Checkbutton(self.frame_base, text= "VBCINE", bg=fondo, fg=letra,selectcolor=color_check, variable= self.VBCINE, onvalue=True, offvalue=False)
        self.check_VBCINE.grid(row=6,column=1,padx=10,sticky="w")

        self.check_MVB = Checkbutton(self.frame_base, text= "MVB", bg=fondo, fg=letra,selectcolor=color_check, variable= self.MVB, onvalue=True, offvalue=False)
        self.check_MVB.grid(row=7,column=0,padx=10,sticky="w")

        self.check_GC = Checkbutton(self.frame_base, text= "GC", bg=fondo, fg=letra,selectcolor=color_check, variable= self.GC, onvalue=True, offvalue=False)
        self.check_GC.grid(row=7,column=1,padx=10,sticky="w")

        boton_1 = Button(self.ventana1_1, text="Direccionar", fg="black",activeforeground='white',activebackground='black',font=("Semi Bold",10),bg="white",cursor='hand2',command=self.funcion_configurar)
        boton_1.grid(row=8,column=0,columnspan=2,padx=10, pady=20)

        self.check_servban.select() ; self.check_tae.select() ; self.check_tjcomm.select() ; self.check_P_LINEA.select()
        self.check_ED.select() ; self.check_VBCINE.select() ; self.check_MVB.select() ; self.check_GC.select()

        self.ventana1_1.bind("<Return>",self.funcion1)

        # ---------------------- Deteccion de fallos -------------------------- #
        """
        style = ttk.Style()
        style.configure("Treeview", fg="white")
        style.map("Treeview", background=[("selected","#38022D")])

        self.tabla = ttk.Treeview(frame1, height=20)
        self.tabla["columns"] = ("Caracteristica","Estado","Descripción")
        self.tabla.column("#0",width=0,stretch=NO)
        self.tabla.column("Caracteristica",anchor=CENTER,width=100)
        self.tabla.column("Estado",anchor=CENTER,width=100)
        self.tabla.column("Descripción",anchor=CENTER,width=300)

        self.tabla.heading("#0",text="",anchor=CENTER)
        self.tabla.heading("Caracteristica",text="Caracteristica",anchor=CENTER)
        self.tabla.heading("Estado",text="Estado",anchor=CENTER)
        self.tabla.heading("Descripción",text="Descripción",anchor=CENTER)

        self.tabla.grid(row=0,column=0,sticky="nw",padx=10)

        self.tabla.tag_configure('error', background='red')
        self.tabla.tag_configure("correcto", background="green")

        #self.detectar_error_ip()
        """
    
#///////////---------------Funciones--------------//////////////////////////////
    def cargar_database(self):
        decision=messagebox.askquestion("Atención","Esta opción descarga un archivo de la nube en la ruta del script para tener las IP más actualizadas, solo se realiza si no estas en punto de venta y si tienes conexión a internet. ¿Cumples las condiciones?")
        if decision == "yes":
            self.mongo=MongoDB('admin','701562')
            self.mongo.descargar_DB()
            messagebox.showinfo('Database copiada','Se creo un archivo json con las IP más actualizadas. Copia el script junto al json, o en su defecto la carpeta Monroy')

    def funcion1(self):
        self.funcion_configurar()

    def funcion1_2(self):
        self.funcion_configurar_2()

    def funcion2(self):
        if self.TODOS.get() == True:
            self.check_servban.select() ; self.check_tae.select() ; self.check_tjcomm.select() ; self.check_P_LINEA.select()
            self.check_ED.select() ; self.check_VBCINE.select() ; self.check_MVB.select() ; self.check_GC.select()
        else:
            self.check_servban.deselect() ; self.check_tae.deselect() ; self.check_tjcomm.deselect() ; self.check_P_LINEA.deselect()
            self.check_ED.deselect() ; self.check_VBCINE.deselect() ; self.check_MVB.deselect() ; self.check_GC.deselect()

    def funcion2_2(self):
        if self.TODOS_2.get() == True:
            self.check_servban_2.select() ; self.check_tae_2.select() ; self.check_tjcomm_2.select() ; self.check_P_LINEA_2.select()
            self.check_ED_2.select() ; self.check_VBCINE_2.select() ; self.check_MVB_2.select() ; self.check_GC_2.select()
        else:
            self.check_servban_2.deselect() ; self.check_tae_2.deselect() ; self.check_tjcomm_2.deselect() ; self.check_P_LINEA_2.deselect()
            self.check_ED_2.deselect() ; self.check_VBCINE_2.deselect() ; self.check_MVB_2.deselect() ; self.check_GC_2.deselect()
    
    def ruta_computadora(self):
        self.ruta = filedialog.askdirectory()
        if self.ruta != '':
            self.mostrar_ventana1()

    def funcion_configurar(self):
        llamar_manage = Manage()
        lista_claves = list()
        tipo_ambiente = self.comb_configuraciones.get()
        
        if self.SERVBAN.get() == True:
            lista_claves.append('VENTA/SERVBAN.INI')
        if self.TAE.get() == True:
            lista_claves.append('XPOS/SubSystems/TAE/TAE.ini')
        if self.TJCOMM.get() == True:
            lista_claves.append('VENTA/TJCOMM.INI')
        if self.P_LINEA.get() == True:
            lista_claves.append('VENTA/P_LINEA.INI')

        if self.ED.get() == True:
            lista_claves.append('ED/EDConfig.XML')
        if self.VBCINE.get() == True:
            lista_claves.append('VENTA/PLN/VBCINE.XML')
        if self.MVB.get() == True:
            lista_claves.append('MVB/MVB.INI')
            lista_claves.append('MVB/CADENAMVB.INI')
        if self.GC.get() == True:
            lista_claves.append('GC/GcAConfig.INI')
            lista_claves.append('GC/GCConfig.INI')

        llamar_manage.direccionamiento_online(tipo_ambiente,lista_claves,self.ruta)
        messagebox.showinfo("Completado","Configuración terminada")
        self.window.destroy()

    # FUNCION PARA CONFIGURACION DE LA VENTANA 2 #
    def funcion_configurar_2(self):
        llamar_manage = Manage()
        lista_claves = list()
        tipo_ambiente = self.comb_configuraciones_2.get()

        if self.SERVBAN_2.get() == True:
            lista_claves.append('VENTA/SERVBAN.INI')
        if self.TAE_2.get() == True:
            lista_claves.append('XPOS/SubSystems/TAE/TAE.ini')
        if self.TJCOMM_2.get() == True:
            lista_claves.append('VENTA/TJCOMM.INI')
        if self.P_LINEA_2.get() == True:
            lista_claves.append('VENTA/P_LINEA.INI')

        if self.ED_2.get() == True:
            lista_claves.append('ED/EDConfig.XML')
        if self.VBCINE_2.get() == True:
            lista_claves.append('VENTA/PLN/VBCINE.XML')
        if self.MVB_2.get() == True:
            lista_claves.append('MVB/MVB.INI')
            lista_claves.append('MVB/CADENAMVB.INI')
        if self.GC_2.get() == True:
            lista_claves.append('GC/GcAConfig.INI')
            lista_claves.append('GC/GCConfig.INI')

        direccionar = llamar_manage.direccionamiento_offline_json(tipo_ambiente,lista_claves)
        if direccionar == False:
            question = messagebox.askquestion('Error','Archivo json no encontrado, se te recomienda pasar el archivo json junto al script. ¿Deseas usar las direcciones del código? FECHA DE LAS DIRECCIONES EN CÓDIGO: 10/08/2022')
            if question == 'yes':
                llamar_manage.direccionamiento_offline(tipo_ambiente,lista_claves)
                messagebox.showinfo('Completado','Configuración terminada')
                self.window.destroy()
        else:
            messagebox.showinfo('Completado','Configuración terminada')
            self.window.destroy()
    
    #Verifica si la ip escrita en el host es igual a la del dispositivo
    """
    def detectar_error_ip(self):
        ip = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ip.connect(("8.8.8.8", 80))
        ip_completa = ip.getsockname()[0]

        objeto = Buscar()
        llamada = objeto.detectar_ip_en_host(f"C:/XPOS/hosts1","storeserver", ip_completa)
        if llamada == True:
            self.tabla.insert(parent="",index="end", text="", values=("Ip en HOST","Correcto","Ip del host correponde a la del dispositivo"),tags=("correcto",))
        else:
            self.tabla.insert(parent="",index="end", text="", values=("Ip en HOST","Error",llamada),tags=("error",))

    def corregir_ip(self):
        ip = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ip.connect(("8.8.8.8", 80))
        ip_completa = ip.getsockname()[0]

        objeto = Buscar()
        objeto.cambiar_ip_host(f"C:/Windows/System32/drivers/etc/hosts","storeserver", ip_completa)"""

if __name__ =="__main__":   
    window= Tk()
    iniciar_sesion=Login(window,"Direccionamiento")
    window.mainloop()