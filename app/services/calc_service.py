
from typing import Optional
from app.repositories.product_types_repo import fetch_product_types
from app.repositories.material_types_repo import fetch_material_types

def calculate_raw_material(
    product_type_id: int,
    material_type_id: int,
    quantity: int,
    param1: float,
    param2: float,
) -> int:
    # Валидация типов входных данных
    if quantity <= 0 or param1 <= 0 or param2 <= 0:
        return -1

    # Получаем справочники
    pts = fetch_product_types()
    mts = fetch_material_types()

    pt: Optional[dict] = next((p for p in pts if p["id"] == product_type_id), None)
    mt: Optional[dict] = next((m for m in mts if m["id"] == material_type_id), None)
    if not pt or not mt:
        return -1

    coeff = float(pt["coefficient"])
    loss = float(mt["loss_percent"])

    base_raw = param1 * param2 * coeff
    total_raw = base_raw * quantity * (1 + loss / 100.0)

    # Возвращаем целое число, округляя вверх при наличии долей
    return int(total_raw + 0.0000001)
