# vconnect


py -m pip install whitenoise
py -m pip freeze > requirements.txt
python manage.py collectstatic


✅ 6. Deploy on Render
Go to https://render.com

Create an account (or log in)

Click New Web Service

Connect your GitHub repo

Fill in:

Build Command: pip install -r requirements.txt

Start Command: gunicorn project.wsgi:application

Environment: Python 3.x

Add Environment Variables:

SECRET_KEY → your secret key

DEBUG → False