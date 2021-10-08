import json
import pymysql

from asyncio import sleep
from channels.generic.websocket import AsyncWebsocketConsumer
from itertools import count
from LecturaPulso.views import *


class WSConsumerdashboard(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super(WSConsumerdashboard, self).__init__(*args, **kwargs)
        self.disconnected = True

    async def connect(self):
        global Pulso, voltaje, corriente, Q00, Q01, Q02, Q03, Q04, Q05, Q06, Q07, Q08, Q09

        await self.accept()
        self.disconnected = False  # connected, set flag to False

        imp = ""
        var = Clientes(imp)
        aser = "database_" + var
        user = aser.lower()

        for i in range(1):
            miConexion = pymysql.connect(host='127.0.0.1', user='root', passwd='SqlAdmin', db=user)
            cur = miConexion.cursor()
            cur.execute("INSERT INTO database_Q09 (estado) VALUES (0);")
            cur.execute("SELECT estado FROM database_buton ORDER BY id DESC LIMIT 1")
            for estado0 in cur.fetchall():
                Pulso = estado0[0]
            cur.execute("SELECT estado FROM database_voltaje ORDER BY id DESC LIMIT 1")
            for estado1 in cur.fetchall():
                voltaje = estado1[0]
            cur.execute("SELECT estado FROM database_corriente ORDER BY id DESC LIMIT 1")
            for estado2 in cur.fetchall():
                corriente = estado2[0]
            cur.execute("SELECT estado FROM database_Q00 ORDER BY id DESC LIMIT 1")
            for estado3 in cur.fetchall():
                Q00 = estado3[0]
            cur.execute("SELECT estado FROM database_Q01 ORDER BY id DESC LIMIT 1")
            for estado4 in cur.fetchall():
                Q01 = estado4[0]
            cur.execute("SELECT estado FROM database_Q02 ORDER BY id DESC LIMIT 1")
            for estado5 in cur.fetchall():
                Q02 = estado5[0]
            cur.execute("SELECT estado FROM database_Q03 ORDER BY id DESC LIMIT 1")
            for estado6 in cur.fetchall():
                Q03 = estado6[0]
            cur.execute("SELECT estado FROM database_Q04 ORDER BY id DESC LIMIT 1")
            for estado7 in cur.fetchall():
                Q04 = estado7[0]
            cur.execute("SELECT estado FROM database_Q05 ORDER BY id DESC LIMIT 1")
            for estado8 in cur.fetchall():
                Q05 = estado8[0]
            cur.execute("SELECT estado FROM database_Q06 ORDER BY id DESC LIMIT 1")
            for estado9 in cur.fetchall():
                Q06 = estado9[0]
            cur.execute("SELECT estado FROM database_Q07 ORDER BY id DESC LIMIT 1")
            for estado00 in cur.fetchall():
                Q07 = estado00[0]
            cur.execute("SELECT estado FROM database_Q08 ORDER BY id DESC LIMIT 1")
            for estado01 in cur.fetchall():
                Q08 = estado01[0]
            cur.execute("SELECT estado FROM database_Q09 ORDER BY id DESC LIMIT 1")
            for estado02 in cur.fetchall():
                Q09 = estado02[0]
            cur.execute("SELECT estado FROM database_buton ORDER BY id DESC LIMIT 1;")
            valor = [i[0] for i in cur.fetchall()]
            val = valor[0]
            cur.execute("SELECT fecha FROM database_buton ORDER BY id DESC LIMIT 1;")
            fecha = [i[0] for i in cur.fetchall()]
            fecha2 = str(fecha[0])
            OutputS = [Pulso, voltaje, corriente, Q00, Q01, Q02, Q03, Q04, Q05, Q06, Q07, Q08, Q09, val, fecha2]

            await self.send(json.dumps({'OutputS': OutputS}))
            await sleep(0.001)

        for i in range(29):
            miConexion = pymysql.connect(host='127.0.0.1', user='root', passwd='SqlAdmin', db=user)
            cur = miConexion.cursor()
            cur.execute("SELECT estado FROM database_buton ORDER BY id DESC LIMIT 1")
            for estado0 in cur.fetchall():
                Pulso = estado0[0]
            cur.execute("SELECT estado FROM database_voltaje ORDER BY id DESC LIMIT 1")
            for estado1 in cur.fetchall():
                voltaje = estado1[0]
            cur.execute("SELECT estado FROM database_corriente ORDER BY id DESC LIMIT 1")
            for estado2 in cur.fetchall():
                corriente = estado2[0]
            cur.execute("SELECT estado FROM database_Q00 ORDER BY id DESC LIMIT 1")
            for estado3 in cur.fetchall():
                Q00 = estado3[0]
            cur.execute("SELECT estado FROM database_Q01 ORDER BY id DESC LIMIT 1")
            for estado4 in cur.fetchall():
                Q01 = estado4[0]
            cur.execute("SELECT estado FROM database_Q02 ORDER BY id DESC LIMIT 1")
            for estado5 in cur.fetchall():
                Q02 = estado5[0]
            cur.execute("SELECT estado FROM database_Q03 ORDER BY id DESC LIMIT 1")
            for estado6 in cur.fetchall():
                Q03 = estado6[0]
            cur.execute("SELECT estado FROM database_Q04 ORDER BY id DESC LIMIT 1")
            for estado7 in cur.fetchall():
                Q04 = estado7[0]
            cur.execute("SELECT estado FROM database_Q05 ORDER BY id DESC LIMIT 1")
            for estado8 in cur.fetchall():
                Q05 = estado8[0]
            cur.execute("SELECT estado FROM database_Q06 ORDER BY id DESC LIMIT 1")
            for estado9 in cur.fetchall():
                Q06 = estado9[0]
            cur.execute("SELECT estado FROM database_Q07 ORDER BY id DESC LIMIT 1")
            for estado00 in cur.fetchall():
                Q07 = estado00[0]
            cur.execute("SELECT estado FROM database_Q08 ORDER BY id DESC LIMIT 1")
            for estado01 in cur.fetchall():
                Q08 = estado01[0]
            cur.execute("SELECT estado FROM database_Q09 ORDER BY id DESC LIMIT 1")
            for estado02 in cur.fetchall():
                Q09 = estado02[0]
            cur.execute("SELECT estado FROM database_buton ORDER BY id DESC LIMIT 1;")
            valor = [i[0] for i in cur.fetchall()]
            val = valor[0]
            cur.execute("SELECT fecha FROM database_buton ORDER BY id DESC LIMIT 1;")
            fecha = [i[0] for i in cur.fetchall()]
            fecha2 = str(fecha[0])
            OutputS = [Pulso, voltaje, corriente, Q00, Q01, Q02, Q03, Q04, Q05, Q06, Q07, Q08, Q09, val, fecha2]
            await self.send(json.dumps({'OutputS': OutputS}))

            await sleep(0.001)

        for i in count(0):
            miConexion = pymysql.connect(host='127.0.0.1', user='root', passwd='SqlAdmin', db=user)
            cur = miConexion.cursor()
            cur.execute("SELECT estado FROM database_buton ORDER BY id DESC LIMIT 1")
            for estado0 in cur.fetchall():
                Pulso = estado0[0]
            cur.execute("SELECT estado FROM database_voltaje ORDER BY id DESC LIMIT 1")
            for estado1 in cur.fetchall():
                voltaje = estado1[0]
            cur.execute("SELECT estado FROM database_corriente ORDER BY id DESC LIMIT 1")
            for estado2 in cur.fetchall():
                corriente = estado2[0]
            cur.execute("SELECT estado FROM database_Q00 ORDER BY id DESC LIMIT 1")
            for estado3 in cur.fetchall():
                Q00 = estado3[0]
            cur.execute("SELECT estado FROM database_Q01 ORDER BY id DESC LIMIT 1")
            for estado4 in cur.fetchall():
                Q01 = estado4[0]
            cur.execute("SELECT estado FROM database_Q02 ORDER BY id DESC LIMIT 1")
            for estado5 in cur.fetchall():
                Q02 = estado5[0]
            cur.execute("SELECT estado FROM database_Q03 ORDER BY id DESC LIMIT 1")
            for estado6 in cur.fetchall():
                Q03 = estado6[0]
            cur.execute("SELECT estado FROM database_Q04 ORDER BY id DESC LIMIT 1")
            for estado7 in cur.fetchall():
                Q04 = estado7[0]
            cur.execute("SELECT estado FROM database_Q05 ORDER BY id DESC LIMIT 1")
            for estado8 in cur.fetchall():
                Q05 = estado8[0]
            cur.execute("SELECT estado FROM database_Q06 ORDER BY id DESC LIMIT 1")
            for estado9 in cur.fetchall():
                Q06 = estado9[0]
            cur.execute("SELECT estado FROM database_Q07 ORDER BY id DESC LIMIT 1")
            for estado00 in cur.fetchall():
                Q07 = estado00[0]
            cur.execute("SELECT estado FROM database_Q08 ORDER BY id DESC LIMIT 1")
            for estado01 in cur.fetchall():
                Q08 = estado01[0]
            cur.execute("SELECT estado FROM database_Q09 ORDER BY id DESC LIMIT 1")
            for estado02 in cur.fetchall():
                Q09 = estado02[0]
            cur.execute("SELECT estado FROM database_buton ORDER BY id DESC LIMIT 1;")
            valor = [i[0] for i in cur.fetchall()]
            val = valor[0]
            cur.execute("SELECT fecha FROM database_buton ORDER BY id DESC LIMIT 1;")
            fecha = [i[0] for i in cur.fetchall()]
            fecha2 = str(fecha[0])

            OutputS = [Pulso, voltaje, corriente, Q00, Q01, Q02, Q03, Q04, Q05, Q06, Q07, Q08, Q09, val, fecha2]
            print(OutputS)
            await self.send(json.dumps({'OutputS': OutputS}))
            await sleep(0.5)

            if i >= 5000000:
                i = 0

    async def receive(self, *args):
        text_data_json = json.loads(text_data)
        if 'action' in text_data_json and text_data_json['action'] == 'disconnect':
            websocket_disconnected = True
            return await self.close()
