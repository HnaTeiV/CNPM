import json
from app import app
def load_categories():
    with open('%sdata/categories.json'% app.root_path, encoding='utf-8') as f:
        return json.load(f)

def load_products():
    with open('%sdata/products.json'% app.root_path, encoding='utf-8') as f:
        return json.load(f)