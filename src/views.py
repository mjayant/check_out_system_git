#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import request, render_template, make_response
from datetime import datetime as dt
from flask import current_app as app
from .models import db, Product


@app.route('/', methods=['GET'])
def add_product():
    """Create a user via query string parameters."""
    product_id = request.args.get('product_id')
    product_name = request.args.get('product_name')
    price = request.args.get('price')
    if product_id and product_name:
        new_product = Product(product_id= product_id,
                              product_name=product_name,
                              price=price)
    db.session.add(new_product)  # Adds new User record to database
    db.session.commit()

    return make_response(f"{new_product} successfully created!")