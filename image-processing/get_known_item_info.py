import requests
import pprint

def get_known_item_info(barcode_numbers: list[str]):
    items = []
    for num in barcode_numbers:
        response = requests.get(f'https://world.openfoodfacts.net/api/v3/product/{num}?fields=product_name,link,image_url,generic_name_en,brands,abbreviated_product_name')
        data = response.json()
        pprint.pprint(data)
        if data["status"] == "success":
            items.append(data)
    return items
