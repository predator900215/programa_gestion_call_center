import os.path
from tkinter import Tk, Button, Label, Entry, END, Toplevel, StringVar, OptionMenu, Text

import pyperclip as pyperclip
from PIL import ImageTk, Image
import time
import webbrowser
from datetime import datetime
import pytz


def registrar_usuario():
    usuario_registrado = ent_nombre.get()
    clave_registrada = ent_clave.get()
    archivo = open('C:/Users/ADMIN/Desktop/proyectopeya/cache/usuarios.txt', 'a', encoding='utf-8')
    archivo.write('nombre: ' + usuario_registrado + '\n' + 'clave: ' + clave_registrada + '\n')
    archivo.close()

    ent_nombre.delete(0, END)
    ent_clave.delete(0, END)


def verificar_usuario():
    nombre = ent_nombre.get()
    clave = ent_clave.get()

    archivo = open('C:/Users/ADMIN/Desktop/proyectopeya/cache/usuarios.txt', 'r', encoding='utf-8')
    contenido = archivo.read()
    archivo.close()

    if nombre and clave in contenido:
        print('acceso concedido')
        time.sleep(1)
        cerrar_ventana()
        abrir_ventana_2()
    else:
        ent_nombre.delete(0, END)
        ent_clave.delete(0, END)


def cerrar_ventana():
    raiz.destroy()


def abrir_ventana_2():

    def copiar_contenido():
        contenido = cuadronota.get('1.0', 'end-1c')
        pyperclip.copy(contenido)

    def notaox():
        nota1 = 'O.X//'
        cuadronota.insert(END, nota1)

    def notasa():
        nota2 = 'S.A//'
        cuadronota.insert(END, nota2)

    def notanombre():
        nombre = entrada_nombre_rider.get()
        cuadronota.insert(END, '{}//'.format(nombre))

    def notacancelo():
        nota3 = '//cancelo orden'
        cuadronota.insert(END, nota3)

    def notareasigna():
        nota4 = '//reasigno orden'
        cuadronota.insert(END, nota4)

    def notadivido():
        nota5 = '//divido orden'
        cuadronota.insert(END, nota5)

    def notallamoconexito():
        nota6 = '//llamo con exito'
        cuadronota.insert(END, nota6)

    def notallamosinexito():
        nota7 = '//llamo sin exito'
        cuadronota.insert(END, nota7)

    def notareportofallo():
        nota8 = '//reporto fallo de IC'
        cuadronota.insert(END, nota8)

    def notaridersegmentoa():
        nota9 = '//rider segmento A'
        cuadronota.insert(END, nota9)

    def notaridersegmentob():
        nota10 = '//rider segmento B'
        cuadronota.insert(END, nota10)

    def notaenviosolucion():
        nota11 = '//envio solucion '
        cuadronota.insert(END, nota11)

    def notaactivopausa():
        nota12 = '//activo pausa'
        cuadronota.insert(END, nota12)

    def notaretiropausa():
        nota13 = '//retiro pausa'
        cuadronota.insert(END, nota13)

    def notafeedback():
        nota14 = '//realizo feedback'
        cuadronota.insert(END, nota14)

    def notars():
        nota15 = '//RS'
        cuadronota.insert(END, nota15)

    def notalocalcerrado():
        nota16 = 'local cerrado'
        cuadronota.insert(END, nota16)

    def notaproblemascte():
        nota17 = 'problemas con cliente'
        cuadronota.insert(END, nota17)


    def notavehiculo():
        nota18 = 'problemas con vehiculo'
        cuadronota.insert(END, nota18)

    def notaotrorider():
        nota19 = 'orden tomada por otro rider'
        cuadronota.insert(END, nota19)

    def notapedidocancelado():
        nota20 = 'Pedidocancelado'
        cuadronota.insert(END, nota20)

    def notadeliveryinverso():
        nota21 = 'DeliveryInverso'
        cuadronota.insert(END, nota21)

    def quitarespacios():
        numero = entrynumerollamar.get()
        numerosinespacios = numero.replace(" ", "").replace("(", "").replace(")", "")
        entrynumerollamar.delete(0, END)
        x = (entrynumerollamar.insert(END, numerosinespacios))
        return x

    def copiar_telefono():
        telefono = entrynumerollamar.get()
        pyperclip.copy(telefono)

    def segmentacion():
        segmento = entradasegmento.get()

        url3 = 'https://lookerstudio.google.com/u/0/reporting/7d96f4bb-a653-4240-bd71-' \
               'b4e7c2b0bb12/page/p_9sq6spxkxc?params=%7B%22df11%22:%22include%25EE%2580%25801%25EE' \
               '%2580%2580EQ%25EE%2580%2580{}%22%7D'.format(segmento)

        webbrowser.open_new_tab(url3)

    def obtener_pais():
        pais = combo_paises.get()
        if pais in paises:
            if pais == 'Argentina':
                pais = 'ar'
            elif pais == 'Bolivia':
                pais = 'bo'
            elif pais == 'Chile':
                pais = 'cl'
            elif pais == 'Ecuador':
                pais = 'Ec'
            elif pais == 'Paraguay':
                pais = ''
            elif pais == 'Perú':
                pais = 'pe'
            elif pais == 'Uruguay':
                pais = 'uy'
            elif pais == 'Venezuela':
                pais = 've'
            elif pais == 'Costa Rica':
                pais = 'cr'
            elif pais == 'El Salvador':
                pais = 'sv'
            elif pais == 'Guatemala':
                pais = 'gt'
            elif pais == 'Honduras':
                pais = 'hn'
            elif pais == 'Nicaragua':
                pais = 'ni'
            elif pais == 'Panamá':
                pais = 'pa'
            elif pais == 'República Dominicana':
                pais = 'do'
            return pais
        return None

    def abrirhu():
        pais = obtener_pais()

        if pais:
            numeroorden = entrada_numero_orden.get()
            urlhu = 'https://{}.us.logisticsbackoffice.com/dispatcher/order_details/{}'.format(pais, numeroorden)
            webbrowser.open_new_tab(urlhu)

    def abrirbo():
        pais2 = obtener_pais()

        if pais2:
            numero_de_orden = entrada_numero_orden.get()
            urlbo = 'https://backoffice-app.pedidosya.com/#/orders/' + numero_de_orden
            webbrowser.open_new_tab(urlbo)

    def abrirhu2():
        pais2 = obtener_pais()

        if pais2:
            numero_de_orden = entrada_numero_orden.get()
            urlhu2 = 'http://{}.us.logisticsbackoffice.com/dashboard/v2/hurrier/order_details/{}'.format(
                pais2, numero_de_orden)
            webbrowser.open_new_tab(urlhu2)

    def guardar_registro():
        entrada1 = entrada_nombre_rider.get()
        entrada2 = obtener_pais()
        entrada3 = entrada_numero_orden.get()
        entrada4 = entradasegmento.get()
        entrada5 = entrynumerollamar.get()
        entrada6 = cuadronota.get(1.0, END)
        entrada7 = hora_formateada

        archivo = open('C:/Users/ADMIN/Desktop/proyectopeya/cache/registro.txt', 'a', encoding='utf-8')
        archivo.write('\nnombre: ' + entrada1 + '\n' + 'pais: ' + entrada2 + '\n' + 'numero de orden: ' + entrada3 +
                      '\n' + 'id de rider: ' + entrada4 + '\n' + 'numero de llamada: ' + entrada5 + '\n' +
                      'nota de HU : ' + entrada6 + 'hora: ' + entrada7 + '\n' + '------------------------------------')
        archivo.close()

    def copiar_entradanombre():
        nombrecopiado = entrada_nombre_rider.get()
        pyperclip.copy(nombrecopiado)

    def copiar_numeroorden():
        ordencopiada = entrada_numero_orden.get()
        pyperclip.copy(ordencopiada)

    def copiar_segmento():
        segmento = entradasegmento.get()
        pyperclip.copy(segmento)

    def obtener_hora():
        pais = combo_paises.get()
        if pais in paises:
            timezone = pytz.timezone(paises[pais])
            hora_actual = datetime.now(timezone).strftime('%H:%M:%S')
            label_hora.config(text="Hora actual: " + hora_actual)

        nueva_raiz.after(1000, obtener_hora)

    def creartemplate():
        nombretemplate = ent_nombretemplate.get()
        contenido = cuadro_contenidotemplate.get(1.0, 'end-1c')
        with open('C:/Users/ADMIN/Desktop/proyectopeya/cache/{}.txt'.format(nombretemplate), 'a', encoding='utf-8') \
                as archivo:
            archivo.write(contenido)

    def vertemplate():
        nombretemp = ent_nombretemplate.get()
        ruta = 'C:/Users/ADMIN/Desktop/proyectopeya/cache/{}.txt'.format(nombretemp)
        with open(ruta, 'r', encoding='utf8') as archivo:
            contenido = archivo.read()

        cuadro_contenidotemplate.delete('1.0', END)
        cuadro_contenidotemplate.insert(END, contenido)

    def editartemplate():
        nombretem = ent_nombretemplate.get()
        rutatemp = 'C:/Users/ADMIN/Desktop/proyectopeya/cache/{}.txt'.format(nombretem)
        contenidotemp = cuadro_contenidotemplate.get('1.0', END)

        with open(rutatemp, 'w', encoding='utf-8') as archivo:
            archivo.write(contenidotemp)

    def borrartemplate():
        nombreruta = ent_nombretemplate.get()
        ruta_archivo = 'C:/Users/ADMIN/Desktop/proyectopeya/cache/{}.txt'.format(nombreruta)
        if os.path.exists(ruta_archivo):
            os.remove(ruta_archivo)
            print('archivo eliminado exitosamente')
        else:
            print('archivo no existe')

    def copiartemplate():
        contenido = cuadro_contenidotemplate.get('1.0', END)
        pyperclip.copy(contenido)

    def borrar_contenido():
        entrada_nombre_rider.delete(0, END)
        entrada_numero_orden.delete(0, END)
        entradasegmento.delete(0, END)
        entrynumerollamar.delete(0, END)
        cuadronota.delete('1.0', END)

    nueva_raiz = Toplevel()
    nueva_raiz.geometry('1300x450')
    nueva_raiz.config(bg='#FF5555')
    nueva_raiz.title('GESTION DE PROCESOS')
    hora_actual_col = datetime.now()
    formato = "%H:%M:%S - %d/%m"
    hora_formateada = hora_actual_col.strftime(formato)

    imagencopiar = Image.open('C:/Users/ADMIN/Desktop/proyectopeya/imagenes/copiarlogo.png')
    nuevo_ancho2 = 25
    nuevo_alto2 = 25
    imagenredimensionada = imagencopiar.resize((nuevo_ancho2, nuevo_alto2))
    imagen_tk2 = ImageTk.PhotoImage(imagenredimensionada)

    imagenborrar = Image.open('C:/Users/ADMIN/Desktop/proyectopeya/imagenes/borrartodo3.png')
    nuevo_ancho3 = 40
    nuevo_alto3 = 40
    imagenredimensionada2 = imagenborrar.resize((nuevo_ancho3, nuevo_alto3))
    imagen_tk3 = ImageTk.PhotoImage(imagenredimensionada2)

    imagenguardar = Image.open('C:/Users/ADMIN/Desktop/proyectopeya/imagenes/Icono-guardar.png')
    nuevo_ancho4 = 37
    nuevo_alto4 = 37
    imagenredimensionada3 = imagenguardar.resize((nuevo_ancho4, nuevo_alto4))
    imagen_tk4 = ImageTk.PhotoImage(imagenredimensionada3)

    imagenver = Image.open('C:/Users/ADMIN/Desktop/proyectopeya/imagenes/ver.png')
    nuevo_ancho5 = 40
    nuevo_alto5 = 40
    imagenredimensionada3 = imagenver.resize((nuevo_ancho5, nuevo_alto5))
    imagen_tk5 = ImageTk.PhotoImage(imagenredimensionada3)

    imageneditar = Image.open('C:/Users/ADMIN/Desktop/proyectopeya/imagenes/editar.png')
    nuevo_ancho6 = 40
    nuevo_alto6 = 40
    imagenredimensionada3 = imageneditar.resize((nuevo_ancho6, nuevo_alto6))
    imagen_tk6 = ImageTk.PhotoImage(imagenredimensionada3)

    paises = {
        "Argentina": "America/Argentina/Buenos_Aires",
        "Bolivia": "America/La_Paz",
        "Chile": "America/Santiago",
        "Ecuador": "America/Guayaquil",
        "Paraguay": "America/Asuncion",
        "Perú": "America/Lima",
        "Uruguay": "America/Montevideo",
        "Venezuela": "America/Caracas",
        "Costa Rica": "America/Costa_Rica",
        "El Salvador": "America/El_Salvador",
        "Guatemala": "America/Guatemala",
        "Honduras": "America/Tegucigalpa",
        "Nicaragua": "America/Managua",
        "Panamá": "America/Panama",
        "República Dominicana": "America/Santo_Domingo"
    }

    btn_localcerrado = Button(nueva_raiz, text='local cerrado', font=('Arial', 12, 'bold'), command=notalocalcerrado)
    btn_localcerrado.place(x=750, y=260, width=170, height=30)
    btn_problemascte = Button(nueva_raiz, text='problemas cliente', font=('Arial', 12, 'bold'), command=notaproblemascte)
    btn_problemascte.place(x=750, y=290, width=170, height=30)
    btn_vehiculo = Button(nueva_raiz, text='problemas vehiculo', font=('Arial', 12, 'bold'), command=notavehiculo)
    btn_vehiculo.place(x=750, y=320, width=170, height=30)
    btn_otrorider = Button(nueva_raiz, text='otro rider', font=('Arial', 12, 'bold'), command=notaotrorider)
    btn_otrorider.place(x=750, y=350, width=170, height=30)
    btn_pedidocancelado = Button(nueva_raiz, text='PedidoCancelado', font=('Arial', 12, 'bold'),
                                 command=notapedidocancelado)
    btn_pedidocancelado.place(x=930, y=260, width=150, height=30)
    btn_deliveryinverso = Button(nueva_raiz, text='DeliveryInverso', font=('Arial', 12, 'bold'),
                                 command=notadeliveryinverso)
    btn_deliveryinverso.place(x=930, y=290, width=150, height=30)

    btn_borrar = Button(nueva_raiz, image=imagen_tk3, command=borrar_contenido, bg='white')
    btn_borrar.image = imagen_tk3
    btn_borrar.place(x=640, y=20)

    btn_guardar = Button(nueva_raiz, image=imagen_tk4, command=guardar_registro, bg='white')
    btn_guardar.image = imagen_tk4
    btn_guardar.place(x=640, y=80)

    lbl_nombretemplate = Label(nueva_raiz, text='Nombre template', font=('Arial', 12, 'bold'), bg='yellow')
    lbl_nombretemplate.place(x=750, y=20, width=150, height=30)

    ent_nombretemplate = Entry(nueva_raiz, font=('Arial', 12, 'bold'))
    ent_nombretemplate.place(x=910, y=20, width=335, height=30)

    lbl_contenidotemplate = Label(nueva_raiz, text='Contenido', font=('Arial', 12, 'bold'), bg='yellow')
    lbl_contenidotemplate.place(x=750, y=60, width=100, height=30)

    btn_vertemplate = Button(nueva_raiz, image=imagen_tk5, bg='white', command=vertemplate)
    btn_vertemplate.image = imagen_tk5
    btn_vertemplate.place(x=1050, y=60)

    btn_creartemplate = Button(nueva_raiz, image=imagen_tk4, bg='green', command=creartemplate)
    btn_creartemplate.image = imagen_tk4
    btn_creartemplate.place(x=1100, y=60)

    btn_editartemplate = Button(nueva_raiz, image=imagen_tk6, bg='yellow', command=editartemplate)
    btn_editartemplate.image = imagen_tk6
    btn_editartemplate.place(x=1150, y=60)

    btn_borrartemplate = Button(nueva_raiz, image=imagen_tk3, bg='white', command=borrartemplate)
    btn_borrartemplate.image = imagen_tk3
    btn_borrartemplate.place(x=1200, y=60)

    cuadro_contenidotemplate = Text(nueva_raiz, font=('Arial', 12, 'bold'), width=55, height=4)
    cuadro_contenidotemplate.place(x=750, y=110)

    btn_copiarcontenidotemplate = Button(nueva_raiz, image=imagen_tk2, bg='blue', command=copiartemplate)
    btn_copiarcontenidotemplate.image = imagen_tk2
    btn_copiarcontenidotemplate.place(x=1215, y=155)

    lbl_nombre_rider = Label(nueva_raiz, text='Nombre del Rider', font=('Arial', 12, 'bold'), bg='yellow')
    lbl_nombre_rider.place(x=20, y=20, width=150, height=30)

    entrada_nombre_rider = Entry(nueva_raiz, font=('Arial', 12, 'bold'), justify='center')
    entrada_nombre_rider.place(x=180, y=20, width=350, height=30)

    btn_copiar_nombre_rider = Button(nueva_raiz, image=imagen_tk2, font=('Arial', 12, 'bold'), bg='blue',
                                     command=copiar_entradanombre)
    btn_copiar_nombre_rider.image = imagen_tk2
    btn_copiar_nombre_rider.place(x=530, y=20)

    lbl_numero_orden = Label(nueva_raiz, text='No de Orden', font=('Arial', 12, 'bold'), bg='yellow')
    lbl_numero_orden.place(x=20, y=100, width=150, height=30)

    entrada_numero_orden = Entry(nueva_raiz, font=('Arial', 12, 'bold'), justify='center')
    entrada_numero_orden.place(x=180, y=100, width=150, height=30)

    btn_copiar_orden = Button(nueva_raiz, image=imagen_tk2, font=('Arial', 12, 'bold'), bg='blue',
                              command=copiar_numeroorden)
    btn_copiar_nombre_rider.image = imagen_tk2
    btn_copiar_orden.place(x=330, y=100)

    btn_abrir_hu = Button(nueva_raiz, text='HU', font=('Arial', 12, 'bold'), command=abrirhu)
    btn_abrir_hu.place(x=370, y=100, width=40, height=30)

    btn_abrir_bo = Button(nueva_raiz, text='BO', font=('Arial', 12, 'bold'), command=abrirbo)
    btn_abrir_bo.place(x=420, y=100, width=40, height=30)

    btn_abrir_hu2 = Button(nueva_raiz, text='HU2', font=('Arial', 12, 'bold'), command=abrirhu2)
    btn_abrir_hu2.place(x=470, y=100, width=40, height=30)

    lblsegmento = Label(nueva_raiz, text='ID Rider', font=('Arial', 12, 'bold'), bg='yellow')
    lblsegmento.place(x=20, y=140, width=100, height=30)

    entradasegmento = Entry(nueva_raiz, font=('Arial', 12, 'bold'), justify='center')
    entradasegmento.place(x=130, y=140, width=150, height=30)

    btn_copiar_segmento = Button(nueva_raiz, image=imagen_tk2, font=('Arial', 12, 'bold'), bg='blue',
                                 command=copiar_segmento)
    btn_copiar_segmento.image = imagen_tk2
    btn_copiar_segmento.place(x=280, y=140)

    btnsegmento = Button(nueva_raiz, text='Obtener segmento', font=('Arial', 12, 'bold'), command=segmentacion)
    btnsegmento.place(x=320, y=140, width=150, height=30)

    lblnumerollamar = Label(nueva_raiz, text='Telefono', font=('Arial', 12, 'bold'), bg='yellow')
    lblnumerollamar.place(x=20, y=180, width=100, height=30)

    entrynumerollamar = Entry(nueva_raiz, font=('Arial', 12, 'bold'), justify='center')
    entrynumerollamar.place(x=130, y=180, width=200, height=30)

    btn_copiar_telefono = Button(nueva_raiz, image=imagen_tk2, font=('Arial', 12, 'bold'), bg='blue',
                                 command=copiar_telefono)
    btn_copiar_telefono.image = imagen_tk2
    btn_copiar_telefono.place(x=330, y=180)

    btnquitarespacios = Button(nueva_raiz, text='Modificar', font=('Arial', 12, 'bold'), command=quitarespacios)
    btnquitarespacios.place(x=370, y=180, width=100, height=30)

    lblconstruirnota = Label(nueva_raiz, text='Construir Nota', font=('Arial', 12, 'bold'), bg='yellow')
    lblconstruirnota.place(x=20, y=230, width=120, height=30)

    cuadronota = Text(nueva_raiz, width=25, height=8, font=('Arial', 12, 'bold'))
    cuadronota.place(x=20, y=260)

    btn_copiar_cuadronota = Button(nueva_raiz, image=imagen_tk2, font=('Arial', 12, 'bold'), bg='blue',
                                   command=copiar_contenido)
    btn_copiar_cuadronota.image = imagen_tk2
    btn_copiar_cuadronota.place(x=213, y=380)

    # -----------------------------------------------------------------------------------------------------------

    btn_nombre = Button(nueva_raiz, text='Nombre', font=('Arial', 12, 'bold'), command=notanombre)
    btn_nombre.place(x=250, y=260, width=100, height=30)

    btn_ox = Button(nueva_raiz, text='O.X', font=('Arial', 12, 'bold'), command=notaox)
    btn_ox.place(x=250, y=290, width=100, height=30)

    btn_sa = Button(nueva_raiz, text='S.A', font=('Arial', 12, 'bold'), command=notasa)
    btn_sa.place(x=250, y=320, width=100, height=30)

    btn_rs = Button(nueva_raiz, text='RS', font=('Arial', 12, 'bold'), command=notars)
    btn_rs.place(x=250, y=350, width=100, height=30)

    # -----------------------------------------------------------------------------------------------------------

    btn_cancelo = Button(nueva_raiz, text='Cancelo', font=('Arial', 12, 'bold'), command=notacancelo)
    btn_cancelo.place(x=360, y=260, width=100, height=30)

    btn_reasigno = Button(nueva_raiz, text='Reasigno', font=('Arial', 12, 'bold'), command=notareasigna)
    btn_reasigno.place(x=360, y=290, width=100, height=30)

    btn_divido = Button(nueva_raiz, text='Divido', font=('Arial', 12, 'bold'), command=notadivido)
    btn_divido.place(x=360, y=320, width=100, height=30)

    btn_enviosolucion = Button(nueva_raiz, text='Solucion', font=('Arial', 12, 'bold'), command=notaenviosolucion)
    btn_enviosolucion.place(x=360, y=350, width=100, height=30)

    # -----------------------------------------------------------------------------------------------------------

    btn_llamoconexito = Button(nueva_raiz, text='Llamo con Exito', font=('Arial', 12, 'bold'),
                               command=notallamoconexito)
    btn_llamoconexito.place(x=480, y=260, width=150, height=30)

    btn_llamosinexito = Button(nueva_raiz, text='Llamo sin Exito', font=('Arial', 12, 'bold'),
                               command=notallamosinexito)
    btn_llamosinexito.place(x=480, y=290, width=150, height=30)

    btn_reportofallo = Button(nueva_raiz, text='Fallo IC', font=('Arial', 12, 'bold'), command=notareportofallo)
    btn_reportofallo.place(x=480, y=320, width=150, height=30)

    btn_realizofeedback = Button(nueva_raiz, text='Feedback', font=('Arial', 12, 'bold'), command=notafeedback)
    btn_realizofeedback.place(x=480, y=350, width=150, height=30)

    # -----------------------------------------------------------------------------------------------------------

    btn_sega = Button(nueva_raiz, text='Seg A', font=('Arial', 12, 'bold'), command=notaridersegmentoa)
    btn_sega.place(x=640, y=260, width=100, height=30)

    btn_segb = Button(nueva_raiz, text='Seg B', font=('Arial', 12, 'bold'), command=notaridersegmentob)
    btn_segb.place(x=640, y=290, width=100, height=30)

    btn_activopausa = Button(nueva_raiz, text='Act Pausa', font=('Arial', 12, 'bold'), command=notaactivopausa)
    btn_activopausa.place(x=640, y=320, width=100, height=30)

    btn_retiropausa = Button(nueva_raiz, text='Ret Pausa', font=('Arial', 12, 'bold'), command=notaretiropausa)
    btn_retiropausa.place(x=640, y=350, width=100, height=30)

    # menu desplegable paises
    # -------------------------------------------------------------
    lbl_pais = Label(nueva_raiz, text='Pais de la Orden', font=('Arial', 12, 'bold'), bg='yellow')
    lbl_pais.place(x=20, y=60, width=150, height=30)

    combo_paises = StringVar()
    combo = OptionMenu(nueva_raiz, combo_paises, *paises.keys())
    combo.place(x=180, y=60, width=170, height=30)

    label_hora = Label(nueva_raiz, font=('Arial', 12, 'bold'), bg='yellow')
    label_hora.place(x=360, y=60, width=200, height=30)

    obtener_hora()
    # -------------------------------------------------------------


raiz = Tk()
raiz.title('AGENTE RIDER SERVICE')
raiz.geometry('500x450')
raiz.config(bg='#FF5555')

imagen = Image.open('C:/Users/ADMIN/Desktop/proyectopeya/imagenes/logo.jpg')
nuevo_ancho = 450
nuevo_alto = 200
imagen_redimensionada = imagen.resize((nuevo_ancho, nuevo_alto))

imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)
imagen_lbl = Label(raiz, image=imagen_tk)
imagen_lbl.place(x=20, y=20)

lbl_nombre = Label(raiz, text='Nombre', font=('Arial', 12, 'bold'), bg='yellow')
lbl_nombre.place(x=20, y=270, width=100, height=30)

ent_nombre = Entry(raiz, justify='center', font=('Arial', 12, 'bold'))
ent_nombre.place(x=130, y=270, width=350, height=30)

lbl_clave = Label(raiz, text='Clave', font=('Arial', 12, 'bold'), bg='yellow')
lbl_clave.place(x=20, y=310, width=100, height=30)

ent_clave = Entry(raiz, show='*', justify='center', font=('Arial', 12, 'bold'))
ent_clave.place(x=130, y=310, width=350, height=30)

bton_registrar = Button(raiz, text='REGISTRARME', font=('Arial', 12, 'bold'), command=registrar_usuario)
bton_registrar.place(x=130, y=350, width=150, height=30)

bton_ingresar = Button(raiz, text='INGRESAR', font=('Arial', 12, 'bold'), command=verificar_usuario)
bton_ingresar.place(x=330, y=350, width=150, height=30)

raiz.mainloop()
