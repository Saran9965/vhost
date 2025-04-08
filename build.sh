
pip install -r requirements.txt

python manage.py collectstatic --no-input

python manage.py migrate

python -m pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate

