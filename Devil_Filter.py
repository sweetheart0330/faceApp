import cv2
from PIL import Image as im

#
def devil_filter(path):

    face = cv2.CascadeClassifier('Datas/haarcascade_frontalface_default.xml')

    img=cv2.imread(path)
    img=cv2.resize(img,(0,0),None,0.5,0.5)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # препроцессинг
    fl=face.detectMultiScale(gray,1.09,7)
    dev=cv2.imread('Filters/devil.png')


    # функция для подгонки и размещения шляпы
    def put_dev(de, fc, x, y, w, h):
        face_width = w
        face_height = h
        dev_width = face_width + 1
        dev_height = int(0.50 * face_height) + 1
        de = cv2.resize(de, (dev_width, dev_height))

        for i in range(dev_height):
            for j in range(dev_width):
                for k in range(3):
                    if de[i][j][k] < 235:
                        fc[y + i - int(0.40 * face_height)][x + j][k] = de[i][j][k]
        return fc
    for (x, y, w, h) in fl:
        frame = put_dev(dev, img, x, y, w, h)

    return frame
