from flask import Flask, request, render_template
from models import User, db
from form import RegistrationForm
from flask_wtf import CSRFProtect
from encryption import encryption_pass


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db.init_app(app)


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('OK')


@app.cli.command('get-users')
def get_users():
    users = User.query.all()
    return list(users)


@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        name = form.name.data
        second_name = form.second_name.data
        email = form.email.data
        password = form.password.data
        user = User(name=name,
                    second_name=second_name,
                    email=email,
                    password=encryption_pass(password))
        db.session.add(user)
        db.session.commit()
    return render_template('form.html', form=form)
