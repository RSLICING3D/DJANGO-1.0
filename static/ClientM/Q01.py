import mysql.connector
import paho.mqtt.client as mqttClient
from LecturaPulso.views import *

imp = ""
var = Clientes(imp)
aser = "database_" + var
user = aser.lower()

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SqlAdmin",
    database=user
)

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected  # Use global variable
        Connected = True  # Signal connection
    else:
        print("Connection failed")


def on_message(client, userdata, message):
    mycursor = mydb.cursor()
    mycursor.execute("INSERT INTO database_q01 (estado) VALUES (%(message.payload)s)",{'message.payload': message.payload})
    mydb.commit()


Connected = False  # global variable for the state of the connection

# ////////////////////BROKER MQTT/////////////////////////////////////

broker_address = "172.20.108.25"  # Broker address
port = 1883  # Broker port
user = "Rene"  # Connection username
password = "643092"  # Connection password

client = mqttClient.Client("Python4"+user)  # create new instance
client.username_pw_set(user, password=password)  # set username and password
client.on_connect = on_connect  # attach function to callback
client.on_message = on_message  # attach function to callback
client.connect(broker_address, port, 60)  # connect
client.subscribe("Q01")  # subscribe
client.loop_forever()  # then keep listening forever