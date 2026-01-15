from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        message = request.form.get("message")
        return f"Thank you {name}, your message was received!"

    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)
