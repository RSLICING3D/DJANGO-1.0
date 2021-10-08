import mysql.connector
import paho.mqtt.client as mqttClient
from LecturaPulso.views import *

imp = ""
var = Clientes(imp)
aser = "database_" + var
user = aser.lower()

h = 0
while 1:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="SqlAdmin",
        database=user
    )

    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Holis aqui ando")
            global Connected  # Use global variable
            Connected = True  # Signal connection
        else:
            print("Connection failed")


    def on_message2(client, userdata, message):
        var2 = int(message.payload)
        print(var2)
        if var2 == 1:
            client.disconnect()
        else:
            pass


    def on_message(client, userdata, message):
        global h
        mycursor = mydb.cursor()
        var1 = message.payload
        mycursor.execute("INSERT INTO database_corriente (estado) VALUES (%(message.payload)s)", {'message.payload': message.payload})
        mydb.commit()

        if h == 6:
            h = 0
            client.disconnect()
            print("Final: "+str(h))

        elif var1 == 0:
            h = h + 1
            print(h)


    Connected = False  # global variable for the state of the connection

    # ////////////////////BROKER MQTT/////////////////////////////////////

    broker_address = "172.20.108.25"  # Broker address
    port = 1883  # Broker port
    user = "Rene"  # Connection username
    password = "643092"  # Connection password

    client = mqttClient.Client("Python00"+var)  # create new instance
    client.username_pw_set(user, password=password)  # set username and password
    client.on_connect = on_connect  # attach function to callback
    client.on_message = on_message2  # attach function to callback
    client.connect(broker_address, port, 60)  # connect
    client.subscribe("arranque")  # subscribe
    client.loop_forever()  # then keep listening forever

    client = mqttClient.Client("Python2"+var)  # create new instance
    client.username_pw_set(user, password=password)  # set username and password
    client.on_connect = on_connect  # attach function to callback
    client.on_message = on_message  # attach function to callback
    client.connect(broker_address, port, 60)  # connect
    client.subscribe("corriente")  # subscribe
    client.loop_forever()  # then keep listening forever
