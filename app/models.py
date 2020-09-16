from .config import machines_collection,pods_collection
from bson.json_util import dumps

class CoffeeMachine:
    product_type = None
    water_line = None
    sku = None

    available_product_types = [
        "COFFE_MACHINE_LARGE",
        "COFFE_MACHINE_SMALL",
        "ESPRESSO_MACHINE"
    ]

    def __init__(self, product_type, water_line, sku):
        self.product_type = product_type
        self.water_line = water_line
        self.sku = sku

    def save(self):
        response = {
            "body": None,
            "status_code": 200
        }
        # save data to mongo
        data = {
            'product_type': self.product_type,
            'water_line': self.water_line,
            'sku': self.sku
        }
        result = machines_collection.insert_one(data)
        response["body"] = result.inserted_id if result.inserted_id  else "Error"
        response["status_code"] = 200 if result.inserted_id else 500

        return response

    def get(filter):
        result = machines_collection.find(filter)
        result_list = list(result)
        skus = []
        for result in result_list:
            skus.append(result['sku'])
        json_data = dumps(skus)
        return json_data


class CoffeePod:
    product_type = None
    coffee_flavor = None
    pack_size = None
    sku = None

    available_product_types = [
        "COFFE_POD_LARGE",
        "COFFE_POD_SMALL",
        "ESPRESSO_POD"
    ]

    def __init__(self, product_type, coffee_flavor, pack_size, sku):
        self.product_type = product_type
        self.coffee_flavor = coffee_flavor
        self.pack_size = pack_size
        self.sku = sku

    def save(self):
        response = {
            "body": None,
            "status_code": 200
        }
        # save data to mongo
        data = {
            'product_type': self.product_type,
            'coffee_flavor': self.coffee_flavor,
            'pack_size': self.pack_size,
            'sku': self.sku
        }
        result = pods_collection.insert_one(data)
        response["body"] = result.inserted_id if result.inserted_id  else "Error"
        response["status_code"] = 200 if result.inserted_id else 500

        return response

    def get(filter):
        result = pods_collection.find(filter)
        result_list = list(result)
        skus = []
        for result in result_list:
            skus.append(result['sku'])
        json_data = dumps(skus)
        return json_data
