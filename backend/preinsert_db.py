import subprocess

from db.session import SessionLocal
from models import Button
from time import sleep
sleep(10)
print("Updating database")
subprocess.run(["sh", "./alembic-recreate.sh"])
print("Finished updating database")

print("Inserting data")

with SessionLocal() as db:
    button = Button(id=123242, place="Первый лежак")
    button2 = Button(id=123243, place="Второй лежак")

    db.add(button)
    db.add(button2)

    db.commit()

print("Inserted all data")
