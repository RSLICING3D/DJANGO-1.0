from datetime import datetime

import matplotlib.pyplot as plt
import paho.mqtt.client as mqttClient
import pymysql

from dateutil import parser
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from threading import Thread
from .forms import CreateUserForm

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import bcrypt
import subprocess

mydb = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin')

global imp


@csrf_protect
def index(request):
    return render(request, 'index.html')


def contact(request):
    if request.method == 'POST':
        asunto = request.POST.get("asunto")
        correo = request.POST.get("correo")
        mensaje = request.POST.get("mensaje")

        print(asunto, correo, mensaje)

        msg = MIMEMultipart()

        message = mensaje + " : " + correo

        # setup the parameters of the message
        password = "hvksorlrbfdupgau"
        msg['From'] = "rene.c.j83@gmail.com"
        msg['To'] = 'ingenieria6@dedutel.com'
        msg['Subject'] = asunto

        # add in the message body
        msg.attach(MIMEText(message, 'plain'))

        # create server
        server = smtplib.SMTP('smtp.gmail.com: 587')

        server.starttls()

        # Login Credentials for sending the mail
        server.login(msg['From'], password)

        # send the message via the server.
        server.sendmail(msg['From'], msg['To'], msg.as_string())

        server.quit()

        print("successfully sent email to %s:" % (msg['To']))
    return render(request, 'contact.html', )


def dashboard(request):
    global Pulso, Pulso0, Pulso01, Pulso02, voltaje, corriente, Q00, Q01, Q02, Q03, Q04, Q05, Q06, Q07, Q08, \
        Q09, imp, ultimo, primer, num, Pulso1

    imp = Clientes(username)

    user = imp
    print(user)

    # Autorun

    def client_0():
        import static.ClientM.Corriente

    def client_1():
        import static.ClientM.Presion

    def client_2():
        import static.ClientM.Q00

    def client_3():
        import static.ClientM.Q01

    def client_4():
        import static.ClientM.Q02

    def client_5():
        import static.ClientM.Q03

    def client_6():
        import static.ClientM.Q04

    def client_7():
        import static.ClientM.Q05

    def client_8():
        import static.ClientM.Q06

    def client_9():
        import static.ClientM.Q07

    def client_10():
        import static.ClientM.Q08

    def client_11():
        import static.ClientM.Q09

    def client_12():
        import static.ClientM.Voltaje

    threads = []
    threads.append(Thread(target=client_0))
    threads.append(Thread(target=client_1))
    threads.append(Thread(target=client_2))
    threads.append(Thread(target=client_3))
    threads.append(Thread(target=client_4))
    threads.append(Thread(target=client_5))
    threads.append(Thread(target=client_6))
    threads.append(Thread(target=client_7))
    threads.append(Thread(target=client_8))
    threads.append(Thread(target=client_9))
    threads.append(Thread(target=client_10))
    threads.append(Thread(target=client_11))
    threads.append(Thread(target=client_12))
    for thread in threads:
        thread.start()

    # Indicador Presion

    miConexion = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion.cursor()
    cur.execute("SELECT estado FROM database_buton;")
    for estado in cur.fetchall():
        Pulso = estado[0]
    # Indicador Voltaje

    miConexion3 = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion3.cursor()
    cur.execute("SELECT estado FROM database_voltaje;")
    for estado in cur.fetchall():
        voltaje = estado[0]
    miConexion3.commit()

    # Indicador Corriente

    miConexion6 = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion6.cursor()
    cur.execute("SELECT estado FROM database_corriente;")
    for estado in cur.fetchall():
        corriente = estado[0]
    miConexion6.commit()

    # Graficas

    miConexion4 = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion4.cursor()
    cur.execute("SELECT fecha, estado FROM database_buton ORDER BY id DESC LIMIT 1047;")
    data = cur.fetchall()

    dates = []
    values = []

    for row in data:
        dates.append(parser.parse(str(row[0])))
        values.append(row[1])

    plt.figure(figsize=(5, 4))
    plt.plot_date(dates, values, '-')
    plt.title('Presion')
    plt.ylabel("Presion (Psi)")
    plt.xlabel("Tiempo (hr)")
    plt.grid()
    plt.savefig('F:/Proyectos Django/asd/static/media/GraphicPresion.png')
    miConexion4.commit()

    miConexion5 = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion5.cursor()
    cur.execute("SELECT fecha, estado FROM database_voltaje ORDER BY id DESC LIMIT 120;")

    data1 = cur.fetchall()

    dates1 = []
    values1 = []

    for row in data1:
        dates1.append(parser.parse(str(row[0])))
        values1.append(row[1])

    plt.figure(figsize=(5, 4))
    plt.plot_date(dates1, values1, '-')
    plt.title('Voltaje')
    plt.ylabel("Voltaje (V)")
    plt.xlabel("Tiempo (hr)")
    plt.grid()
    plt.savefig('F:/Proyectos Django/asd/static/media/GraphicVoltage.png')
    miConexion5.commit()

    miConexion7 = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion7.cursor()
    cur.execute("SELECT id, estado FROM database_corriente WHERE estado = 0 order by id LIMIT 80000;")
    for estado in cur.fetchall():
        Pulso = list(estado)
    Pulso21 = []
    cur.execute("SELECT id FROM database_corriente WHERE estado = 0 order by id LIMIT 80000;")
    for estado in cur.fetchall():
        Pulso12 = list(estado)
        Pulso11 = estado[0]
        Pulso21.append(Pulso11)
    print(Pulso21)
    _2Pulso = len(Pulso21)
    _1Pulso = _2Pulso - 1
    _3Pulso = _2Pulso - 2
    print(_3Pulso)
    _5Pulso = Pulso21[_1Pulso]
    _4Pulso = Pulso21[_3Pulso]
    print(_4Pulso)
    a = _5Pulso - _4Pulso
    print(a, _5Pulso, _4Pulso)
    cur.execute("SELECT fecha, estado FROM database_corriente ORDER BY id DESC LIMIT %(a)s", {'a': a})

    data2 = cur.fetchall()

    dates2 = []
    values2 = []

    for row in data2:
        dates2.append(parser.parse(str(row[0])))
        values2.append(row[1])

    plt.figure(figsize=(6, 4))
    plt.plot_date(dates2, values2, '-')
    plt.title('Corriente')
    plt.ylabel("Corriente (A)")
    plt.xlabel("Tiempo (hr)")
    plt.grid()
    plt.savefig('F:/Proyectos Django/asd/static/media/GraphicCorriente.png')
    miConexion7.commit()

    # Indicadores LEDs

    miConexion8 = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion8.cursor()
    cur.execute("SELECT estado FROM database_Q00;")
    for estado in cur.fetchall():
        Q00 = estado[0]
    miConexion8.commit()

    miConexion9 = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion9.cursor()
    cur.execute("SELECT estado FROM database_Q01;")
    for estado in cur.fetchall():
        Q01 = estado[0]
    miConexion9.commit()

    miConexion10 = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion10.cursor()
    cur.execute("SELECT estado FROM database_Q02;")
    for estado in cur.fetchall():
        Q02 = estado[0]
    miConexion10.commit()

    miConexion11 = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion11.cursor()
    cur.execute("SELECT estado FROM database_Q03;")
    for estado in cur.fetchall():
        Q03 = estado[0]
    miConexion11.commit()

    miConexion12 = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion12.cursor()
    cur.execute("SELECT estado FROM database_Q04;")
    for estado in cur.fetchall():
        Q04 = estado[0]
    miConexion12.commit()

    miConexion13 = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion13.cursor()
    cur.execute("SELECT estado FROM database_Q05;")
    for estado in cur.fetchall():
        Q05 = estado[0]
    miConexion13.commit()

    miConexion14 = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion14.cursor()
    cur.execute("SELECT estado FROM database_Q06;")
    for estado in cur.fetchall():
        Q06 = estado[0]
    miConexion14.commit()

    miConexion15 = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion15.cursor()
    cur.execute("SELECT estado FROM database_Q07;")
    for estado in cur.fetchall():
        Q07 = estado[0]
    miConexion15.commit()

    miConexion16 = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion16.cursor()
    cur.execute("SELECT estado FROM database_Q08;")
    for estado in cur.fetchall():
        Q08 = estado[0]
    miConexion16.commit()

    miConexion17 = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion17.cursor()
    cur.execute("SELECT estado FROM database_Q09;")
    for estado in cur.fetchall():
        Q09 = estado[0]
    miConexion17.commit()

    plt.switch_backend('agg')

    # Vaciado de tablas

    miConexion20 = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion20.cursor()
    cur.execute("SELECT id FROM database_buton;")
    for estado in cur.fetchall():
        Pulso0 = estado[0]

    cur.execute("SELECT id FROM database_voltaje;")
    for estado in cur.fetchall():
        Pulso01 = estado[0]

    cur.execute("SELECT id FROM database_corriente;")
    for estado in cur.fetchall():
        Pulso02 = estado[0]
    miConexion20.commit()

    return render(request, "Pulso.html", context={}, )


def Encender(request):
    global Pulso1, imp
    topic = "compresor_on"

    imp = Clientes(username)

    user = imp

    # Graficas

    miConexion4 = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion4.cursor()
    cur.execute("SELECT fecha, estado FROM database_buton ORDER BY id DESC LIMIT 1047;")
    data = cur.fetchall()

    dates = []
    values = []

    for row in data:
        dates.append(parser.parse(str(row[0])))
        values.append(row[1])

    plt.figure(figsize=(5, 4))
    plt.plot_date(dates, values, '-')
    plt.title('Presion')
    plt.ylabel("Presion (Psi)")
    plt.xlabel("Tiempo (hr)")
    plt.grid()
    plt.savefig('F:/Proyectos Django/asd/static/media/GraphicPresion.png')
    miConexion4.commit()

    miConexion5 = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion5.cursor()
    cur.execute("SELECT fecha, estado FROM database_voltaje ORDER BY id DESC LIMIT 120;")

    data1 = cur.fetchall()

    dates1 = []
    values1 = []

    for row in data1:
        dates1.append(parser.parse(str(row[0])))
        values1.append(row[1])

    plt.figure(figsize=(5, 4))
    plt.plot_date(dates1, values1, '-')
    plt.title('Voltaje')
    plt.ylabel("Voltaje (V)")
    plt.xlabel("Tiempo (hr)")
    plt.grid()
    plt.savefig('F:/Proyectos Django/asd/static/media/GraphicVoltage.png')
    miConexion5.commit()

    miConexion7 = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion7.cursor()
    cur.execute("SELECT id, estado FROM database_corriente WHERE estado = 0 order by id LIMIT 80000;")
    for estado in cur.fetchall():
        Pulso = list(estado)
    Pulso21 = []
    cur.execute("SELECT id FROM database_corriente WHERE estado = 0 order by id LIMIT 80000;")
    for estado in cur.fetchall():
        Pulso12 = list(estado)
        Pulso11 = estado[0]
        Pulso21.append(Pulso11)
    print(Pulso21)
    _2Pulso = len(Pulso21)
    _1Pulso = _2Pulso - 1
    _3Pulso = _2Pulso - 2
    print(_3Pulso)
    _5Pulso = Pulso21[_1Pulso]
    _4Pulso = Pulso21[_3Pulso]
    print(_4Pulso)
    a = _5Pulso - _4Pulso
    print(a, _5Pulso, _4Pulso)
    cur.execute("SELECT fecha, estado FROM database_corriente ORDER BY id DESC LIMIT %(a)s", {'a': a})

    data2 = cur.fetchall()

    dates2 = []
    values2 = []

    for row in data2:
        dates2.append(parser.parse(str(row[0])))
        values2.append(row[1])

    plt.figure(figsize=(6, 4))
    plt.plot_date(dates2, values2, '-')
    plt.title('Corriente')
    plt.ylabel("Corriente (A)")
    plt.xlabel("Tiempo (hr)")
    plt.grid()
    plt.savefig('F:/Proyectos Django/asd/static/media/GraphicCorriente.png')
    miConexion7.commit()

    miConexion3 = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion3.cursor()
    cur.execute("INSERT INTO database_led0 (estado) VALUES (1);")
    cur.execute("SELECT estado FROM database_led0;")
    for estado1 in cur.fetchall():
        Pulso1 = estado1[0]
    miConexion3.commit()
    # ////////////////////BROKER MQTT/////////////////////////////////////
    broker_address = "172.20.108.25"  # Broker address
    port = 1883  # Broker port
    user = "Miranda"  # Connection username
    password = "643092"  # Connection password

    client = mqttClient.Client(client_id="Django")  # create new instance
    client.username_pw_set(user, password=password)  # set username and password
    client.connect(broker_address, port, 60)  # connect
    client.publish(topic, Pulso1, qos=2, retain=bool(0), properties=None)
    client.loop_start()  # then keep listening forever

    return render(request, "Pulso.html", )


def Apagar(request):
    global Pulso1, imp
    topic = "compresor_on"

    imp = Clientes(username)

    user = imp

    # Graficas

    miConexion4 = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion4.cursor()
    cur.execute("SELECT fecha, estado FROM database_buton ORDER BY id DESC LIMIT 1047;")
    data = cur.fetchall()

    dates = []
    values = []

    for row in data:
        dates.append(parser.parse(str(row[0])))
        values.append(row[1])

    plt.figure(figsize=(5, 4))
    plt.plot_date(dates, values, '-')
    plt.title('Presion')
    plt.ylabel("Presion (Psi)")
    plt.xlabel("Tiempo (hr)")
    plt.grid()
    plt.savefig('F:/Proyectos Django/asd/static/media/GraphicPresion.png')
    miConexion4.commit()

    miConexion5 = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion5.cursor()
    cur.execute("SELECT fecha, estado FROM database_voltaje ORDER BY id DESC LIMIT 120;")

    data1 = cur.fetchall()

    dates1 = []
    values1 = []

    for row in data1:
        dates1.append(parser.parse(str(row[0])))
        values1.append(row[1])

    plt.figure(figsize=(5, 4))
    plt.plot_date(dates1, values1, '-')
    plt.title('Voltaje')
    plt.ylabel("Voltaje (V)")
    plt.xlabel("Tiempo (hr)")
    plt.grid()
    plt.savefig('F:/Proyectos Django/asd/static/media/GraphicVoltage.png')
    miConexion5.commit()

    miConexion7 = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion7.cursor()
    cur.execute("SELECT id, estado FROM database_corriente WHERE estado = 0 order by id LIMIT 80000;")
    for estado in cur.fetchall():
        Pulso = list(estado)
    Pulso21 = []
    cur.execute("SELECT id FROM database_corriente WHERE estado = 0 order by id LIMIT 80000;")
    for estado in cur.fetchall():
        Pulso12 = list(estado)
        Pulso11 = estado[0]
        Pulso21.append(Pulso11)
    print(Pulso21)
    _2Pulso = len(Pulso21)
    _1Pulso = _2Pulso - 1
    _3Pulso = _2Pulso - 2
    print(_3Pulso)
    _5Pulso = Pulso21[_1Pulso]
    _4Pulso = Pulso21[_3Pulso]
    print(_4Pulso)
    a = _5Pulso - _4Pulso
    print(a, _5Pulso, _4Pulso)
    cur.execute("SELECT fecha, estado FROM database_corriente ORDER BY id DESC LIMIT %(a)s", {'a': a})

    data2 = cur.fetchall()

    dates2 = []
    values2 = []

    for row in data2:
        dates2.append(parser.parse(str(row[0])))
        values2.append(row[1])

    plt.figure(figsize=(6, 4))
    plt.plot_date(dates2, values2, '-')
    plt.title('Corriente')
    plt.ylabel("Corriente (A)")
    plt.xlabel("Tiempo (hr)")
    plt.grid()
    plt.savefig('F:/Proyectos Django/asd/static/media/GraphicCorriente.png')
    miConexion7.commit()

    miConexion2 = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion2.cursor()
    cur.execute("INSERT INTO database_led0 (estado) VALUES (0);")
    cur.execute("SELECT estado FROM database_led0;")
    for estado1 in cur.fetchall():
        Pulso1 = estado1[0]
    miConexion2.commit()

    # ////////////////////BROKER MQTT/////////////////////////////////////
    broker_address = "172.20.108.25"  # Broker address
    port = 1883  # Broker port
    user = "Miranda"  # Connection username
    password = "643092"  # Connection password

    client = mqttClient.Client(client_id="Django")  # create new instance
    client.username_pw_set(user, password=password)  # set username and password
    client.connect(broker_address, port, 60)  # connect
    client.publish(topic, Pulso1, qos=2, retain=bool(0), properties=None)
    client.loop_start()  # then keep listening forever

    return render(request, "Pulso.html", )


def Encender1(request):
    global Pulso1, imp, Pulso
    topic = "led1"

    imp = Clientes(username)

    user = imp

    # Graficas

    miConexion4 = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion4.cursor()
    cur.execute("SELECT fecha, estado FROM database_buton ORDER BY id DESC LIMIT 1047;")
    data = cur.fetchall()

    dates = []
    values = []

    for row in data:
        dates.append(parser.parse(str(row[0])))
        values.append(row[1])

    plt.figure(figsize=(5, 4))
    plt.plot_date(dates, values, '-')
    plt.title('Presion')
    plt.ylabel("Presion (Psi)")
    plt.xlabel("Tiempo (hr)")
    plt.grid()
    plt.savefig('F:/Proyectos Django/asd/static/media/GraphicPresion.png')
    miConexion4.commit()

    miConexion5 = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion5.cursor()
    cur.execute("SELECT fecha, estado FROM database_voltaje ORDER BY id DESC LIMIT 120;")

    data1 = cur.fetchall()

    dates1 = []
    values1 = []

    for row in data1:
        dates1.append(parser.parse(str(row[0])))
        values1.append(row[1])

    plt.figure(figsize=(5, 4))
    plt.plot_date(dates1, values1, '-')
    plt.title('Voltaje')
    plt.ylabel("Voltaje (V)")
    plt.xlabel("Tiempo (hr)")
    plt.grid()
    plt.savefig('F:/Proyectos Django/asd/static/media/GraphicVoltage.png')
    miConexion5.commit()

    miConexion7 = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion7.cursor()
    cur.execute("SELECT id, estado FROM database_corriente WHERE estado = 0 order by id LIMIT 80000;")
    for estado in cur.fetchall():
        Pulso = list(estado)
    Pulso21 = []
    cur.execute("SELECT id FROM database_corriente WHERE estado = 0 order by id LIMIT 80000;")
    for estado in cur.fetchall():
        Pulso12 = list(estado)
        Pulso11 = estado[0]
        Pulso21.append(Pulso11)
    print(Pulso21)
    _2Pulso = len(Pulso21)
    _1Pulso = _2Pulso - 1
    _3Pulso = _2Pulso - 2
    print(_3Pulso)
    _5Pulso = Pulso21[_1Pulso]
    _4Pulso = Pulso21[_3Pulso]
    print(_4Pulso)
    a = _5Pulso - _4Pulso
    print(a, _5Pulso, _4Pulso)
    cur.execute("SELECT fecha, estado FROM database_corriente ORDER BY id DESC LIMIT %(a)s", {'a': a})

    data2 = cur.fetchall()

    dates2 = []
    values2 = []

    for row in data2:
        dates2.append(parser.parse(str(row[0])))
        values2.append(row[1])

    plt.figure(figsize=(6, 4))
    plt.plot_date(dates2, values2, '-')
    plt.title('Corriente')
    plt.ylabel("Corriente (A)")
    plt.xlabel("Tiempo (hr)")
    plt.grid()
    plt.savefig('F:/Proyectos Django/asd/static/media/GraphicCorriente.png')
    miConexion7.commit()

    miConexion2 = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion2.cursor()
    cur.execute("INSERT INTO database_led1 (estado) VALUES (1);")
    cur.execute("SELECT estado FROM database_led1;")
    for estado1 in cur.fetchall():
        Pulso1 = estado1[0]
    miConexion2.commit()
    # ////////////////////BROKER MQTT/////////////////////////////////////
    broker_address = "172.20.108.25"  # Broker address
    port = 1883  # Broker port
    user = "Miranda"  # Connection username
    password = "643092"  # Connection password

    client = mqttClient.Client(client_id="Django")  # create new instance
    client.username_pw_set(user, password=password)  # set username and password
    client.connect(broker_address, port, 60)  # connect
    client.publish(topic, Pulso1, qos=2, retain=bool(0), properties=None)
    client.loop_start()  # then keep listening forever

    return render(request, "Pulso.html", context={'Text2': Pulso, 'Text3': voltaje}, )


def Apagar1(request):
    global Pulso1, imp
    topic = "led1"

    imp = Clientes(username)
    user = imp

    # Graficas

    miConexion4 = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion4.cursor()
    cur.execute("SELECT fecha, estado FROM database_buton ORDER BY id DESC LIMIT 100;")
    data = cur.fetchall()

    dates = []
    values = []

    for row in data:
        dates.append(parser.parse(str(row[0])))
        values.append(row[1])

    plt.figure(figsize=(5, 4))
    plt.plot_date(dates, values, '-')
    plt.title('Presion')
    plt.ylabel("Presion (Psi)")
    plt.xlabel("Tiempo (hr)")
    plt.grid()
    plt.savefig('F:/Proyectos Django/asd/static/media/GraphicPresion.png')
    miConexion4.commit()

    miConexion5 = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion5.cursor()
    cur.execute("SELECT fecha, estado FROM database_voltaje ORDER BY id DESC LIMIT 120;")

    data1 = cur.fetchall()

    dates1 = []
    values1 = []

    for row in data1:
        dates1.append(parser.parse(str(row[0])))
        values1.append(row[1])

    plt.figure(figsize=(5, 4))
    plt.plot_date(dates1, values1, '-')
    plt.title('Voltaje')
    plt.ylabel("Voltaje (V)")
    plt.xlabel("Tiempo (hr)")
    plt.grid()
    plt.savefig('F:/Proyectos Django/asd/static/media/GraphicVoltage.png')
    miConexion5.commit()

    miConexion7 = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion7.cursor()
    cur.execute("SELECT id, estado FROM database_corriente WHERE estado = 0 order by id LIMIT 80000;")
    for estado in cur.fetchall():
        Pulso = list(estado)
    Pulso21 = []
    cur.execute("SELECT id FROM database_corriente WHERE estado = 0 order by id LIMIT 80000;")
    for estado in cur.fetchall():
        Pulso12 = list(estado)
        Pulso11 = estado[0]
        Pulso21.append(Pulso11)
    print(Pulso21)
    _2Pulso = len(Pulso21)
    _1Pulso = _2Pulso - 1
    _3Pulso = _2Pulso - 2
    print(_3Pulso)
    _5Pulso = Pulso21[_1Pulso]
    _4Pulso = Pulso21[_3Pulso]
    print(_4Pulso)
    a = _5Pulso - _4Pulso
    print(a, _5Pulso, _4Pulso)
    cur.execute("SELECT fecha, estado FROM database_corriente ORDER BY id DESC LIMIT %(a)s", {'a': a})

    data2 = cur.fetchall()

    dates2 = []
    values2 = []

    for row in data2:
        dates2.append(parser.parse(str(row[0])))
        values2.append(row[1])

    plt.figure(figsize=(6, 4))
    plt.plot_date(dates2, values2, '-')
    plt.title('Corriente')
    plt.ylabel("Corriente (A)")
    plt.xlabel("Tiempo (hr)")
    plt.grid()
    plt.savefig('F:/Proyectos Django/asd/static/media/GraphicCorriente.png')
    miConexion7.commit()

    miConexion2 = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion2.cursor()
    cur.execute("INSERT INTO database_led1 (estado) VALUES (0);")
    cur.execute("SELECT estado FROM database_led1;")
    for estado1 in cur.fetchall():
        Pulso1 = estado1[0]
    miConexion2.commit()
    # ////////////////////BROKER MQTT/////////////////////////////////////
    broker_address = "172.20.108.25"  # Broker address
    port = 1883  # Broker port
    user = "Miranda"  # Connection username
    password = "643092"  # Connection password

    client = mqttClient.Client(client_id="Django")  # create new instance
    client.username_pw_set(user, password=password)  # set username and password
    client.connect(broker_address, port, 60)  # connect
    client.publish(topic, Pulso1, qos=2, retain=bool(0), properties=None)
    client.loop_start()  # then keep listening forever

    return render(request, "Pulso.html", )


def Encender2(request):
    global Pulso1, imp
    topic = "led2"

    imp = Clientes(username)
    user = imp

    miConexion2 = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion2.cursor()
    cur.execute("INSERT INTO database_led2 (estado) VALUES (1);")
    cur.execute("SELECT estado FROM database_led2;")
    for estado1 in cur.fetchall():
        Pulso1 = estado1[0]
    miConexion2.commit()
    # ////////////////////BROKER MQTT/////////////////////////////////////
    broker_address = "172.20.108.25"  # Broker address
    port = 1883  # Broker port
    user = "Miranda"  # Connection username
    password = "643092"  # Connection password

    client = mqttClient.Client(client_id="Django")  # create new instance
    client.username_pw_set(user, password=password)  # set username and password
    client.connect(broker_address, port, 60)  # connect
    client.publish(topic, Pulso1, qos=2, retain=bool(0), properties=None)
    client.loop_start()  # then keep listening forever

    return render(request, "Pulso.html", )


def Apagar2(request):
    global Pulso1, imp
    topic = "led2"

    imp = Clientes(username)
    user = imp

    miConexion2 = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion2.cursor()
    cur.execute("INSERT INTO database_led2 (estado) VALUES (0);")
    cur.execute("SELECT estado FROM database_led2;")
    for estado1 in cur.fetchall():
        Pulso1 = estado1[0]
    miConexion2.commit()
    # ////////////////////BROKER MQTT/////////////////////////////////////
    broker_address = "172.20.108.25"  # Broker address
    port = 1883  # Broker port
    user = "Miranda"  # Connection username
    password = "643092"  # Connection password

    client = mqttClient.Client(client_id="Django")  # create new instance
    client.username_pw_set(user, password=password)  # set username and password
    client.connect(broker_address, port, 60)  # connect
    client.publish(topic, Pulso1, qos=2, retain=bool(0), properties=None)
    client.loop_start()  # then keep listening forever

    return render(request, "Pulso.html", )


def Encender3(request):
    global Pulso1, imp
    topic = "led3"

    imp = Clientes(username)
    user = imp

    miConexion2 = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion2.cursor()
    cur.execute("INSERT INTO database_led3 (estado) VALUES (1);")
    cur.execute("SELECT estado FROM database_led3;")
    for estado1 in cur.fetchall():
        Pulso1 = estado1[0]
    miConexion2.commit()
    # ////////////////////BROKER MQTT/////////////////////////////////////
    broker_address = "172.20.108.25"  # Broker address
    port = 1883  # Broker port
    user = "Miranda"  # Connection username
    password = "643092"  # Connection password

    client = mqttClient.Client(client_id="Django")  # create new instance
    client.username_pw_set(user, password=password)  # set username and password
    client.connect(broker_address, port, 60)  # connect
    client.publish(topic, Pulso1, qos=2, retain=bool(0), properties=None)
    client.loop_start()  # then keep listening forever

    return render(request, "Pulso.html")


def Apagar3(request):
    global Pulso1, imp
    topic = "led3"

    imp = Clientes(username)
    user = imp

    miConexion2 = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion2.cursor()
    cur.execute("INSERT INTO database_led3 (estado) VALUES (0);")
    cur.execute("SELECT estado FROM database_led3;")
    for estado1 in cur.fetchall():
        Pulso1 = estado1[0]
    miConexion2.commit()
    # ////////////////////BROKER MQTT/////////////////////////////////////
    broker_address = "172.20.108.25"  # Broker address
    port = 1883  # Broker port
    user = "Miranda"  # Connection username
    password = "643092"  # Connection password

    client = mqttClient.Client(client_id="Django")  # create new instance
    client.username_pw_set(user, password=password)  # set username and password
    client.connect(broker_address, port, 60)  # connect
    client.publish(topic, Pulso1, qos=2, retain=bool(0), properties=None)
    client.loop_start()  # then keep listening forever

    return render(request, "Pulso.html", )


def Encender4(request):
    global Pulso1, imp
    topic = "led4"

    imp = Clientes(username)
    user = imp

    miConexion2 = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion2.cursor()
    cur.execute("INSERT INTO database_led4 (estado) VALUES (1);")
    cur.execute("SELECT estado FROM database_led4;")
    for estado1 in cur.fetchall():
        Pulso1 = estado1[0]
    miConexion2.commit()
    # ////////////////////BROKER MQTT/////////////////////////////////////
    broker_address = "172.20.108.25"  # Broker address
    port = 1883  # Broker port
    user = "Miranda"  # Connection username
    password = "643092"  # Connection password

    client = mqttClient.Client(client_id="Django")  # create new instance
    client.username_pw_set(user, password=password)  # set username and password
    client.connect(broker_address, port, 60)  # connect
    client.publish(topic, Pulso1, qos=2, retain=bool(0), properties=None)
    client.loop_start()  # then keep listening forever

    return render(request, "Pulso.html", )


def Apagar4(request):
    global Pulso1, imp
    topic = "led4"

    imp = Clientes(username)
    user = imp

    miConexion2 = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion2.cursor()
    cur.execute("INSERT INTO database_led4 (estado) VALUES (0);")
    cur.execute("SELECT estado FROM database_led4;")
    for estado1 in cur.fetchall():
        Pulso1 = estado1[0]
    miConexion2.commit()
    # ////////////////////BROKER MQTT/////////////////////////////////////
    broker_address = "172.20.108.25"  # Broker address
    port = 1883  # Broker port
    user = "Miranda"  # Connection username
    password = "643092"  # Connection password

    client = mqttClient.Client(client_id="Django")  # create new instance
    client.username_pw_set(user, password=password)  # set username and password
    client.connect(broker_address, port, 60)  # connect
    client.publish(topic, Pulso1, qos=2, retain=bool(0), properties=None)
    client.loop_start()  # then keep listening forever

    return render(request, "Pulso.html", )


def Encender5(request):
    global Pulso1, imp
    topic = "led5"

    imp = Clientes(username)
    user = imp

    miConexion2 = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion2.cursor()
    cur.execute("INSERT INTO database_led5 (estado) VALUES (1);")
    cur.execute("SELECT estado FROM database_led5;")
    for estado1 in cur.fetchall():
        Pulso1 = estado1[0]
    miConexion2.commit()
    # ////////////////////BROKER MQTT/////////////////////////////////////
    broker_address = "172.20.108.25"  # Broker address
    port = 1883  # Broker port
    user = "Miranda"  # Connection username
    password = "643092"  # Connection password

    client = mqttClient.Client(client_id="Django")  # create new instance
    client.username_pw_set(user, password=password)  # set username and password
    client.connect(broker_address, port, 60)  # connect
    client.publish(topic, Pulso1, qos=2, retain=bool(0), properties=None)
    client.loop_start()  # then keep listening forever

    return render(request, "Pulso.html", )


def Apagar5(request):
    global Pulso1, imp
    topic = "led5"

    imp = Clientes(username)
    user = imp

    miConexion2 = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion2.cursor()
    cur.execute("INSERT INTO database_led5 (estado) VALUES (0);")
    cur.execute("SELECT estado FROM database_led5;")
    for estado1 in cur.fetchall():
        Pulso1 = estado1[0]
    miConexion2.commit()
    # ////////////////////BROKER MQTT/////////////////////////////////////
    broker_address = "172.20.108.25"  # Broker address
    port = 1883  # Broker port
    user = "Miranda"  # Connection username
    password = "643092"  # Connection password

    client = mqttClient.Client(client_id="Django")  # create new instance
    client.username_pw_set(user, password=password)  # set username and password
    client.connect(broker_address, port, 60)  # connect
    client.publish(topic, Pulso1, qos=2, retain=bool(0), properties=None)
    client.loop_start()  # then keep listening forever

    return render(request, "Pulso.html", )


def Encender6(request):
    global Pulso1, imp
    topic = "led6"

    imp = Clientes(username)
    user = imp

    miConexion2 = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion2.cursor()
    cur.execute("INSERT INTO database_led6 (estado) VALUES (1);")
    cur.execute("SELECT estado FROM database_led6;")
    for estado1 in cur.fetchall():
        Pulso1 = estado1[0]
    miConexion2.commit()
    # ////////////////////BROKER MQTT/////////////////////////////////////
    broker_address = "172.20.108.25"  # Broker address
    port = 1883  # Broker port
    user = "Miranda"  # Connection username
    password = "643092"  # Connection password

    client = mqttClient.Client(client_id="Django")  # create new instance
    client.username_pw_set(user, password=password)  # set username and password
    client.connect(broker_address, port, 60)  # connect
    client.publish(topic, Pulso1, qos=2, retain=bool(0), properties=None)
    client.loop_start()  # then keep listening forever

    return render(request, "Pulso.html", )


def Apagar6(request):
    global Pulso1, imp
    topic = "led6"

    imp = Clientes(username)
    user = imp

    miConexion2 = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion2.cursor()
    cur.execute("INSERT INTO database_led6 (estado) VALUES (0);")
    cur.execute("SELECT estado FROM database_led6;")
    for estado1 in cur.fetchall():
        Pulso1 = estado1[0]
    miConexion2.commit()
    # ////////////////////BROKER MQTT/////////////////////////////////////
    broker_address = "172.20.108.25"  # Broker address
    port = 1883  # Broker port
    user = "Miranda"  # Connection username
    password = "643092"  # Connection password

    client = mqttClient.Client(client_id="Django")  # create new instance
    client.username_pw_set(user, password=password)  # set username and password
    client.connect(broker_address, port, 60)  # connect
    client.publish(topic, Pulso1, qos=2, retain=bool(0), properties=None)
    client.loop_start()  # then keep listening forever

    return render(request, "Pulso.html", )


def Encender7(request):
    global Pulso1, imp
    topic = "led7"

    imp = Clientes(username)
    user = imp

    miConexion2 = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion2.cursor()
    cur.execute("INSERT INTO database_led7 (estado) VALUES (1);")
    cur.execute("SELECT estado FROM database_led7;")
    for estado1 in cur.fetchall():
        Pulso1 = estado1[0]
    miConexion2.commit()
    # ////////////////////BROKER MQTT/////////////////////////////////////
    broker_address = "172.20.108.25"  # Broker address
    port = 1883  # Broker port
    user = "Miranda"  # Connection username
    password = "643092"  # Connection password

    client = mqttClient.Client(client_id="Django")  # create new instance
    client.username_pw_set(user, password=password)  # set username and password
    client.connect(broker_address, port, 60)  # connect
    client.publish(topic, Pulso1, qos=2, retain=bool(0), properties=None)
    client.loop_start()  # then keep listening forever

    return render(request, "Pulso.html", )


def Apagar7(request):
    global Pulso1, imp
    topic = "led7"

    imp = Clientes(username)
    user = imp

    miConexion2 = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion2.cursor()
    cur.execute("INSERT INTO database_led7 (estado) VALUES (0);")
    cur.execute("SELECT estado FROM database_led7;")
    for estado1 in cur.fetchall():
        Pulso1 = estado1[0]
    miConexion2.commit()
    # ////////////////////BROKER MQTT/////////////////////////////////////
    broker_address = "172.20.108.25"  # Broker address
    port = 1883  # Broker port
    user = "Miranda"  # Connection username
    password = "643092"  # Connection password

    client = mqttClient.Client(client_id="Django")  # create new instance
    client.username_pw_set(user, password=password)  # set username and password
    client.connect(broker_address, port, 60)  # connect
    client.publish(topic, Pulso1, qos=2, retain=bool(0), properties=None)
    client.loop_start()  # then keep listening forever

    return render(request, "Pulso.html", )


def Encender00(request):
    global Pulso1, imp
    topic = "salida1.0"

    imp = Clientes(username)
    user = imp

    miConexion2 = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion2.cursor()
    cur.execute("INSERT INTO database_led00 (estado) VALUES (1);")
    cur.execute("SELECT estado FROM database_led00;")
    for estado1 in cur.fetchall():
        Pulso1 = estado1[0]
    miConexion2.commit()
    # ////////////////////BROKER MQTT/////////////////////////////////////
    broker_address = "172.20.108.25"  # Broker address
    port = 1883  # Broker port
    user = "Miranda"  # Connection username
    password = "643092"  # Connection password

    client = mqttClient.Client(client_id="Django")  # create new instance
    client.username_pw_set(user, password=password)  # set username and password
    client.connect(broker_address, port, 60)  # connect
    client.publish(topic, Pulso1, qos=2, retain=bool(0), properties=None)
    client.loop_start()  # then keep listening forever

    return render(request, "Pulso.html", )


def Apagar00(request):
    global Pulso1, imp
    topic = "salida1.0"

    imp = Clientes(username)
    user = imp

    miConexion2 = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion2.cursor()
    cur.execute("INSERT INTO database_led00 (estado) VALUES (0);")
    cur.execute("SELECT estado FROM database_led00;")
    for estado1 in cur.fetchall():
        Pulso1 = estado1[0]
    miConexion2.commit()
    # ////////////////////BROKER MQTT/////////////////////////////////////
    broker_address = "172.20.108.25"  # Broker address
    port = 1883  # Broker port
    user = "Miranda"  # Connection username
    password = "643092"  # Connection password

    client = mqttClient.Client(client_id="Django")  # create new instance
    client.username_pw_set(user, password=password)  # set username and password
    client.connect(broker_address, port, 60)  # connect
    client.publish(topic, Pulso1, qos=2, retain=bool(0), properties=None)
    client.loop_start()  # then keep listening forever

    return render(request, "Pulso.html", )


def Encender01(request):
    global Pulso1, imp
    topic = "salida1.1"

    imp = Clientes(username)
    user = imp

    miConexion2 = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion2.cursor()
    cur.execute("INSERT INTO database_led01 (estado) VALUES (1);")
    cur.execute("SELECT estado FROM database_led01;")
    for estado1 in cur.fetchall():
        Pulso1 = estado1[0]
    miConexion2.commit()
    # ////////////////////BROKER MQTT/////////////////////////////////////
    broker_address = "172.20.108.25"  # Broker address
    port = 1883  # Broker port
    user = "Miranda"  # Connection username
    password = "643092"  # Connection password

    client = mqttClient.Client(client_id="Django")  # create new instance
    client.username_pw_set(user, password=password)  # set username and password
    client.connect(broker_address, port, 60)  # connect
    client.publish(topic, Pulso1, qos=2, retain=bool(0), properties=None)
    client.loop_start()  # then keep listening forever

    return render(request, "Pulso.html", )


def Apagar01(request):
    global Pulso1, imp
    topic = "salida1.1"

    imp = Clientes(username)
    user = imp

    miConexion2 = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion2.cursor()
    cur.execute("INSERT INTO database_led01 (estado) VALUES (0);")
    cur.execute("SELECT estado FROM database_led01;")
    for estado1 in cur.fetchall():
        Pulso1 = estado1[0]
    miConexion2.commit()
    # ////////////////////BROKER MQTT/////////////////////////////////////
    broker_address = "172.20.108.25"  # Broker address
    port = 1883  # Broker port
    user = "Miranda"  # Connection username
    password = "643092"  # Connection password

    client = mqttClient.Client(client_id="Django")  # create new instance
    client.username_pw_set(user, password=password)  # set username and password
    client.connect(broker_address, port, 60)  # connect
    client.publish(topic, Pulso1, qos=2, retain=bool(0), properties=None)
    client.loop_start()  # then keep listening forever

    return render(request, "Pulso.html", )


def Message(request):
    global Pulso1, imp
    topic = "texto"

    imp = Clientes(username)
    user = imp

    message = request.POST.get("tipo_de_dato")

    miConexion2 = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion2.cursor()
    cur.execute("INSERT INTO database_texto (Mensaje) VALUES(%(message)s)", {'message': message})
    cur.execute("SELECT Mensaje FROM database_texto;")
    for estado1 in cur.fetchall():
        Pulso1 = estado1[0]
    miConexion2.commit()
    # ////////////////////BROKER MQTT/////////////////////////////////////
    broker_address = "172.20.108.25"  # Broker address
    port = 1883  # Broker port
    user = "Miranda"  # Connection username
    password = "643092"  # Connection password

    client = mqttClient.Client(client_id="Django")  # create new instance
    client.username_pw_set(user, password=password)  # set username and password
    client.connect(broker_address, port, 60)  # connect
    client.publish(topic, Pulso1, qos=2, retain=bool(0), properties=None)
    client.loop_start()  # then keep listening forever

    return render(request, "Pulso.html", )


def Int00(request):
    global Pulso1, imp
    topic = "Int00"

    imp = Clientes(username)
    user = imp

    message = request.POST.get("tipo_de_dato_int0")

    miConexion2 = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion2.cursor()
    cur.execute("INSERT INTO database_texto (Mensaje) VALUES(%(message)s)", {'message': message})
    cur.execute("SELECT Mensaje FROM database_Int00;")
    for estado1 in cur.fetchall():
        Pulso1 = estado1[0]
    miConexion2.commit()
    # ////////////////////BROKER MQTT/////////////////////////////////////
    broker_address = "172.20.108.25"  # Broker address
    port = 1883  # Broker port
    user = "Miranda"  # Connection username
    password = "643092"  # Connection password

    client = mqttClient.Client(client_id="Django")  # create new instance
    client.username_pw_set(user, password=password)  # set username and password
    client.connect(broker_address, port, 60)  # connect
    client.publish(topic, Pulso1, qos=2, retain=bool(0), properties=None)
    client.loop_start()  # then keep listening forever

    return render(request, "Pulso.html", )


def Int01(request):
    global Pulso1, imp
    topic = "Int01"

    imp = Clientes(username)
    user = imp

    message = request.POST.get("tipo_de_dato_int1")

    miConexion2 = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion2.cursor()
    cur.execute("INSERT INTO database_texto (Mensaje) VALUES(%(message)s)", {'message': message})
    cur.execute("SELECT Mensaje FROM database_Int01;")
    for estado1 in cur.fetchall():
        Pulso1 = estado1[0]
    miConexion2.commit()
    # ////////////////////BROKER MQTT/////////////////////////////////////
    broker_address = "172.20.108.25"  # Broker address
    port = 1883  # Broker port
    user = "Miranda"  # Connection username
    password = "643092"  # Connection password

    client = mqttClient.Client(client_id="Django")  # create new instance
    client.username_pw_set(user, password=password)  # set username and password
    client.connect(broker_address, port, 60)  # connect
    client.publish(topic, Pulso1, qos=2, retain=bool(0), properties=None)
    client.loop_start()  # then keep listening forever

    return render(request, "Pulso.html", )


def Int02(request):
    global Pulso1, imp
    topic = "Int02"

    imp = Clientes(username)
    user = imp

    message = request.POST.get("tipo_de_dato_int2")

    miConexion2 = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion2.cursor()
    cur.execute("INSERT INTO database_texto (Mensaje) VALUES(%(message)s)", {'message': message})
    cur.execute("SELECT Mensaje FROM database_Int02;")
    for estado1 in cur.fetchall():
        Pulso1 = estado1[0]
    miConexion2.commit()
    # ////////////////////BROKER MQTT/////////////////////////////////////
    broker_address = "172.20.108.25"  # Broker address
    port = 1883  # Broker port
    user = "Miranda"  # Connection username
    password = "643092"  # Connection password

    client = mqttClient.Client(client_id="Django")  # create new instance
    client.username_pw_set(user, password=password)  # set username and password
    client.connect(broker_address, port, 60)  # connect
    client.publish(topic, Pulso1, qos=2, retain=bool(0), properties=None)
    client.loop_start()  # then keep listening forever

    return render(request, "Pulso.html")


def Int03(request):
    global Pulso1, imp
    topic = "Int03"

    imp = Clientes(username)
    user = imp

    message = request.POST.get("tipo_de_dato_int3")

    miConexion2 = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion2.cursor()
    cur.execute("INSERT INTO database_texto (Mensaje) VALUES(%(message)s)", {'message': message})
    cur.execute("SELECT Mensaje FROM database_Int03;")
    for estado1 in cur.fetchall():
        Pulso1 = estado1[0]
    miConexion2.commit()
    # ////////////////////BROKER MQTT/////////////////////////////////////
    broker_address = "172.20.108.25"  # Broker address
    port = 1883  # Broker port
    user = "Miranda"  # Connection username
    password = "643092"  # Connection password

    client = mqttClient.Client(client_id="Django")  # create new instance
    client.username_pw_set(user, password=password)  # set username and password
    client.connect(broker_address, port, 60)  # connect
    client.publish(topic, Pulso1, qos=2, retain=bool(0), properties=None)
    client.loop_start()  # then keep listening forever

    return render(request, "Pulso.html", )


def Int04(request):
    global Pulso1, imp
    topic = "Int04"

    imp = Clientes(username)
    user = imp

    message = request.POST.get("tipo_de_dato_int4")

    miConexion2 = pymysql.connect(host='localhost', user='root', passwd='SqlAdmin', db='database_' + user)
    cur = miConexion2.cursor()
    cur.execute("INSERT INTO database_texto (Mensaje) VALUES(%(message)s)", {'message': message})
    cur.execute("SELECT Mensaje FROM database_Int04;")
    for estado1 in cur.fetchall():
        Pulso1 = estado1[0]
    miConexion2.commit()
    # ////////////////////BROKER MQTT/////////////////////////////////////
    broker_address = "172.20.108.25"  # Broker address
    port = 1883  # Broker port
    user = "Miranda"  # Connection username
    password = "643092"  # Connection password

    client = mqttClient.Client(client_id="Django")  # create new instance
    client.username_pw_set(user, password=password)  # set username and password
    client.connect(broker_address, port, 60)  # connect
    client.publish(topic, Pulso1, qos=2, retain=bool(0), properties=None)
    client.loop_start()  # then keep listening forever

    return render(request, "Pulso.html", )


def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Cuenta creada para ' + user)
            cur = mydb.cursor()
            cur.execute("CREATE DATABASE IF NOT EXISTS database_" + user)
            cur.execute("USE database_" + user)
            cur.execute(
                "CREATE TABLE IF NOT EXISTS database_buton(id INT PRIMARY KEY AUTO_INCREMENT, estado INT, fecha datetime default current_timestamp on update current_timestamp);")
            cur.execute("INSERT INTO database_buton (estado) VALUES (0);")
            cur.execute(
                "CREATE TABLE IF NOT EXISTS database_texto(id INT PRIMARY KEY AUTO_INCREMENT, Mensaje char(20), fecha datetime default current_timestamp on update current_timestamp);")
            cur.execute("INSERT INTO database_texto (Mensaje) VALUES (0);")
            cur.execute(
                "CREATE TABLE IF NOT EXISTS database_corriente(id INT PRIMARY KEY AUTO_INCREMENT, estado INT, fecha datetime default current_timestamp on update current_timestamp);")
            cur.execute("INSERT INTO database_corriente (estado) VALUES (0);")
            cur.execute(
                "CREATE TABLE IF NOT EXISTS database_voltaje(id INT PRIMARY KEY AUTO_INCREMENT, estado INT, fecha datetime default current_timestamp on update current_timestamp);")
            cur.execute("INSERT INTO database_voltaje (estado) VALUES (0);")
            cur.execute(
                "CREATE TABLE IF NOT EXISTS database_led0(id INT PRIMARY KEY AUTO_INCREMENT, estado INT, fecha datetime default current_timestamp on update current_timestamp );")
            cur.execute("INSERT INTO database_led0 (estado) VALUES (0);")
            cur.execute(
                "CREATE TABLE IF NOT EXISTS database_led1(id INT PRIMARY KEY AUTO_INCREMENT, estado INT, fecha datetime default current_timestamp on update current_timestamp );")
            cur.execute("INSERT INTO database_led1 (estado) VALUES (0);")
            cur.execute(
                "CREATE TABLE IF NOT EXISTS database_led2(id INT PRIMARY KEY AUTO_INCREMENT, estado INT, fecha datetime default current_timestamp on update current_timestamp );")
            cur.execute("INSERT INTO database_led2 (estado) VALUES (0);")
            cur.execute(
                "CREATE TABLE IF NOT EXISTS database_led3(id INT PRIMARY KEY AUTO_INCREMENT, estado INT, fecha datetime default current_timestamp on update current_timestamp );")
            cur.execute("INSERT INTO database_led3 (estado) VALUES (0);")
            cur.execute(
                "CREATE TABLE IF NOT EXISTS database_led4(id INT PRIMARY KEY AUTO_INCREMENT, estado INT, fecha datetime default current_timestamp on update current_timestamp );")
            cur.execute("INSERT INTO database_led4 (estado) VALUES (0);")
            cur.execute(
                "CREATE TABLE IF NOT EXISTS database_led5(id INT PRIMARY KEY AUTO_INCREMENT, estado INT, fecha datetime default current_timestamp on update current_timestamp );")
            cur.execute("INSERT INTO database_led5 (estado) VALUES (0);")
            cur.execute(
                "CREATE TABLE IF NOT EXISTS database_led6(id INT PRIMARY KEY AUTO_INCREMENT, estado INT, fecha datetime default current_timestamp on update current_timestamp );")
            cur.execute("INSERT INTO database_led6(estado) VALUES (0);")
            cur.execute(
                "CREATE TABLE IF NOT EXISTS database_led7(id INT PRIMARY KEY AUTO_INCREMENT, estado INT, fecha datetime default current_timestamp on update current_timestamp );")
            cur.execute("INSERT INTO database_led7 (estado) VALUES (0);")
            cur.execute(
                "CREATE TABLE IF NOT EXISTS database_led00(id INT PRIMARY KEY AUTO_INCREMENT, estado INT, fecha datetime default current_timestamp on update current_timestamp );")
            cur.execute("INSERT INTO database_led00 (estado) VALUES (0);")
            cur.execute(
                "CREATE TABLE IF NOT EXISTS database_led01(id INT PRIMARY KEY AUTO_INCREMENT, estado INT, fecha datetime default current_timestamp on update current_timestamp );")
            cur.execute("INSERT INTO database_led01(estado) VALUES (0);")
            cur.execute(
                "CREATE TABLE IF NOT EXISTS database_int00(id INT PRIMARY KEY AUTO_INCREMENT, Mensaje char(20), fecha datetime default current_timestamp on update current_timestamp );")
            cur.execute("INSERT INTO database_int00 (Mensaje) VALUES (0);")
            cur.execute(
                "CREATE TABLE IF NOT EXISTS database_int01(id INT PRIMARY KEY AUTO_INCREMENT, Mensaje char(20), fecha datetime default current_timestamp on update current_timestamp );")
            cur.execute("INSERT INTO database_int01 (Mensaje) VALUES (0);")
            cur.execute(
                "CREATE TABLE IF NOT EXISTS database_int02(id INT PRIMARY KEY AUTO_INCREMENT, Mensaje char(20), fecha datetime default current_timestamp on update current_timestamp );")
            cur.execute("INSERT INTO database_int02 (Mensaje) VALUES (0);")
            cur.execute(
                "CREATE TABLE IF NOT EXISTS database_int03(id INT PRIMARY KEY AUTO_INCREMENT, Mensaje char(20), fecha datetime default current_timestamp on update current_timestamp );")
            cur.execute("INSERT INTO database_int03 (Mensaje) VALUES (0);")
            cur.execute(
                "CREATE TABLE IF NOT EXISTS database_int04(id INT PRIMARY KEY AUTO_INCREMENT, Mensaje char(20), fecha datetime default current_timestamp on update current_timestamp );")
            cur.execute("INSERT INTO database_int04 (Mensaje) VALUES (0);")
            cur.execute(
                "CREATE TABLE IF NOT EXISTS database_Q00(id INT PRIMARY KEY AUTO_INCREMENT, estado INT, fecha datetime default current_timestamp on update current_timestamp );")
            cur.execute("INSERT INTO database_Q00 (estado) VALUES (0);")
            cur.execute(
                "CREATE TABLE IF NOT EXISTS database_Q01(id INT PRIMARY KEY AUTO_INCREMENT, estado INT, fecha datetime default current_timestamp on update current_timestamp );")
            cur.execute("INSERT INTO database_Q01 (estado) VALUES (0);")
            cur.execute(
                "CREATE TABLE IF NOT EXISTS database_Q02(id INT PRIMARY KEY AUTO_INCREMENT, estado INT, fecha datetime default current_timestamp on update current_timestamp );")
            cur.execute("INSERT INTO database_Q02 (estado) VALUES (0);")
            cur.execute(
                "CREATE TABLE IF NOT EXISTS database_Q03(id INT PRIMARY KEY AUTO_INCREMENT, estado INT, fecha datetime default current_timestamp on update current_timestamp );")
            cur.execute("INSERT INTO database_Q03 (estado) VALUES (0);")
            cur.execute(
                "CREATE TABLE IF NOT EXISTS database_Q04(id INT PRIMARY KEY AUTO_INCREMENT, estado INT, fecha datetime default current_timestamp on update current_timestamp );")
            cur.execute("INSERT INTO database_Q04 (estado) VALUES (0);")
            cur.execute(
                "CREATE TABLE IF NOT EXISTS database_Q05(id INT PRIMARY KEY AUTO_INCREMENT, estado INT, fecha datetime default current_timestamp on update current_timestamp );")
            cur.execute("INSERT INTO database_Q05 (estado) VALUES (0);")
            cur.execute(
                "CREATE TABLE IF NOT EXISTS database_Q06(id INT PRIMARY KEY AUTO_INCREMENT, estado INT, fecha datetime default current_timestamp on update current_timestamp );")
            cur.execute("INSERT INTO database_Q06 (estado) VALUES (0);")
            cur.execute(
                "CREATE TABLE IF NOT EXISTS database_Q07(id INT PRIMARY KEY AUTO_INCREMENT, estado INT, fecha datetime default current_timestamp on update current_timestamp );")
            cur.execute("INSERT INTO database_Q07 (estado) VALUES (0);")
            cur.execute(
                "CREATE TABLE IF NOT EXISTS database_Q08(id INT PRIMARY KEY AUTO_INCREMENT, estado INT, fecha datetime default current_timestamp on update current_timestamp );")
            cur.execute("INSERT INTO database_Q08 (estado) VALUES (0);")
            cur.execute(
                "CREATE TABLE IF NOT EXISTS database_Q09(id INT PRIMARY KEY AUTO_INCREMENT, estado INT, fecha datetime default current_timestamp on update current_timestamp );")
            mydb.commit()
            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)


def loginPage(request):
    global username, user
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'redirect.html', )
        else:
            messages.info(request, 'Usuario o contraseña incorrecta')

    context = {}
    return render(request, 'login.html', context, )


def logoutUser(request):
    logout(request)
    stop_threads = True

    return redirect('login')


username = ""


def Clientes(imp):
    imp = username
    return imp