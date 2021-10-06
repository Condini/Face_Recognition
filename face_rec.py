import numpy as np
import face_recognition as fr
import cv2
import json
import os, os.path
from os import listdir
from os.path import isfile, join
from datetime import datetime
import dbconfig

db = dbconfig.db
qtdPerfis = len(db.child("mocados").get().val())
tudo = db.child("mocados").get().val()
todosNomes = list(tudo)

def collect_imgs(known_face, known_names):

    profiles_ln = qtdPerfis
    images = []

    for x in range(profiles_ln):
        images.append(fr.load_image_file("Images/"+todosNomes[x]+".jpg"))
        known_face.append(fr.face_encodings(images[x])[0])
        known_names.append(todosNomes[x])

def main():

    video_capture = cv2.VideoCapture(0)
    known_face_encondings = []
    known_face_names = []
    collect_imgs(known_face_encondings, known_face_names)

    listaDeTempos = []

    while True:
        
        ret, frame = video_capture.read()

        rgb_frame = frame[:, :, ::-1]

        face_locations = fr.face_locations(rgb_frame)
        face_encodings = fr.face_encodings(rgb_frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):

            matches = fr.compare_faces(known_face_encondings, face_encoding)

            name = "Usuario nao reconhecido"

            face_distances = fr.face_distance(known_face_encondings, face_encoding)

            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

            hoje = datetime.today().strftime('%d-%m-%Y %H:%M:%S')
            now = datetime.now()  # time object
            listaDeTempos.append(now)
            print("now =", now)

        cv2.imshow('Webcam_facerecognition', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    #minhas variaveis
    tempoInicial = listaDeTempos[0]
    tempoFinal = listaDeTempos[-1]
    tempoDeLavagem = tempoFinal - tempoInicial

    obj = [
    "Nome: " + str(name),
    "Tempo de Lavagem: " + str(tempoDeLavagem),
    "Data: " + str(hoje)
    ]

    objJson = {
    "Nome: ": str(name),
    "Tempo de Lavagem: ": str(tempoDeLavagem),
    "Data: ": str(hoje)
    }

    arquivo = open("logs.txt", "a")
    arquivo.writelines(str(obj) + "\n")

    db.child("dados").push(objJson)

    #

    video_capture.release()
    cv2.destroyAllWindows()
    print("\n\n\n\n" ,"tempo inicial:", tempoInicial, "\n", "tempo final:", tempoFinal)
    print("\n\n", "Tempo de Lavagem:", tempoDeLavagem, "\n\n")

    print("\n\n", "lista obj:", obj, "\n\n")

