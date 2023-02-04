from flask import Flask, render_template,request,redirect,url_for,flash
from pymongo import MongoClient


app = Flask(__name__)
app.config["SECRET_KEY"]="dhawjofhQWUIHQW"
client = MongoClient()
db = client['pythondb']
collection = db['subscribers']


@app.route("/")
def index():    
    for subscriber in db.subscribers.find():
        print(subscriber)
    return render_template("index.html")



@app.route("/auth/login")
def login():
    return render_template("login.html")



@app.route("/auth/register", methods=["POST","GET"])
def register():
    if request.method == "POST":       
        user_data = {
                    "name":request.form["name"],
                    "mobile":request.form["mobile"],
                    "email":request.form["email"],
                    "password":request.form["password"]
                    }
        
        try:
            db.subscribers.insert_one(user_data)  
            flash("Registration Successfull, Kindly Login to continue...")          
            
        except:
            print("ERROR: Could not write to database...")
            
            
        return redirect(url_for('login'))

    return render_template("register.html")


if __name__ == '__main__':
    app.run(debug=True)
