import os
from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dcelery.settings")
app = Celery("dcelery")
app.config_from_object("django.conf:settings", namespace="CELERY")
# app.conf.task_routes = {
#     "newapp.tasks.task1": {"queue": "queue1"},
#     "newapp.tasks.task2": {"queue": "queue2"},
# }
app.conf.broker_transport_options = {
    "priority_steps": list(range(10)),
    "sep": ":",
    "queue_order_strategy": "priority",
}
base_dir = os.getcwd()
task_folder = os.path.join(base_dir, "dcelery", "celery_tasks")

if os.path.exists(task_folder) and os.path.isdir(task_folder):
    task_modules = []
    for filename in os.listdir(task_folder):
        if filename.startswith("ex") and filename.endswith(".py"):
            module_name = f"dcelery.celery_tasks.{filename[:-3]}"
            module = __import__(module_name, fromlist=["*"])
            for name in dir(module):
                obj = getattr(module, name)
                if callable(obj):
                    task_modules.append(f"{module_name}.{name}")

    app.autodiscover_tasks(task_modules)
