from flask import Flask, request, jsonify
from app.models import CoffeeMachine,CoffeePod

app = Flask(__name__)


@app.route("/machines", methods=['POST'])
def insert_machine():
    data = request.json

    # Data access
    product_type: str = request.json.get("type")
    water_line: bool = request.json.get("waterLine")
    sku: str = request.json.get("sku")

    error, msg = False, None

    # validation
    if product_type not in CoffeeMachine.available_product_types:
        error = True
        msg = "Invalid product type"

    elif water_line not in [True, False]:
        error = True
        msg = "Invalid water line type"

    if error:
        return jsonify({"error": msg}), 400


    cm = CoffeeMachine(product_type, water_line, sku)

    response = cm.save()


    return jsonify(response["body"]), response["status_code"]

@app.route("/machines/filter", methods=["GET"])
def filter_machine():
    machine_filter = { # {"water_line": false, product_type: None}
        "product_type" : request.args.get('product_type', default=None, type=str),
        "water_line": request.args.get('water_line', default=None, type=bool),
    }
    filter = {} # {"water_line": false}
    for k, v in machine_filter.items():
        if machine_filter[k] is  not None:
            filter[k] = v

    skus = CoffeeMachine.get(filter)
    return skus

@app.route("/pods/filter", methods=["GET"])
def filter_pod():
    pod_filter = { # {"water_line": false, product_type: None}
        "product_type" : request.args.get('product_type', default=None, type=str),
        "flavor": request.args.get('flavor', default=None, type=str),
        "pack_size": request.args.get('pack_size', default=None, type=int),
    }
    filter = {} # {"water_line": false}
    for k, v in pod_filter.items():
        if pod_filter[k] is  not None:
            filter[k] = v

    skus = CoffeePod.get(filter)
    return skus


if __name__ == "__main__":
    app.run(debug=True)
