from flask import Blueprint,jsonify,request
from . import db
from .models import Order
from flask_socketio import socketio

main = Blueprint('main', __name__)

@main.route('/orders', methods = ['GET'])
def get_orders():
    """GET Request to get all orders in the database"""
    orders = []
    orders_list = Order.query.all()
    for order in orders_list:
        orders.append({
            'ordr_pk' : order.ordr_pk,
            'ordr_barCode' : order.ordr_barCode,
            'stts_name' : order.stts_name,
            'ordr_createdBy' : order.ordr_createdBy
        })
    return jsonify({'Orders':orders})

@main.route('/add_order', methods = ['POST'])
def add_order():
    """POST request connected to webhook that automatically adds the order into the database"""
    order_data = request.get_json()
    new_order = Order(
        ordr_pk = order_data['pk'],
        ordr_barCode = order_data['columns']['ordr_barCode']['value'],
        stts_name = order_data['columns']['stts_name']['value'],
        ordr_createdBy = order_data['columns']['ordr_createdBy']['value']
    )
    db.session.add(new_order)
    db.session.commit()
    return 'Done', 201

@main.route('/update_order', methods = ['POST'])
def update_order():
    """POST request connected to webhook that automatically update the order in the database"""
    order_data = request.get_json()
    if(order_data['pk']):
        order = Order.query.filter_by(ordr_pk=order_data['pk'])
        if(order):
            order.update(dict(
                ordr_barCode = order_data['columns']['ordr_barCode']['value'],
                stts_name = order_data['columns']['stts_name']['value'],
                ordr_createdBy = order_data['columns']['ordr_createdBy']['value']
                    ))
            db.session.commit()
            return 'Done', 201
        else:
            return 'Order specificied not found',404
    else:
        return "Please POST request with pk"