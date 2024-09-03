from backend.celery import app


@app.task()
def temp():
    return 1
