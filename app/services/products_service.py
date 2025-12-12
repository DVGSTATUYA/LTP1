from math import ceil
from app.repositories.products_repo import fetch_products, fetch_product_time_sum
from app.schemas.product import ProductItem

def list_products_with_time() -> list[ProductItem]:
    rows = fetch_products()
    result: list[ProductItem] = []
    for r in rows:
        print("DEBUG ROW:", r) 
        total_time = fetch_product_time_sum(r["product_name"])
        manufacturing_time = max(0, ceil(total_time))
        result.append(
            ProductItem(
                id=r["id"],  
                product_type=r["product_type"],
                product_name=r["product_name"],
                article=r["article"],
                min_partner_cost=r["min_partner_cost"],
                main_material=r["main_material"],
                manufacturing_time=manufacturing_time,
            )
        )
    return result

