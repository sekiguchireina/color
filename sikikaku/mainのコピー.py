from tkinter import Frame
import cv2
import numpy as np

#カメラ読み込み 内蔵カメラは0,usb接続とかは1か-1
cap = cv2.VideoCapture(0)

#カメラが開いてる間繰り返す
while(True):
    #フレーム取得
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #im = cv2.imread('color.jpg',cv2.IMREAD_COLOR)

    #色　H,S,Vの順　抽出
    lower =np.array([0,64,0])
    upper =np.array([5,255,255])
    #frame_maskの中に上で指定した色を保存
    mask1 = cv2.inRange(hsv,lower,upper)
    #赤の場合はもう一回
    lower =np.array([173,64,0])
    upper =np.array([180,255,255])
    mask2 = cv2.inRange(hsv,lower,upper)

    mask = mask1 + mask2

    #frame_maskの色だけ抽出、表示
    dst = cv2.bitwise_and(frame,frame,mask = mask)

    frame[mask==0] = [128,128,128]
    
    #グレスケ変換　
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #フレーム表示
    cv2.imshow("Frame",gray)
    cv2.imshow("Frame",dst)

    #Q押されたら終わり
    if cv2.waitKey(1)&0xFF == ord('q'):
        break
    
#あとしまつ
cap.release()
cv2.destroyAllWindows()