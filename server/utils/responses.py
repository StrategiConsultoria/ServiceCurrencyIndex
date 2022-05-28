from flask import jsonify


class ResponseErrors():
    """_class with format for responses in error"""

    def __init__(self, message, request) -> None:
        """_entry values and set in value the format
        :entry:
            :message: str -> 'Message of error'
            :args: _description_
            :form: (_type_): _description_
            :method: str -> 'GET','POST' -> request.method
        """
        self.value = jsonify(
            {"error": message, "args": request.args, "form": request.form, "method": request.method})
