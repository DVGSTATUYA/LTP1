from app.db import execute_query

def fetch_products() -> list[dict]:
    sql = """
    SELECT
      p."id" AS id,
      p."Product type" AS product_type,
      p."Product name" AS product_name,
      p."Article" AS article,
      p."Minimum cost for a partner" AS min_partner_cost,
      p."Main material" AS main_material
    FROM public."Products_import" AS p
    ORDER BY p."Product name";
    """
    rows = execute_query(sql).mappings().all()
    print("DEBUG:", rows[0])   
    return rows


def fetch_product_time_sum(product_name: str) -> float:
    sql = """
    SELECT COALESCE(SUM(w."Production time, h"), 0) AS total_time
    FROM public."Product_workshops_import" AS w
    WHERE w."Product name" = :product_name;
    """
    row = execute_query(sql, {"product_name": product_name}).first()
    return float(row[0] or 0.0)

def insert_product(data: dict):
    sql = """
    INSERT INTO public."Products_import"
    ("Product type", "Product name", "Article", "Minimum cost for a partner", "Main material")
    VALUES (:product_type, :product_name, :article, :min_partner_cost, :main_material)
    RETURNING id;
    """
    return execute_query(sql, data).scalar()

def update_product(product_id: int, data: dict):
    sql = """
    UPDATE public."Products_import"
    SET "Product type" = :product_type,
        "Product name" = :product_name,
        "Article" = :article,
        "Minimum cost for a partner" = :min_partner_cost,
        "Main material" = :main_material
    WHERE id = :id;
    """
    data["id"] = product_id
    execute_query(sql, data)
    

def delete_product(product_id: int):
    sql = """
    DELETE FROM public."Products_import"
    WHERE id = :id;
    """
    execute_query(sql, {"id": product_id})


