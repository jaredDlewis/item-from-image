from pathlib import Path
import cv2
from cv2.typing import MatLike
from pyzbar.pyzbar import decode

def get_barcode_numbers(img: MatLike | None = None):
    barcodes = []
    for d in decode(img):
        barcodes.append(d.data.decode())
    return barcodes

if __name__ == '__main__':
    ''' Run on example image '''
    script_dir = Path(__file__).resolve().parent
    image_path = script_dir / "../images/1F051B14-9D22-41CA-94E4-219F378DA753_1_102_o.jpeg"
    img = cv2.imread(image_path)
    print(get_img_barcode(img))
