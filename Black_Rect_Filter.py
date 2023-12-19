import cv2

def brect_filter(path):

    face = cv2.CascadeClassifier('Datas/haarcascade_frontalface_default.xml')

    img=cv2.imread(path)
    img=cv2.resize(img,(0,0),None,0.5,0.5)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    rc=face.detectMultiScale(gray,1.09,7)
    rec=(cv2.imread('Filters/rect.png'))

    def put_rect(rectan, fc, x, y, w, h):
        face_width = w
        face_height = h

        rec_width = face_width + 1
        rec_height = int(0.30 * face_height) + 1

        rectan = cv2.resize(rectan, (rec_width, rec_height))

        for i in range(rec_height):
            for j in range(rec_width):
                for k in range(3):
                    if rectan[i][j][k] < 235:
                        fc[y + i - int(-0.20 * face_height)][x + j][k] = rectan[i][j][k]
        return fc

    for (x, y, w, h) in rc:
        frame=put_rect(rec, img, x, y, w, h)
    #cv2.imshow('Rectangle filter',frame)
    #cv2.waitKey()
    #cv2.destroyAllWindows()
    return frame
