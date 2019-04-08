# "Quality Control" Exercise

Provides an example application with opportunities for refactoring and testing.

## Setup

```sh
conda create -n id-autogen-env python=3.7
conda activate id-autogen-env
```

Copy the default products CSV file into the "data" directory, where the application expects it to be:

```sh
cp test/mock_data/default_products.csv data/products.csv # (or do it manually)
```

## Usage

Run the app:

```sh
python app/inventory_app.py
```

## Testing

Install the `pytest` package, if necessary (first time only, from within the virtual environment):

```sh
pip install pytest
```

Run tests:

```sh
pytest
```
