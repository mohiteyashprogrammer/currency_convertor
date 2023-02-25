from flask import Flask,render_template,request

application =  Flask(__name__)
app = application

@app.route("/",methods = ["GET"])
def hello_world():
    return render_template("index.html")

@app.route("/currencyconverator", methods = ["POST"])
def currency_converator():
    if request.method == "POST":
        amount = int(request.form["amount"])
        currency = request.form["currency"]
        try:
            with open("currency.txt")as f:
                lines = f.readlines()
            #read data
                lines
            # conver data in to dict and take only 2 values
            dictionary = {}
            for i in lines:
                parsed = i.split("\t")# split data with \t
                dictionary[parsed[0]] = parsed[1]
            result = f"{amount} INR is equal to {amount * float(dictionary[currency])} {currency}"
        except Exception as e:
            print(e)

    return render_template("result.html",result=result)


if __name__=="__main__":
    app.run(host="0.0.0.0")