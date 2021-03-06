import os
import dlib
import cv2
import glob

print(dlib.test_simple_object_detector("recursos/detect_rocket.xml", "recursos/detector_rocket.svm"))

detectorRelogio = dlib.simple_object_detector("recursos/detector_rocket.svm")
for imagem in glob.glob(os.path.join("foguete", "*.jpg")):
    img = cv2.imread(imagem)
    objetosDetectados = detectorRelogio(img)
    for d in objetosDetectados:
        e, t, d, b = (int(d.left()), int(d.top()), int(d.right()), int(d.bottom()))
        cv2.rectangle(img, (e,t), (d, b), (0,0,255), 2)

    cv2.imshow("Detector de rockets", img)
    cv2.waitKey(0)

cv2.destroyAllWindows()