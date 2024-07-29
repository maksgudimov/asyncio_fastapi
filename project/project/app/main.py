import asyncio
import json
import uuid

from fastapi import FastAPI, Response
from models import Operations
from tasks import do_operation

from uuid import uuid4

app = FastAPI()


tasks = {}


endpoint = "/api/operations"


@app.post(endpoint)
async def create_operation(operation: Operations):
    task_id = str(uuid4())
    tasks[task_id] = {"status": "in_progress"}
    operation_task = asyncio.create_task(do_operation(
        operation_dict=dict(operation), tasks=tasks, task_id=task_id
    ))
    print(tasks)
    return task_id


@app.get(f"{endpoint}" + "/{task_id}")
async def read_operations(task_id: str):
    try:
        uuid_task_id = uuid.UUID(task_id)
        return tasks[str(uuid_task_id)]["result"]
    except Exception as exp:
        print(exp)
        return Response(status_code=400)


@app.get(f"{endpoint}")
async def list_tasks():
    return [{"task_id": task_id, "status": task_info['status']}
            for task_id, task_info in tasks.items()]
