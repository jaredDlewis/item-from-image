import cv2
import numpy as np
from pyzbar.pyzbar import decode

img = cv2.imread('../images/1F051B14-9D22-41CA-94E4-219F378DA753_1_102_o.jpeg')

for d in decode(img):
    img = cv2.rectangle(img, (d.rect.left, d.rect.top),
                        (d.rect.left + d.rect.width, d.rect.top + d.rect.height), (255, 0, 0), 2)
    img = cv2.polylines(img, [np.array(d.polygon)], True, (0, 255, 0), 2)
    img = cv2.putText(img, d.data.decode(), (d.rect.left, d.rect.top + d.rect.height),
                      cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 1, cv2.LINE_AA)

cv2.imwrite('../images/1F051B14-9D22-41CA-94E4-219F378DA753_1_102_o_opencv.jpeg')