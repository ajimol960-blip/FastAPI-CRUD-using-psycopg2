from fastapi import FastAPI
import psycopg2
from sample import conn
import schemas


# Create FastAPI app
app=FastAPI()
@app.get("/")
def home():
    return{"Message":"Welcome"}

@app.get("/tasks")
def get_tasks():
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks ORDER BY id ASC")
    rows = cur.fetchall()
    cur.close()

    return rows

#create API
@app.post("/tasks")
def create_task(task: schemas.Task):
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO tasks (title, is_completed) VALUES (%s, %s)",
        (task.title, task.is_completed)
    )

    conn.commit()
    cur.close()

    return {"message": "Task created successfully"}

#UPDATE API (Update task completion)

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: schemas.Task):
    cur = conn.cursor()

    cur.execute(
        "UPDATE tasks SET title=%s, is_completed=%s WHERE id=%s",
        (task.title, task.is_completed, task_id)
    )

    conn.commit()
    cur.close()

    return {"message": "Task updated successfully"}


#DELETE API (Delete task)
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM tasks WHERE id = %s",
        (task_id,)
    )

    conn.commit()
    cur.close()

    return {"message": "Task deleted successfully"}







