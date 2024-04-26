from flask import jsonify


def response(message, status):
    """Standard response"""
    return jsonify({"message": message, "status": status}), status
