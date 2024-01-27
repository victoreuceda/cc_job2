import os
import socket
import subprocess

def check_file_access():
    print("\nChecking File Access:")
    sensitive_files = ["/etc/passwd", "/root/.ssh/", "/var/run/docker.sock"]
    for file in sensitive_files:
        if os.path.exists(file):
            print(f"Access to {file} is possible.")
        else:
            print(f"Access to {file} is not possible.")

def check_permission_change():
    print("\nChecking Permission Change:")
    test_file = "/etc/passwd"
    try:
        subprocess.run(["sudo", "chmod", "777", test_file], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"Permission change on {test_file} successful.")
        # Revert permission change for safety
        subprocess.run(["sudo", "chmod", "644", test_file], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        print(f"Permission change on {test_file} not possible.")

def check_privileged_port_binding():
    print("\nChecking Privileged Port Binding:")
    privileged_port = 80
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind(("", privileged_port))
        print(f"Binding to privileged port {privileged_port} successful.")
    except OSError:
        print(f"Binding to privileged port {privileged_port} failed.")
    finally:
        s.close()

if __name__ == "__main__":
    check_file_access()
    check_permission_change()
    check_privileged_port_binding()
