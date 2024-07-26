import asyncio
import uuid
from typing import Dict


async def do_operation(operation_dict: Dict, tasks: Dict, task_id: str):
    await asyncio.sleep(5)
    if operation_dict['operation'] == '+':
        result = int(operation_dict['x']) + int(operation_dict['y'])
        tasks[task_id] = {"status": "completed", "result": result}
        return result
    if operation_dict['operation'] == '-':
        result = int(operation_dict['x']) - int(operation_dict['y'])
        tasks[task_id] = {"status": "completed", "result": result}
        return result
    if operation_dict['operation'] == '*':
        result = int(operation_dict['x']) * int(operation_dict['y'])
        tasks[task_id] = {"status": "completed", "result": result}
        return result
    if operation_dict['operation'] == '/':
        try:
            result = int(operation_dict['x']) / int(operation_dict['y'])
            tasks[task_id] = {"status": "completed", "result": result}
            return result
        except ZeroDivisionError:
            tasks[task_id] = {"status": "failed", "result": 0}
            return 0
