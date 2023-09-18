import os
import datetime
from flask import Flask
from google.cloud import storage
from threading import Thread

app = Flask(__name__)

@app.route("/")
def create_backup():
    data = f"{datetime.datetime.now().day}-{datetime.datetime.now().month}"

    os.system(f"sh ./backup-via-apiv3.sh && tar -cf 4projects.bkp-{data}.tar /backup/files/attachment/ /app/openproject.sql.zip")

    Thread(target = send_backup).start()
    return (f'Upload do dia {data} sendo enviado como: "4projects.bkp-{data}.tar".')

def send_backup():
    data = f"{datetime.datetime.now().day}-{datetime.datetime.now().month}"

    storage_client = storage.Client(project="serene-courier-198218")
    bucket = storage_client.bucket("backup-4projects")
    blob = bucket.blob(f"4projects.bkp-{data}.tar")

    blob.upload_from_filename(f"/app/4projects.bkp-{data}.tar")
    print("Backup enviado")

    os.system("rm -rf /app/4projects.bkp* && rm -rf /app/openproject.sql*")
    print("Arquivos locais removidos")
