from redis import Redis
from rq import Queue

queue=Queue(connection=Radis(
    host="localhost",
    port="6379"
))