import os
from sys import exit, stdout
from time import sleep
import boto3
from dotenv import load_dotenv
from paramiko import AuthenticationException, AutoAddPolicy, SSHClient, SSHException

load_dotenv()

aws_access_key = os.getenv("aws_access_key")
aws_secret_access_key = os.getenv("aws_secret_access_key")
frontend_instance_id = os.getenv("frontend_instance_id")
backend_instance_id = os.getenv("backend_instance_id")
fronted_key_filename = os.getenv("fronted_key_filename")
backend_key_filename = os.getenv("backend_key_filename")

ec2 = boto3.client(
    "ec2",
    "eu-west-2",
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_access_key,
)

# Start AWS backend instance
try:
    print("Starting AWS backend instance...")
    response = ec2.start_instances(InstanceIds=[backend_instance_id])
    backend_instance = ec2.Instance(backend_instance_id)
    backend_instance.wait_until_running()
    backend_instance.reload()
    ip_backend = backend_instance.public_ip_address
    print("AWS backend instance successfully started with IP: ", ip_backend)
except Exception as error:
    print("Error starting AWS backend instance: ", error)
    exit()

# Start AWS frontend instance
try:
    print("Starting AWS frontend instance...")
    response = ec2.start_instances(InstanceIds=[frontend_instance_id])
    frontend_instance = ec2.Instance(frontend_instance_id)
    frontend_instance.wait_until_running()
    frontend_instance.reload()
    ip_frontend = frontend_instance.public_ip_address
    print("AWS frontend instance successfully started with IP: ", ip_frontend)
except Exception as error:
    print("Error starting AWS frontend instance: ", error)
    try:
        # Stop backend instance before exiting if frontend instance fails to start
        response = ec2.stop_instances(InstanceIds=[backend_instance_id])
        print("Sent request to stop AWS backend instance before exiting!")
    except Exception as error:
        print(
            "Error sending request to stop AWS backend instance before exiting: ", error
        )
    exit()

# SSH connect to backend instance
try:
    print("Connecting to backend instance through SSH...")
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.connect(
        ip_backend,
        username="ubuntu",
        key_filename=backend_key_filename,
        passphrase="",
        timeout=40,
    )
except:
    print("Error connecting to backend instance through SSH!")
    client.close()
    exit()

# Download latest repository code on backend instance
print("Downloading latest repository code on backend instance...")
stdin, stdout, stderr = client.exec_command(
    """
    cd ~/quirked-up-software;
    git restore .;
    git pull origin production;"
    """
)
print("Donwload complete!")

# Delete previous backend processes (if running)
print("Deleting previous backend processes, if any are running...")
stdin, stdout, stderr = client.exec_command(
    """
    cd ~/quirked-up-software/DEV/backend/main;
    cat save.pid
    """
)
pid = stdout.readline()[:-1]
stdin, stdout, stderr = client.exec_command(f"kill {pid}")
print("Deletion complete!")

# Install backend packages
print("Installing backend packages...")
stdin, stdout, stderr = client.exec_command(
    """
    cd ~/quirked-up-software/DEV/backend;
    pip install -r requirements.txt;
    """
)
print("Installation complete!")

# Start backend
print("Starting backend...")
stdin, stdout, stderr = client.exec_command(
    """
    cd ~/quirked-up-software/DEV/backend;
    python3 manage.py reset_db --noinput;
    python3 manage.py makemigrations --merge --noinput;
    python3 manage.py migrate;
    python3 manage.py runscript init_db;
    gunicorn -p save.pid main.wsgi -b 0.0.0.0:8081 --daemon
    """
)
stdout.channel.wait()

# Verify if backend successfully started
stdin, stdout, stderr = client.exec_command(
    """
    cd ~/quirked-up-software/DEV/backend
    cat save.pid
    """
)
pid = stdout.readline()[:-1]
stdin, stdout, stderr = client.exec_command(f"ps -p {pid}")
if len(stdout.readlines()) > 1:
    print("Backend deployment successful!")
    print("IP: ", ip_backend)
else:
    print("Backend deployment failed!")

# Close SSH connection to backend instance
client.close()
print("SSH connection to backend instance closed!")

# SSH connect to frontend instance
print("Connecting to frontend instance through SSH...")
try:
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.connect(
        ip_frontend,
        username="ubuntu",
        key_filename=fronted_key_filename,
        passphrase="",
        timeout=40,
    )
except:
    print("Error connecting to frontend instance through SSH!")
    client.close()
    exit()
print("SSH connection to frontend instance successful!")

# Download latest repository code on frontend instance
print("Downloading latest repository code on frontend instance...")
stdin, stdout, stderr = client.exec_command(
    """
    cd ~/quirked-up-software;
    git restore .;
    git pull origin production;"
    """
)
print("Donwload complete!")

# Delete previous frontend processes (if running)
print("Deleting previous frontend processes, if any are running...")
client.exec_command(
    """
    cd ~/quirked-up-software/DEV/frontend/;
    pm2 delete all
    """
)
print("Deletion complete!")

# Install frontend packages
print("Installing frontend packages and starting build...")
stdin, stdout, stderr = client.exec_command(
    """
    cd ~/quirked-up-software/DEV/frontend;
    npm install;
    npm run build
    """
)
result = stdout.read().decode("utf-8")
if result.find("Failed") == -1:
    stdin, stdout, stderr = client.exec_command(
        """
        cd ~/quirked-up-software/DEV/frontend;
        pm2 --name Quirked-Up-Software  start npm -- run start_deploy
        """
    )
    print("Frontend deployment successful!")
    print("IP: ", ip_frontend)
else:
    print("Frontend deployment failed!")
    print("Error: ", result)

# Close SSH connection to frontend instance
client.close()
