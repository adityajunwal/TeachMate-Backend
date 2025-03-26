from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4

taskRouter = APIRouter(
    prefix="/taskmanager",
    tags=["Task Manager"]
)

tasks = []

class Task(BaseModel):
    id: Optional[UUID] = None
    title: str
    description: Optional[str] = None
    completed: bool = False

@taskRouter.post("/", response_model=Task)
def create_task(task: Task):
    task.id = uuid4()
    tasks.append(task)
    return task    


@taskRouter.get("/", response_model=List[Task])
def read_tasks():
    return tasks

@taskRouter.get("/", response_model=Task)
def read_task(task_id: UUID):
    for task in tasks:
        if task.id == task_id:
            return task
    
    raise HTTPException(status_code=404, detail="TASK NOT FOUND!!!")

@taskRouter.put("/", response_model=Task)
def update_task(task_id: UUID, task_update: Task):
    for idx, task in enumerate(tasks):
        if task.id == task_id:
            updated_task = task.copy(
                update=task_update.model_dump(exclude_unset=True)
            )
            tasks[idx] = updated_task
            return updated_task

    raise HTTPException(status_code=404, detail="TASK NOT FOUND!!!")

@taskRouter.delete("/", response_model=Task)
def delete_task(task_id: UUID):
    for idx, task in enumerate(tasks):
        if task.id == task_id:
            return tasks.pop(idx)

    raise HTTPException(status_code=404, detail="TASK NOT FOUND!!!")