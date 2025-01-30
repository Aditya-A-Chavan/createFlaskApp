import argparse
from createFlaskAppBackend.main import main1
import os

def main():
    parser = argparse.ArgumentParser(description="A bot that creates flask app directory structure and files along with boilerplate code.")
    parser.add_argument("-docker", action="store_true", help="Include Dockerfile and docker-compose configuration.")
    parser.add_argument("-port", type=int, help="Port number for the flask app.", dest="port", default=8080)
    parser.add_argument("-extraDirs", nargs="+", help="Extra directories to create.")

    args = parser.parse_args()
    currDirs = os.getcwd()
    
    docker = False
    if args.docker:
        docker = True
        print("docker mode is enabled.")
    
    if args.port:
        print(f"Port number is {args.port}")
    
    extraDirs = None
    if args.extraDirs:
        extraDirs = args.extraDirs
        print(f"Extra directories are {args.extraDirs}")
    
    main1(extraDirs, currDirs, docker)

    print(f"Current directory is {currDirs}")

if __name__ == "__main__":
    main()
