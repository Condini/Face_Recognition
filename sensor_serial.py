import serial
import time


def rfid_compare(uid_a, uid_db, rfid):
    if(uid_a == uid_db):
        rfid = uid_db
        return print("Cartao valido")
    else:
        return print("Cartao Invalido")

def dup_rfid(uid, rfid):
    if(uid == rfid):
        return
    else:
        return print("")

conexao = ""
profile = "Rodrigo.json"
UID = "45678"
UID_t = ""

for porta in range(10):
        try:
            conexao = serial.Serial("COM"+str(porta), 9600, timeout=0.5)
            print("Conectado na porta: ", conexao.portstr)
            break
        except serial.SerialException:
            pass

if conexao!="":
    while True:
        infra_1 = (conexao.read()).decode()
        infra_2 = (conexao.read()).decode()
        rfid = (conexao.readline()).decode('utf-8')
        dup_rfid()
        print("Tag detectada: " + rfid)
        rfid_compare(rfid, UID)
        print("Infravermelhos detectados: \n")
        print(infra_1)
        print(infra_2)
    conexao.close()
    print("Conexao encerrada")
else:
    print("Sem portas disponíveis")