# -*- coding:utf-8 -*-

BROKER_URL = 'redis://localhost'  # 使用RabbitMQ作为消息代理

CELERY_TASK_PROTOCOL = 1  # 现在celery升级到了4.0，是老版本的librabbitmq与最新的celery4.0 Message Protocol协议不兼容，celery4.0默认使用Task messages Version 2 ，而librabbitmq使用Task messages Version 1

CELERY_RESULT_BACKEND = 'redis://localhost:6379/1' # 把结果存在Redis

CELERY_TASK_SERIALIZER = 'msgpack'  # 任务序列化肯反序列化使用msgpack方案

CELERY_RESULT_SERIALIZER = 'json'   # 读取任务结果一般性能要求不高，所以使用可读性更好的json

CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24  # 任务过期时间

CELERY_ACCEPT_CONTENT = ['json', 'msgpack'] # 指定接收的内容类型

CELERY_IMPORTS = ("tasks",)

