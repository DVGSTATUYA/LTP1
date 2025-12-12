
from app.repositories.workshops_repo import fetch_workshops_all, fetch_workshops_for_product

def list_workshops_all(): return fetch_workshops_all()
def list_workshops_for_product(product_id: int): return fetch_workshops_for_product(product_id)
