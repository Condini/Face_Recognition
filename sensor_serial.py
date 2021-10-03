import dbconfig
import serial
import time


def rfid_compare(rfid):
    print("RFID detectado: "+rfid)
    UID_search = db1.child("mocados").order_by_child('UID').equal_to(rfid).get()
    if UID_search == "":
        return print("Cartao Invalido ou Usuário nao existente!\n")
    else:
        for args in UID_search.each():
            list = args.val()
        name_UID = list["Nome"]
        return print("Cartao Válido! Funcionário: "+ name_UID + "\n")

def dup_rfid(uid, rfid):
    if(uid == rfid):
        return
    else:
        return print("")

conexao = ""
profile = "Rodrigo.json"
UID_t = ""
db1 = dbconfig.db


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
        rfid_compare(rfid)
        print("Infravermelhos detectados: \n")
        print(infra_1)
        print(infra_2)
    conexao.close()
    print("Conexao encerrada")
else:
    print("Sem portas disponíveis")