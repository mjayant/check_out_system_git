#!/usr/bin/python
# -*- coding: utf-8 -*-
# import sys
# import os
# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
# sys.path.append(os.path.dirname(__file__))
# print(sys.path)


from flask import Flask , render_template, request, url_for, flash, redirect, make_response
from models import db, Product
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from main import create_app, db
import utills
import json
import logging



log = logging.getLogger(__name__)

app = create_app()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_product', methods=('GET', 'POST'))
def add_product():
    """
    This API get called when we add new product in DB
    :return:
    """
    log.debug("Adding product in store")
    try:
        if request.method == 'POST':
            product = request.form['prd_name']
            prd_id = request.form['prd_code']
            price = request.form['prd_price']

            if not product:
                flash('Product is required!')
            else:
                new_product = Product(product_code=prd_id,
                                      product_name=product,
                                      price=price)
                db.session.add(new_product)  # Adds new User record to database
                db.session.commit()
            log.debug("Product added successfully")
            return make_response(f"{new_product} successfully created!")

        return render_template('add_product.html')

    except IntegrityError as err:
        db.session.rollback()
        log.debug("Product is already exist!")
        return make_response("Product is already exist!")
    except:
        log.debug("Something went wrong while adding product!")
        return make_response("Something went wrong while adding product!")


@app.route('/show_product', methods=('GET',))
def show_product():
    """
    It show top 10 exist product in DB
    :return:
    """
    context = Product.query.all()[0:10]
    return render_template('show_product.html', context=context)


@app.route('/add_product_in_cart', methods=('GET', 'POST'))
def add_product_in_cart():
    """
    This api add chosen product in cart and call utills function to
    check promo code is applicable .It get call when we submit shopping cart
    form, it fetch all values from form .
    :return:
    """
    log.debug("Calling add_product_in_Cart function")
    if request.method == 'POST':
        #new_product = ''
        data = request.form
        quant_cd_map = {}
        disc_price = 0
        total_price = 0
        final_price = 0
        apply_cd_dict = {}
        for item in data.items():
            vals = item[0].split("___")
            quant_cd_map[vals[1]] = [vals[1], vals[2], item[1]]
        log.debug("Calculating discount price")
        disc_price, apply_cd_dict = utills.apply_code(quant_cd_map)
        log.debug("Calculating total price without discount")
        total_price, total_item_dict = utills.calculate_price(quant_cd_map)
        total_price = float("{:.2f}".format(total_price))
        disc_price = float("{:.2f}".format(disc_price))
        log.debug("Calculating total bill including discount")
        final_price = disc_price + total_price
        final_price = float("{:.2f}".format(final_price))
        return render_template('get_bill.html', final_price=final_price, disc_price=disc_price, \
                               apply_cd_dict=apply_cd_dict, total_price=total_price, total_item_dict=total_item_dict, condition=True)

    context = Product.query.all()[0:10]
    return render_template('show_product_for_cart.html', context=context)


@app.route('/delete/<string:id>', methods=('GET', 'POST'))
def delete(id):
    """
    Delete the item in the database that matches the specified
    id in the URL
    """
    try:
        log.debug("Deleting product")
        qry = db.session.query(Product).filter(Product.product_code == id)
        del_obj = qry.first()
        val = del_obj
        if del_obj:
            db.session.delete(del_obj)
            db.session.commit()
            log.debug("successfully deleted")
            return make_response("{} successfully deleted!".format(val))
        else:
            return 'Error deleting #{id}'.format(id=id)
    except SQLAlchemyError as e:
        db.session.rollback()
        error = str(e.__dict__['orig'])
        log.debug("Something went wrong")
        return make_response("Something went wrong while deleting products!")


@app.route('/get_bill', methods=('GET', 'POST'))
def get_bill():
    """
    This api add chosen product in cart and call utills function to
    check promo code is applicable .It get call when we click on get bill button ,
    it fetch all values from request data , we are passing all inputs from JS .
    :return:
    """
    context = ""
    # data = request.form

    log.debug("Calling get_bill function")
    quant_cd_map = {}
    disc_price = 0
    total_price = 0
    final_price = 0
    apply_cd_dict = {}
    data = json.loads(str(request.data, encoding='utf-8'))

    for item in data.items():
        vals = item[0].split("___")
        if len(vals) > 2:
            quant_cd_map[vals[1]] = [vals[1], vals[2], item[1]]
    log.debug("Calculating discount price")
    disc_price, apply_cd_dict = utills.apply_code(quant_cd_map)
    total_price, total_item_dict = utills.calculate_price(quant_cd_map)
    log.debug("Calculating total price without discount")
    total_price = float("{:.2f}".format(total_price))
    disc_price = float("{:.2f}".format(disc_price))
    log.debug("Calcualating total bill including discount")
    final_price = disc_price + total_price
    final_price = float("{:.2f}".format(final_price))

    return render_template('get_bill.html', final_price=final_price, disc_price=disc_price,\
                           apply_cd_dict=apply_cd_dict, total_price=total_price, total_item_dict=total_item_dict, condition=False)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)