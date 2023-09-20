. venv/bin/activate
pip freeze > requirements.txt
chmod +x ./entrypoint.sh
docker compose up -d --build
./manage.py startapp taskapp
docker exec -it django /bin/sh
./manage.py shell
sudo chmod -R 'permissionNumber' 'folder'

tp1.delay()
tp1.delay()
tp2.delay()
tp2.delay()
tp3.delay()
tp3.delay()
tp4.delay()
tp4.delay()
tp1.delay()
tp2.delay()
tp3.delay()
tp4.delay()

from celery import group
from newapp.tasks import tp1,tp2,tp3,tp4
task_group = group(tp1.s() ,tp2.s() ,tp3.s() ,tp4.s() )
task_group.apply_async()


from celery import chain
from newapp.tasks import tp1,tp2,tp3,tp4
task_chain = chain(tp1.s() ,tp2.s() ,tp3.s() ,tp4.s())
task_chain.apply_async()