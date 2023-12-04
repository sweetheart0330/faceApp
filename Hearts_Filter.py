import cv2
from PIL import Image as im

def hearts_filter(path):
    face = cv2.CascadeClassifier('Datas/haarcascade_frontalface_default.xml')

    img=cv2.imread(path)
    img=cv2.resize(img,(0,0),None,0.5,0.5)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # препроцессинг
    fl=face.detectMultiScale(gray,1.09,7)
    heart=cv2.imread('Filters/hearts.png')


    # функция для подгонки и размещения шляпы
    def put_heart(he, fc, x, y, w, h):
        face_width = w
        face_height = h
        h_width = face_width + 1
        h_height = int(0.60 * face_height) + 1
        he = cv2.resize(he, (h_width, h_height))

        for i in range(h_height):
            for j in range(h_width):
                for k in range(3):
                    if he[i][j][k] < 235:
                        fc[y + i - int(0.45 * face_height)][x + j][k] = he[i][j][k]
        return fc
    for (x, y, w, h) in fl:
        frame = put_heart(heart, img, x, y, w, h)

    cv2.imshow('Hearts filter',frame)
    cv2.waitKey()
    cv2.destroyAllWindows()
    #cv2.imwrite('saved.jpg',frame)
