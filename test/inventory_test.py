import csv
import os

from app.inventory_app import read_from_csv, write_to_csv #, autogen_id

# test logic for processing CSV file contents into a list of product dictionaries
def test_read_from_csv():
    default_products_filepath = os.path.join(os.path.dirname(__file__), "..", "test", "mock_data", "default_products.csv")

    default_products = read_from_csv(default_products_filepath)

    assert len(default_products) == 20
    assert default_products[0]["name"] == "Chocolate Sandwich Cookies"

# test logic for writing a list of product dictionaries to a CSV file
def test_write_to_csv():
    temp_filepath = os.path.join(os.path.dirname(__file__), "..", "test", "mock_data", "temp_products.csv")

    # setup:
    if os.path.isfile(temp_filepath):
        os.remove(temp_filepath)

    assert os.path.isfile(temp_filepath) == False

    # test:
    products = []

    write_to_csv(products, temp_filepath)

    assert os.path.isfile(temp_filepath) == True

## TODO: test logic for auto-incrementing the identifier of a product about to be created
#def test_autogen_id():
#    assert False
