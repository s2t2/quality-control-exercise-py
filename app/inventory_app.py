import csv
import os

csv_headers = ["id", "name", "aisle", "department", "price"]

def read_from_csv(my_csv_filepath):
    my_products = []

    with open(my_csv_filepath, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for ordered_dict in reader:
            my_products.append(dict(ordered_dict))

    return my_products

def write_to_csv(my_products, my_filepath):
    with open(my_filepath, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
        writer.writeheader()

        for product in my_products:
            writer.writerow(product)

def autogen_id(existing_products):
    #return len(existing_products) + 1
    if len(existing_products) == 0: # avoid "max() arg is an empty sequence" error when attempting to call max() on an empty list of products
        next_id = 1
    else:
        product_ids = [int(p["id"]) for p in existing_products]
        max_id = max(product_ids)
        next_id = max_id + 1
    return next_id

# only run the code inside if this script is invoked from the command line
if __name__ == "__main__":

    # READ

    csv_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "products.csv")

    products = read_from_csv(csv_filepath)

    #
    # LIST
    #

    print("---------------------")
    print("LISTING PRODUCTS:")

    for product in products:
        print(f"  {product['id']}) {product['name']} ")

    #
    # CREATE
    #

    print("---------------------")
    print("CREATING A NEW PRODUCT:")

    new_product = {
        "name": "My New Product",
        "aisle": "Some Aisle",
        "department": "Some Department",
        "price": 99.99
    } # further exploration / todo: ask for user to input

    next_id = autogen_id(products)

    new_product["id"] = next_id

    print(new_product)

    products.append(new_product)

    # WRITE

    write_to_csv(products, csv_filepath)
