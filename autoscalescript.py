import time, psutil
from googleapiclient import discovery
from google.oauth2 import service_account

PROJECT_ID = "My First Project"
ZONE = "us-central1-a"
MACHINE_TYPE = "e2-medium"
IMAGE = "projects/debian-cloud/global/images/family/debian-11"
SERVICE_ACCOUNT_FILE = ""/home/vboxuser/sylvan-faculty-452803-v7-2586296d692a.json"

def create_vm():
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE)
    compute = discovery.build("compute", "v1", credentials=creds)
    config = {
        "name": "autoscale-vm",
        "machineType": f"zones/{ZONE}/machineTypes/{MACHINE_TYPE}",
        "disks": [{"boot": True, "autoDelete": True, "initializeParams": {"sourceImage": IMAGE}}],
        "networkInterfaces": [{"network": "global/networks/default", "accessConfigs": [{"type": "ONE_TO_ONE_NAT"}]}]
    }
    compute.instances().insert(project=PROJECT_ID, zone=ZONE, body=config).execute()

while True:
    if psutil.cpu_percent(interval=5) > 75 or psutil.virtual_memory().percent > 75:
        print("High usage detected, creating GCP VM...")
        create_vm()
        break
    time.sleep(10)
