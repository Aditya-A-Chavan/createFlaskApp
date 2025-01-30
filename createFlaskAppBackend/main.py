import os

def createDirs(currDir, extraDirs=None):
    dirs = ["app", "nginx", "app/authentication", "app/utils", "app/toolbox"]
    
    
    if extraDirs:
        for dir in extraDirs:
            dirs.append(dir)

    for dir in dirs:
        os.makedirs(os.path.join(currDir, dir), exist_ok=True)
        print(f"Directory {dir}, created successfully.")

    print("\nAll Directories created successfully.")

def createFiles(currDir, docker=False):
    files = ["Makefile", "Manage.py", "app/__init__.py", "app/config-common.py", "app/config-dev.py", "app/config-prod.py", "app/logger-setup.py", "nginx/Dockerfile", "app/authentication/__init__.py", "app/utils/__init__.py", "app/utils/errorHandler.py", "app/toolbox/__init__.py"]
    
    if docker:
        files.append("Dockerfile")
        files.append(".dockerignore")
        files.append("docker-compose.yml")

    for file in files:
        with open(os.path.join(currDir, file), "w") as f:
            f.write("# Created by createFlaskAppBackend\n")
            print(f"File {file}, created successfully.")

    print("\nAll Files created successfully.")
    

def main1(extraDirs, currDir, docker, dockerCompose):
    createDirs(currDir, extraDirs)
    createFiles(currDir, docker, dockerCompose)

