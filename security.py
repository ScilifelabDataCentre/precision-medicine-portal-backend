import os

import functools
from flask import request
from flask_smorest import abort

def is_valid(api_key):
    return os.getenv("API_KEY") == api_key

def api_key_required(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        api_key = request.headers.get("x-api-key")
        print("headers: ")
        for item in list(request.headers):
            print(item)
        print("api_key: ")
        print(api_key)
        if not api_key:
            abort(
                400, 
                message="Please provide an API key."
            )
        # Check if API key is correct and valid
        if is_valid(api_key):
            return func(*args, **kwargs)
        else:
            abort(
                403, 
                message="The provided API key is not valid."
            )
    return decorator