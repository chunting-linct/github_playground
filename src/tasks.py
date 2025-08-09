from celery import Celery 

app = Celery('tasks', broker='redis://redis', backend='redis://redis')



@app.task(queue='crop_queue')
def test_task(input):

    print(f"successfully get input : {input}")
    return input