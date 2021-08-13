import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail

def save_picture(form_picture_data):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture_data.filename)
    picture_filename = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static', 'profile_pics', picture_filename)

    prev_picture = os.path.join(app.root_path, 'static', 'profile_pics', current_user.image_file)
    if os.path.exists(prev_picture):
        os.remove(prev_picture)

    output_size = (125, 125)
    image = Image.open(form_picture_data)
    image.thumbnail(output_size)
    image.save(picture_path)

    return picture_filename


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='noreply@demo.com',
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}
If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)
