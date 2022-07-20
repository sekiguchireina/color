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
    
    s_magnification = 0  # 彩度(Saturation)の倍率
    v_magnification = 1  # 明度(Value)の倍率

    #hsv[:,:,(1)] = hsv[:,:,(1)]*s_magnification  # 彩度の計算
    #hsv[:,:,(2)] = hsv[:,:,(2)]*v_magnification  # 明度の計算
    
    hsv_2 = np.copy(hsv)
    hsv_3 = np.copy(hsv)
    hsv_4 = np.copy(hsv)


    # h>173の画素(赤いとこ)のhを-155 それ以外は色相そのまま
    hsv_2[:,:, 0] = np.where(hsv[:, :, 0]>173,hsv[:, :, 0]-155,hsv[:, :, 0])
    # h<5の画素(赤いとこ)のhを+18
    hsv_3[:, :, 0] = np.where(hsv_2[:, :, 0]<5,hsv_2[:, :, 0]+18,hsv_2[:, :, 0])

    #赤以外白黒にする
    hsv_3[:,:,1] = np.where((hsv_3[:, :, 0]>17) & (hsv_3[:, :, 0]<26),hsv_3[:,:,(1)],hsv_3[:,:,(1)]*s_magnification)

    # HSV->BGR変換
    bgr = cv2.cvtColor(hsv_3, cv2.COLOR_HSV2BGR)

    #フレーム表示
    cv2.imshow("Frame",bgr)
    
    #Q押されたら終わり
    if cv2.waitKey(1)&0xFF == ord('q'):
        break
    
#あとしまつ
cap.release()
cv2.destroyAllWindows()
