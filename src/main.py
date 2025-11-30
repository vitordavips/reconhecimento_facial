import cv2 
import mediapipe as mp

#iniciando o opencv e o mediopipe
webcam = cv2.VideoCapture(0)
solucao_reconhcimento_rosto = mp.solutions.face_detection
reconhecimento_rostos = solucao_reconhcimento_rosto.FaceDetection()
desenho = mp.solutions.drawing_utills









