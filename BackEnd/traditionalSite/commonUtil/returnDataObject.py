def success_json_response(message, data, status="success"):
    data = {
        "code": 200,
        "status": status,
        "message": message,
        "data": data
    }
    return data


def fail_json_response(message, data, code=300):
    data = {
        "code": code,
        "status": "fail",
        "message": message,
        "data": data
    }
    return data


def error_json_response(message, data, code=400):
    data = {
        "code": 400,
        "status": "error",
        "message": message,
        "data": data
    }
    return data


def bug_json_response(message, data):
    data = {
        "code": 500,
        "status": "bug",
        "message": message,
        "data": data
    }
    return data


def info_json_response(message, data):
    data = {
        "code": 201,
        "status": "info",
        "message": message,
        "data": data
    }
    return data
