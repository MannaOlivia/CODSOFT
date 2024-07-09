from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for tasks
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    task_date = request.form.get('task_date')  # Get selected date from form

    if task:
        new_task = {'task': task, 'date': task_date}
        tasks.append(new_task)

    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('index'))

@app.route('/clear_completed', methods=['POST'])
def clear_completed_tasks():
    tasks.clear()  # Clear all tasks
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
