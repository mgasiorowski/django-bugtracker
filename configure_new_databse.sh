mysql -u root < database_config.sql
python manage.py migrate auth
python manage.py migrate
python manage.py loaddata database_data.json