
from app.db import execute_query

def fetch_workshops_all() -> list[dict]:
    sql = """
    SELECT w."id" AS id,
           w."Workshop name" AS workshop_name,
           w."Workshop type" AS workshop_type,
           w."Number of people for production" AS employee_count
    FROM public."Workshops_import" AS w
    ORDER BY id;
    """
    return execute_query(sql).mappings().all()

def fetch_workshops_for_product(product_id: int) -> list[dict]:
    # Привязываем по имени продукта и имени цеха: берём людей из Workshops_import, время из Product_workshops_import
    sql = """
    SELECT wi."id" AS id,
           wi."Workshop name" AS workshop_name,
           wi."Number of people for production" AS employee_count,
           pwi."Production time, h" AS production_time_h
    FROM public."Products_import" AS p
    JOIN public."Product_workshops_import" AS pwi
      ON pwi."Product name" = p."Product name"
    JOIN public."Workshops_import" AS wi
      ON wi."Workshop name" = pwi."Workshop name"
    WHERE p."id" = :product_id
    ORDER BY wi."id";
    """
    rows = execute_query(sql, {"product_id": product_id}).mappings().all()
    return rows
