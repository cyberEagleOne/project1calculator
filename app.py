from flask import Flask, render_template, request

app = Flask(__name__)

# Fungsi operasi matematika
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    error = None
    num1 = num2 = ""
   
    if request.method == "POST":
        operation = request.form.get("operation")
       
        # Cek tombol "Clear" ditekan
        if operation == "Clear":
            return render_template("index.html", result=None, error=None, num1="", num2="")

        try:
            num1 = request.form["num1"]
            num2 = request.form["num2"]
            num1 = float(num1) if num1 else 0
            num2 = float(num2) if num2 else 0

            if operation == "Add":
                result = add(num1, num2)
            elif operation == "Subtract":
                result = subtract(num1, num2)
            elif operation == "Multiply":
                result = multiply(num1, num2)
            elif operation == "Divide":
                result = divide(num1, num2)
        except ValueError:
            error = "Please enter valid numbers."

    return render_template("index.html", result=result, error=error, num1=num1, num2=num2)

if __name__ == "__main__":
    app.run(debug=True)
