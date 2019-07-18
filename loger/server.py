from sanic import Sanic, response

app = Sanic()


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8080
    )