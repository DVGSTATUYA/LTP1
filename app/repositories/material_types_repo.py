
from app.db import execute_query

def fetch_material_types() -> list[dict]:
    sql = """
    SELECT id,
           "Type material" AS type_material,
           "Percentage of raw material losses" AS loss_percent
    FROM public."Material_type_import"
    ORDER BY id;
    """
    return execute_query(sql).mappings().all()
