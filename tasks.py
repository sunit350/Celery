from celery import Celery


app = Celery('tasks', backend=None, broker='redis://localhost:6379/0')


@app.task(name='tasks.add')
def add(x, y):
	total = x + y
	print('{} + {} = {}'.format(x, y, total))


if __name__ == '__main__':