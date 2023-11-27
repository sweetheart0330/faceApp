import cv2

face = cv2.CascadeClassifier('Datas/haarcascade_frontalface_default.xml')

#
filename='facegirlnew.jpg'

img=cv2.imread(filename)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# препроцессинг
fl=face.detectMultiScale(gray,1.09,7)
hat=cv2.imread('Filters/hat.png')

# функция для подгонки и размещения шляпы
def put_hat(hat, fc, x, y, w, h):
    face_width = w
    face_height = h
    hat_width = face_width + 1
    hat_height = int(0.50 * face_height) + 1
    hat = cv2.resize(hat, (hat_width, hat_height))

    for i in range(hat_height):
        for j in range(hat_width):
            for k in range(3):
                if hat[i][j][k] < 235:
                    fc[y + i - int(0.40 * face_height)][x + j][k] = hat[i][j][k]
    return fc

for (x, y, w, h) in fl:
    frame = put_hat(hat, img, x, y, w, h)
cv2.imshow('Hat filter',frame)
cv2.waitKey()
cv2.destroyAllWindows()