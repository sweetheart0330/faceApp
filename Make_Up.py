import cv2
import numpy as np
import dlib
# основа ии

def make_up_filter(make_up_lips,make_up_eyes,FILTER,COLOR,path):
    detector=dlib.get_frontal_face_detector()
    predictor=dlib.shape_predictor("Datas/shape_predictor_68_face_landmarks.dat")

    # информация с интерфейса
    #make_up_lips=True
    #make_up_eyes=True
    #FILTER=True
    #COLOR=[89, 236, 21]

    # создание маски и преобразование по заданным условиям
    def createBox(img,points,scale=5,masked=False,cropped=True):
        if masked:
            mask=np.zeros_like(img)
            mask=cv2.fillPoly(mask,[points],(255,255,255))
            img=cv2.bitwise_and(img,mask)
            #cv2.imshow('Mask',img)
        if cropped:
            bbox=cv2.boundingRect(points)
            x,y,w,h=bbox
            imgCrop=img[y:y+h,x:x+w]
            imgCrop=cv2.resize(imgCrop,(0,0),None,scale,scale)
            return imgCrop
        else:
            return mask

    # взятие картинки для работы + припроцессинг
    img=cv2.imread(path)
    img=cv2.resize(img,(0,0),None,0.5,0.5)
    imgOriginal=img.copy()

    imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=detector(imgGray)

    # работа проставленние маркеров + конечное преобразование пикчи
    for face in faces:
        x1,y1=face.left(),face.top()
        x2,y2=face.right(),face.bottom()
        #imgOriginal=cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
        landmarks=predictor(imgGray,face)
        myPoints=[]
        # для понимание где на лице располагается какой-то номер маркера
        for n in range(68):
            x=landmarks.part(n).x
            y=landmarks.part(n).y
            myPoints.append([x,y])
            #cv2.circle(imgOriginal,(x,y),5,(50,50,255),cv2.FILLED)
            #cv2.putText(imgOriginal,str(n),(x,y-10),cv2.FONT_HERSHEY_PLAIN,0.8,(0,0,255),1)

        myPoints=np.array(myPoints)
        # фильтр
        if FILTER:
            imgOriginalGray = cv2.cvtColor(imgOriginal,
                                           cv2.COLOR_BGR2GRAY)  # цвето фильтр в из 3-х канального в однокональный
            imgOriginalGray = cv2.cvtColor(imgOriginalGray,
                                           cv2.COLOR_GRAY2BGR)  # цвето фильтр из одноканального в 3 канальный (нужный)
            imgColor = imgOriginalGray
        else:
            imgColor = imgOriginal
        if make_up_lips:
            # работа с точками и использование функции для ролучения полигонов
            imgLips=createBox(img,myPoints[48:61],3,masked=True,cropped=False)

            # окончательное слияние + окрашивание полигонов
            imgColorLips=np.zeros_like(imgLips)
            imgColorLips[:]=COLOR # цвет полигона
            imgColorLips=cv2.bitwise_and(imgLips,imgColorLips)
            imgColorLips=cv2.GaussianBlur(imgColorLips,(7,7),10)# блюр

            imgColor=cv2.addWeighted(imgColor,1,imgColorLips,0.4,0)# слияние полигона и картинки
            #cv2.imshow('ColoredLips',imgColor)


            #cv2.imshow('Lips',imgLips)
            #print(myPoints)
        if make_up_eyes:
            # работа с точками и использование функции для получения полигонов

            imgLeftEye = createBox(img, myPoints[36:42], 3, masked=True, cropped=False)
            imgRightEye = createBox(img, myPoints[42:48], 3, masked=True, cropped=False)
            # окончательное слияние + окрашивание полигонов
            imgColorLeftEye = np.zeros_like(imgLeftEye)
            imgColorRightEye = np.zeros_like(imgRightEye)

            imgColorLeftEye[:] = 153, 0, 157  # цвет полигона
            imgColorRightEye[:] = 153, 0, 157
            imgColorLeftEye = cv2.bitwise_and(imgLeftEye, imgColorLeftEye)
            imgColorRightEye = cv2.bitwise_and(imgRightEye, imgColorRightEye)
            imgColorLeftEye = cv2.GaussianBlur(imgColorLeftEye, (7, 7), 10)  # блюр
            imgColorRightEye = cv2.GaussianBlur(imgColorRightEye, (7, 7), 10)
            imgColor = cv2.addWeighted(imgColor, 1, imgColorLeftEye, 0.4, 0)# слияние полигона и картинки
            imgColor = cv2.addWeighted(imgColor, 1, imgColorRightEye, 0.4, 0)
            #cv2.imshow('Colored Eyes', imgColor)

            #cv2.imshow('Lips', imgLeftEye)
        #итоговое изображение
        cv2.imshow('Result picture',imgColor)


        #print(myPoints)

    #cv2.imshow("Original",imgOriginal)
    cv2.waitKey(0)
#make_up_filter(True,False,False,[30,236,20],'facegirl.jpg')