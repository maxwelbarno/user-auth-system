from flask import jsonify


def response(message, status):
    """Standard response"""
    return jsonify({"message": message, "status": status}), status


def response_with_data(message, data, status):
    """response with data"""
    return jsonify({"message": message, "data": data, "status": status}), status
