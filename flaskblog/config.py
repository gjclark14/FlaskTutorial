class Config:
    SECRET_KEY = '36cec8a6d52cdf30ef725e83a4d7ce07'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    # information with an email and password to send emails to for the password reset function
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''
