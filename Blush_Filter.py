import cv2


def blush_filter(path):

    face = cv2.CascadeClassifier('Datas/haarcascade_frontalface_default.xml')
    #filename='facegirl.jpg'
    img=cv2.imread(path)
    img=cv2.resize(img,(0,0),None,0.5,0.5)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ey=face.detectMultiScale(gray,1.09,7)
    blush=cv2.imread('Filters/blush.png')

    def put_blush(bl, fc, x, y, w, h):
        face_width = w
        face_height = h

        blush_width = int(face_width)+ 1
        blush_height = int(0.30 * face_height) + 1

        bl = cv2.resize(bl, (blush_width, blush_height))

        for i in range(blush_height):
            for j in range(blush_width):
                for k in range(3):
                    if bl[i][j][k] < 235:
                        fc[y + i - int(-0.40 * face_height)][x + j][k] = bl[i][j][k]
        return fc

    for (x, y, w, h) in ey:
        frame=put_blush(blush, img, x, y, w, h)
    return frame