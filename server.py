from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello_handler():
    name = request.args.get("name", "Mysterious stranger")
    if name == "":
        return "name param can't be empty", 400
    
    message = request.args.get("message", "How are you?")
    if message == "":
        return "message param can't be empty", 400
    
    response = f"Hello {name}! {message}"
    return response

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8174)
