
from app.db import execute_query

def fetch_product_types() -> list[dict]:
    sql = """
    SELECT id,
           "Product type" AS product_type,
           "Product type coefficient" AS coefficient
    FROM public."Product_type_import"
    ORDER BY id;
    """
    return execute_query(sql).mappings().all()
