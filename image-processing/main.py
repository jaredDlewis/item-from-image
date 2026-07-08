from pathlib import Path
import cv2

from get_barcode_numbers import get_barcode_numbers


def extract_item_from_image(img):
    print(get_barcode_numbers(img));

if __name__ == "__main__":
    # 1 get the image
    script_dir = Path(__file__).resolve().parent
    image_path = script_dir / "../images/1F051B14-9D22-41CA-94E4-219F378DA753_1_102_o.jpeg"
    img = cv2.imread(image_path)
    # extract item from image
    extract_item_from_image(img)
