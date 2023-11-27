import cv2

face = cv2.CascadeClassifier('Datas/haarcascade_frontalface_default.xml')
filename='facegirl.jpg'
img=cv2.imread(filename)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
rc=face.detectMultiScale(gray,1.09,7)
rec=(cv2.imread('Filters/rect.png'))

def put_rect(rectan, fc, x, y, w, h):
    face_width = w
    face_height = h

    hat_width = face_width + 1
    hat_height = int(0.50 * face_height) + 1

    rectan = cv2.resize(rectan, (hat_width, hat_height))

    for i in range(hat_height):
        for j in range(hat_width):
            for k in range(3):
                if rectan[i][j][k] < 235:
                    fc[y + i - int(-0.20 * face_height)][x + j][k] = rectan[i][j][k]
    return fc

for (x, y, w, h) in rc:
    frame=put_rect(rec, img, x, y, w, h)
cv2.imshow('Rectangle filter',frame)
cv2.waitKey()
cv2.destroyAllWindows()