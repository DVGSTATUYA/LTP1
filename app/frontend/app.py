
from flask import Flask, render_template, request, redirect, url_for, flash
import requests

app = Flask(__name__)
app.secret_key = "dev-secret"
API = "http://127.0.0.1:8000"

@app.route("/")
def home():
    return redirect(url_for("products"))

@app.route("/products")
def products():
    try:
        products = requests.get(f"{API}/products").json()
    except Exception as e:
        flash(f"Ошибка загрузки продукции: {e}", "error")
        products = []
    return render_template("products.html", products=products, title="Продукция")

@app.route("/products/add", methods=["GET", "POST"])
def add_product():
    try:
        product_types = requests.get(f"{API}/product_types").json()
        material_types = requests.get(f"{API}/material_types").json()
    except Exception as e:
        flash(f"Ошибка загрузки справочников: {e}", "error")
        product_types, material_types = [], []

    if request.method == "POST":
        data = {
            "product_type": request.form.get("product_type", "").strip(),
            "product_name": request.form.get("product_name", "").strip(),
            "article": request.form.get("article", "").strip() or None,
            "min_partner_cost": request.form.get("min_partner_cost", "").strip() or None,
            "main_material": request.form.get("main_material", "").strip(),
            "id": None,
        }


        errors = []
        if not data["product_type"]:
            errors.append("Выберите тип продукта.")
        if not data["product_name"]:
            errors.append("Введите наименование продукта.")
        if data["min_partner_cost"] is not None:
            try:
                cost = float(data["min_partner_cost"])
                if cost < 0:
                    errors.append("Минимальная стоимость не может быть отрицательной.")
            except ValueError:
                errors.append("Минимальная стоимость должна быть числом.")
        if not data["main_material"]:
            errors.append("Выберите основной материал.")

        if errors:
            flash("Ошибка ввода: " + " ".join(errors), "error")
            return render_template("product_form.html",
                                   product=None,
                                   product_types=product_types,
                                   material_types=material_types,
                                   title="Добавление продукта")

        try:
            if data["article"] is not None:
                data["article"] = int(data["article"])
            if data["min_partner_cost"] is not None:
                data["min_partner_cost"] = round(float(data["min_partner_cost"]), 2)
            requests.post(f"{API}/products", json=data).raise_for_status()
            flash("Продукт добавлен", "success")
            return redirect(url_for("products"))
        except Exception as e:
            flash(f"Ошибка добавления: {e}", "error")

    return render_template("product_form.html",
                           product=None,
                           product_types=product_types,
                           material_types=material_types,
                           title="Добавление продукта")

@app.route("/products/<int:pid>/edit", methods=["GET", "POST"])
def edit_product(pid: int):
    try:
        products = requests.get(f"{API}/products").json()
        product = next((p for p in products if p["id"] == pid), None)
        product_types = requests.get(f"{API}/product_types").json()
        material_types = requests.get(f"{API}/material_types").json()
    except Exception as e:
        flash(f"Ошибка загрузки: {e}", "error")
        product, product_types, material_types = None, [], []

    if not product:
        flash("Продукт не найден.", "error")
        return redirect(url_for("products"))

    if request.method == "POST":
        data = {
            "product_type": request.form.get("product_type", "").strip(),
            "product_name": request.form.get("product_name", "").strip(),
            "article": request.form.get("article", "").strip() or None,
            "min_partner_cost": request.form.get("min_partner_cost", "").strip() or None,
            "main_material": request.form.get("main_material", "").strip(),
            "id": None,
        }
        errors = []
        if not data["product_type"]:
            errors.append("Выберите тип продукта.")
        if not data["product_name"]:
            errors.append("Введите наименование продукта.")
        if data["min_partner_cost"] is not None:
            try:
                cost = float(data["min_partner_cost"])
                if cost < 0:
                    errors.append("Минимальная стоимость не может быть отрицательной.")
            except ValueError:
                errors.append("Минимальная стоимость должна быть числом.")
        if not data["main_material"]:
            errors.append("Выберите основной материал.")

        if errors:
            flash("Ошибка ввода: " + " ".join(errors), "error")
        else:
            try:
                if data["article"] is not None:
                    data["article"] = int(data["article"])
                if data["min_partner_cost"] is not None:
                    data["min_partner_cost"] = round(float(data["min_partner_cost"]), 2)
                requests.put(f"{API}/products/{pid}", json=data).raise_for_status()
                flash("Продукт обновлен", "success")
                return redirect(url_for("products"))
            except Exception as e:
                flash(f"Ошибка обновления: {e}", "error")

    return render_template("product_form.html",
                           product=product,
                           product_types=product_types,
                           material_types=material_types,
                           title="Редактирование продукта")

@app.route("/products/<int:pid>/delete")
def delete_product(pid: int):
    try:
        requests.delete(f"{API}/products/{pid}").raise_for_status()
        flash("Продукт удалён", "success")
    except Exception as e:
        flash(f"Ошибка удаления: {e}", "error")
    return redirect(url_for("products"))

@app.route("/workshops")
def workshops():
    try:
        workshops = requests.get(f"{API}/workshops").json()
    except Exception as e:
        flash(f"Ошибка загрузки цехов: {e}", "error")
        workshops = []

    total_workers = sum(int(w.get("employee_count", 0)) for w in workshops if isinstance(w, dict))
    return render_template("workshops.html",
                           workshops=workshops,
                           total_workers=total_workers,
                           title="Цеха производства")

@app.route("/products/<int:pid>/workshops")
def product_workshops(pid: int):
    try:
        products = requests.get(f"{API}/products").json()
        product = next((p for p in products if p["id"] == pid), None)
        if not product:
            flash("Продукт не найден.", "error")
            return redirect(url_for("products"))
        rows = requests.get(f"{API}/products/{pid}/workshops").json()
    except Exception as e:
        flash(f"Ошибка загрузки: {e}", "error")
        rows, product = [], None

    total_workers = sum(int(r.get("employee_count", 0)) for r in rows if isinstance(r, dict))
    total_time = sum(float(r.get("production_time_h", 0) or 0) for r in rows if isinstance(r, dict))
    return render_template("product_workshops.html",
                           product=product,
                           rows=rows,
                           total_workers=total_workers,
                           total_time=total_time,
                           title="Цеха продукта")

@app.route("/calculation", methods=["GET", "POST"])
def calculation():
    result = None
    selected_type_id = None
    selected_material_id = None

    try:
        product_types = requests.get(f"{API}/product_types").json()
        material_types = requests.get(f"{API}/material_types").json()
    except Exception as e:
        flash(f"Ошибка загрузки справочников: {e}", "error")
        product_types, material_types = [], []

    param_labels_map = {
        "Гостиные": ("Площадь (м²)", "Коэффициент плотности"),
        "Прихожие": ("Ширина (м)", "Высота (м)"),
        "Мягкая мебель": ("Объём (м³)", "Коэффициент наполнителя"),
        "Кровати": ("Длина (м)", "Ширина (м)"),
        "Шкафы": ("Ширина (м)", "Высота (м)"),
        "Комоды": ("Площадь фасада (м²)", "Толщина материала (мм)"),
    }

    labels = ("Параметр 1", "Параметр 2")

    if request.method == "POST":
        pt_id_raw = request.form.get("product_type_id", "").strip()
        mt_id_raw = request.form.get("material_type_id", "").strip()
        qty_raw = request.form.get("quantity", "").strip()
        p1_raw = request.form.get("param1", "").strip()
        p2_raw = request.form.get("param2", "").strip()

        selected_type_id = pt_id_raw or None
        selected_material_id = mt_id_raw or None

        chosen_pt = next((p for p in product_types if str(p["id"]) == selected_type_id), None)
        if chosen_pt and chosen_pt["product_type"] in param_labels_map:
            labels = param_labels_map[chosen_pt["product_type"]]

        if not (pt_id_raw and mt_id_raw and qty_raw and p1_raw and p2_raw):
            flash("Заполните все поля перед расчётом.", "error")
            return render_template("calculation.html",
                                   product_types=product_types,
                                   material_types=material_types,
                                   labels=labels,
                                   selected_type_id=selected_type_id,
                                   selected_material_id=selected_material_id,
                                   result=None,
                                   title="Расчёт сырья")

        try:
            pt_id = int(pt_id_raw)
            mt_id = int(mt_id_raw)
            qty = int(qty_raw)
            p1 = float(p1_raw)
            p2 = float(p2_raw)
        except ValueError:
            flash("Количество должно быть целым, параметры — вещественными положительными числами.", "error")
            return render_template("calculation.html",
                                   product_types=product_types,
                                   material_types=material_types,
                                   labels=labels,
                                   selected_type_id=selected_type_id,
                                   selected_material_id=selected_material_id,
                                   result=None,
                                   title="Расчёт сырья")

        try:
            resp = requests.get(f"{API}/calculate_raw_material", params={
                "product_type_id": pt_id,
                "material_type_id": mt_id,
                "quantity": qty,
                "param1": p1,
                "param2": p2,
            }).json()
            result = resp.get("result", -1)
            if result == -1:
                flash("Неверные входные данные или отсутствуют типы в справочниках.", "error")
            else:
                flash(f"Необходимое количество сырья: {result} ед.", "success")
        except Exception as e:
            flash(f"Ошибка расчёта: {e}", "error")

        chosen_pt = next((p for p in product_types if p["id"] == pt_id), None)
        if chosen_pt and chosen_pt["product_type"] in param_labels_map:
            labels = param_labels_map[chosen_pt["product_type"]]

    return render_template("calculation.html",
                           product_types=product_types,
                           material_types=material_types,
                           labels=labels,
                           selected_type_id=selected_type_id,
                           selected_material_id=selected_material_id,
                           result=result,
                           title="Расчёт сырья")

if __name__ == "__main__":
    app.run(debug=True)



