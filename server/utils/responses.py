from flask import jsonify


class ResponseErrors():
    def __init__(self, message, args, form, method):
        self.value = jsonify(
            {"error": message, "args": args, "form": form, "method": method})
