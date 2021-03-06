from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.exceptions import NotFound

from models.product import Product

product_app = Blueprint("product_app", __name__)


next_index = iter(range(len(PRODUCTS) + 1, 100))

@product_app.route("/", endpoint="list")
def product_list():
    products = Product.query.all()
    return render_template("products/index.html", products=products)


@product_app.route("/<int:product_id>/", endpoint="details")
def product_details(product_id):
    product = Product.query.filter_by(id=product_id).one_or_none()
    if product_id not in PRODUCTS:
        raise NotFound(f"Product with id {product_id} doesn't exist!")

    product_name = PRODUCTS[product_id]

    return render_template(
        "products/details.html",
        product=product,
    )

@product_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def product_add():
    if request.method == "GET":
        return render_template("products/add-new.html")

    product = Product(name=request.form.get("product-name"))
    db.session.add(product)
    db.session.commit()
    return redirect(url_for("product_app.list"))