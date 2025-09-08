from flask import Flask, jsonify, session as flask_session, redirect, url_for, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.secret_key = "change-me"  # required for session cookies


@app.get("/api/health")
def health():
    return jsonify({"status": "ok"})


@app.get("/api/greet/<name>")
def greet(name: str):
    return jsonify({"message": f"Hello, {name}!"})


@app.route("/")
def home():
    if "username" in flask_session:
        return f"Logged in as {flask_session['username']}"
    return "You are not logged in"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        flask_session["username"] = request.form["username"]
        return redirect(url_for("home"))
    return (
        """
        <form method="post">
            Username: <input type="text" name="username"><br>
            <input type="submit" value="Login">
        </form>
        """
    )


@app.route("/logout")
def logout():
    flask_session.pop("username", None)
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)


