from typing import Optional


def task_done_callback(tasks: Optional, task_id: str):
    def callback(task):
        try:
            result = task.result()
            tasks[task_id]['status'] = 'completed'
            tasks[task_id]['result'] = result
        except Exception as e:
            tasks[task_id]['status'] = 'failed'
            tasks[task_id]['result'] = str(e)
    return callback
