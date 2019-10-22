# celeryDemo

lcy@lcy proj % celery -A app_test worker -l info

# new terminal

python diaoyong.py


redis 表2 为中间件

celery flower --broker=redis://localhost:6379/2
