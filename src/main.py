import cv2 
import mediapipe as mp

#iniciando o opencv e o mediopipe
webcam = cv2.VideoCapture(0)
solucao_reconhcimento_rosto = mp.solutions.face_detection
reconhecimento_rostos = solucao_reconhcimento_rosto.FaceDetection()
desenho = mp.solutions.drawing_utills

while True:
    #Ler as informações da webcam
    verificador, frame = webcam.read()
    if not verificador:
        break

    #reconhecer os rostos que tem ali dentro
    lista_rostos = reconhecimento_rostos.process(frame)

    if lista_rostos.detections:
        for rosto in lista_rostos.detections:
            #desenhar os rostos na imagem
            desenho.draw_detection(frame, rosto)

        cv2.imshow("Rostos na webcam", frame)
        
        #quando apertar ESC, para o loop
        if cv2.waitKey(5) == 27:
            break
webcam.release()







