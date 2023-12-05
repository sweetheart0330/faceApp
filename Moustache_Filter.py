import cv2

def moust_filter(path):

    face = cv2.CascadeClassifier('Datas/haarcascade_frontalface_default.xml')

    img=cv2.imread(path)
    img=cv2.resize(img,(0,0),None,0.5,0.5)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ey=face.detectMultiScale(gray,1.09,7)
    moust=cv2.imread('Filters/moustache.png')

    def put_moust(mo, fc, x, y, w, h):
        face_width = w
        face_height = h

        mou_width = face_width + 1
        mou_height = int(0.40 * face_height) + 1

        mo = cv2.resize(mo, (mou_width, mou_height))

        for i in range(mou_height):
            for j in range(mou_width):
                for k in range(3):
                    if mo[i][j][k] < 235:
                        fc[y + i - int(-0.50 * face_height)][x + j][k] = mo[i][j][k]
        return fc

    for (x, y, w, h) in ey:
        frame=put_moust(moust, img, x, y, w, h)
    return frame
