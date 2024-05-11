from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os
from flask_mail import Mail, Message

app = Flask(__name__)


# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///myfirstwebdb.db"# initialize the app with the extension
# db.init_app(app)
db = SQLAlchemy(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'banvro07@gmail.com'
app.config['MAIL_PASSWORD'] = 'oshs dtpb bnvt etfw'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

# app.config['MAIL_SERVER'] = 'smtp.gmail.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USE_SSL'] = False
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USERNAME'] = "banvro07@gmail.com"
# app.config['MAIL_PASSWORD'] = "oshs dtpb bnvt etfw"

# mail = Mail(app)


class ContactUs(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fullname = db.Column(db.String, nullable=False)
    email = db.Column(db.String)
    phone_number = db.Column(db.Integer)
    message = db.Column(db.Text)
    image_path = db.Column(db.String)
    date = db.Column(db.DateTime, server_default=db.func.now())


with app.app_context():
    db.create_all()

@app.route("/")
def homagepage():
    return render_template("home.html")

@app.route("/about")
def ageepage():
    return render_template("about.html")

@app.route("/contact")
def cntactpage():
    return render_template("contact.html")

@app.route("/services")
def servicespage():
    data = ContactUs.query.all()

    return render_template("services.html", mydata = data)

@app.route("/saveing-data", methods = ["POST"])
def savethisdata():
    if request.method == "POST":
        fullname = request.form.get("fname") 
        emaill = request.form.get("email")
        phonuber = request.form.get("pnumber")
        mesage = request.form.get("msg")
        image = request.files.get("img")

        if image:
            image.save(os.path.join("static/userimage", image.filename))
            path = os.path.join("static/userimage", image.filename)

        page = ContactUs(fullname = fullname, email = emaill, phone_number = phonuber, message = mesage, image_path = path)
        db.session.add(page)
        db.session.commit()

        # sendthis = Message("Test Mail",sender = "banvro@gmail.com", recipients=["banvro07@gmail.com"])
        # sendthis.body = "this is emage "
        # mail.send(sendthis)

        msg = Message('Hello', sender = 'banvro07@gmail.com', recipients = ['programography@gmail.com'])
        msg.body = "This is the email body"
        mail.send(msg)

        return redirect("/services")
    return "data ssavedf"



@app.route("/deletethisdata/<int:xyz>")
def deletethisnow(xyz):
    data = ContactUs.query.get(xyz)
    db.session.delete(data)
    db.session.commit()
    
    return redirect("/services")


@app.route("/update/<int:abc>")
def updatethis(abc):
    data = ContactUs.query.get(abc)
    return render_template("updatedata.html", data = data)



@app.route("/updatedatanow/<int:abc>", methods = ["POST"])
def updatehtis(abc):
    data = ContactUs.query.get(abc)
    if request.method == "POST":
        fullname = request.form.get("fname") 
        emaill = request.form.get("email")
        phonuber = request.form.get("pnumber")
        mesage = request.form.get("msg")

        data.fullname = fullname
        data.email = emaill
        data.phonuber = phonuber
        data.message = mesage

        db.session.commit()

        return redirect("/services")



if __name__ == "__main__":
    app.run(debug = True)