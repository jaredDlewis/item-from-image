from pathlib import Path
import cv2

from get_barcode_numbers import get_barcode_numbers
from get_known_item_info import get_known_item_info

'''
item: {
    name: str                       # done
    description: str                # done
    price_paid: float
    price_per_unit: float
    price_unit: enum (see below)
    open_food_facts_photoUrl: str   # done
    link_url: str                   # done
}
'''


def extract_item_from_image(img):
    barcode_numbers = get_barcode_numbers(img)
    items = get_known_item_info(barcode_numbers)
    

if __name__ == "__main__":
    # 1 get the image
    script_dir = Path(__file__).resolve().parent
    image_path = script_dir / "../images/815A3524-4EA0-4AD1-AA1D-4CBD29B2BE49_1_102_o.jpeg"
    img = cv2.imread(image_path)
    # extract item from image
    extract_item_from_image(img)
