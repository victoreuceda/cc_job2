import subprocess

def check_sudo():
    try:
        # Attempt to execute a harmless command with sudo
        result = subprocess.run(["sudo", "id"], check=True)
        print("This container has sudo privileges.")
    except subprocess.CalledProcessError:
        print("This container does not have sudo privileges.")

if __name__ == "__main__":
    check_sudo()
