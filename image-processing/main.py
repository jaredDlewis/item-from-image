from pathlib import Path
import cv2
import base64
import json
from openai import OpenAI

from get_known_item_info import get_known_item_info
from constants import PRICE_UNIT_GROUPS

client = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')

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


ONE_SHOT_PROMPT = '''Given this photo of an item and its price tag at the grocery store, return a JSON object containing the following information about the item:
{
    name: str
    description: str
    price_paid: float
    price_per_unit: float (Only include the price_per_unit if it is directly available in the photo)
    amount: float (The number associated with the size of the item. (e.g. for "3.0 oz", this field has the value 3.0))
    amount_unit: str (The unit code for the amount. (e.g. for "3.0 oz", this field has the value "oz"))
}

Whenever the information for a field is not in the photo, don't include that field in the output.

If it is obvious what store the image is from, include the name of the store in the name of the item.

For amount_unit value, return the code value for the unit found in this list of price unit dictionaries
''' + f'{PRICE_UNIT_GROUPS}'


def convert_jpg_to_b64(img):
    success, buffer = cv2.imencode('.jpg', img)
    if not success:
        raise ValueError("Failed to encode image")
    img_b64 = base64.b64encode(buffer).decode('utf-8')
    return img_b64


def get_price_info_oneshot(img):
    img_b64 = convert_jpg_to_b64(img)
    resp = client.chat.completions.create(
        model='hf.co/Qwen/Qwen3-VL-8B-Instruct-GGUF:Q4_K_M',
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": ONE_SHOT_PROMPT},
                    {"type": "image_url", "image_url": {
                        "url": f"data:image/jpeg;base64,{img_b64}"}}
                ]
            }
        ]
    )
    try:
        item_dict = json.loads(resp.choices[0].message.content)
        print('item_dict: ', item_dict)
        return item_dict
    except Exception as e:
        print('error turning VLM response into dictionary:', e)
        return {}


def extract_item_from_image(img):
    ''' barcode approach '''
    # barcode_numbers = get_barcode_numbers(img)
    # items = get_known_item_info(barcode_numbers)
    ''' one-shot vlm approach '''
    get_price_info_oneshot(img)


if __name__ == "__main__":
    # 1 get the image
    script_dir = Path(__file__).resolve().parent

    '''barcode image:'''
    # image_path = script_dir / "../images/815A3524-4EA0-4AD1-AA1D-4CBD29B2BE49_1_102_o.jpeg"

    '''pricetag + item image:'''
    # image_path = script_dir / "../images/whiskey_price_tag_one_item.jpeg"

    image_path = script_dir / "../images/wine_price_tag_another_item_in_shot.jpeg"
    img = cv2.imread(image_path)
    # extract item from image
    extract_item_from_image(img)

    image_path = script_dir / "../images/whiskey_price_tag_one_item.jpeg"
    img = cv2.imread(image_path)
    # extract item from image
    extract_item_from_image(img)

    image_path = script_dir / "../images/mary_taylor_wine.jpeg"
    img = cv2.imread(image_path)
    # extract item from image
    extract_item_from_image(img)

    image_path = script_dir / "../images/bananas.jpeg"
    img = cv2.imread(image_path)
    # extract item from image
    extract_item_from_image(img)

    image_path = script_dir / "../images/greek_yogurt.jpeg"
    img = cv2.imread(image_path)
    # extract item from image
    extract_item_from_image(img)
