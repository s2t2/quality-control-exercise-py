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


# only run the code inside if this script is invoked from the command line
if __name__ == "__main__":

    # print(__name__)
    # print(__file__)

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

    next_id = len(products) + 1

    new_product["id"] = next_id

    print(new_product)

    products.append(new_product)

    # WRITE

    write_to_csv(products, csv_filepath)
