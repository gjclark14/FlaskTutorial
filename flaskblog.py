from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

# __name__ is the name of the module
app = Flask(__name__)

# This key was obtained by running
# import secrets
# secrets.token_hex(16)
app.config['SECRET_KEY'] = '36cec8a6d52cdf30ef725e83a4d7ce07'

posts = [
    {
        'author': 'Gabe Clark',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': '1 August 2021'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': '2 August 2021'

    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Login failed. Please check username and password.', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)
