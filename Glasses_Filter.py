import cv2

def glasses_filter(path):
    face = cv2.CascadeClassifier('Datas/haarcascade_frontalface_default.xml')

    img=cv2.imread(path)
    img=cv2.resize(img,(0,0),None,0.5,0.5)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ey=face.detectMultiScale(gray,1.09,7)
    glass=cv2.imread('Filters/glasses.png')

    def put_glass(glass, fc, x, y, w, h):
        face_width = w
        face_height = h

        hat_width = face_width + 1
        hat_height = int(0.50 * face_height) + 1

        glass = cv2.resize(glass, (hat_width, hat_height))

        for i in range(hat_height):
            for j in range(hat_width):
                for k in range(3):
                    if glass[i][j][k] < 235:
                        fc[y + i - int(-0.20 * face_height)][x + j][k] = glass[i][j][k]
        return fc

    for (x, y, w, h) in ey:
        frame=put_glass(glass,img, x, y, w, h)
    return frame
