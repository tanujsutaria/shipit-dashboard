from flask import Blueprint,jsonify,request
from . import db
from .models import Order

main = Blueprint('main', __name__)

@main.route('/orders', methods = ['GET'])
def get_orders():
    """"""
    orders = []
    orders_list = Order.query.all()
    for order in orders_list:
        orders.append({
            'pk' : order.pk,
            'order_number' : order.order_number,
            'order_status' : order.order_status,
            'order_created_date' : order.order_created_date,
            'order_finished_date' : order.order_finished_date,
            'order_target_finish_date' : order. order_target_finish_date,
            'order_late_comment' : order.order_late_comment
        })
    return jsonify({'Orders':orders})

@main.route('/add_order', methods = ['POST'])
def add_order():
    """POST request connected to webhook that automatically adds the order into the database"""
    order_data = request.get_json()
    new_order = Order(
        pk = order_data['pk'],
        order_number = order_data['order_number'],
        order_status = order_data['order_status'],
        order_created_date = order_data['order_created_date'],
        order_finished_date = order_data['order_finished_date'],
        order_target_finish_date = order_data['order_target_finish_date'],
        order_late_comment = order_data['order_late_comment']
    )
    db.session.add(new_order)
    db.session.commit()
    return 'Done', 201

