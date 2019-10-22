#!/usr/bin/python
# -*- coding: UTF-8 -*-

from celery import Celery

app = Celery('tasks')
app.config_from_object('celeryconfig')

if __name__ == '__main__':
    app.start()