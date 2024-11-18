import os
from pathlib import Path
import subprocess
import pwd

root_password = "dees"
target_user = "Joe"
target_password = "joe_password"

subprocess.run(f"sudo useradd -m {target_user} && echo '{target_user}:{target_password}' | sudo chpasswd", shell=True)
subprocess.run(["usermod", "-aG", "sudo", target_user], check=True)
print(f"Added {target_user} to the sudo group.")
home_path = Path(f"/home/{target_user}")
file_name = "my_password"
file_path = home_path / file_name
file_path.write_text("root password: {root_password}\nMy password: Doe")
print(f"File created at {file_path} with the root password")
os.chown(file_path, uid=pwd.getpwnam(target_user).pw_uid, gid=pwd.getpwnam(target_user).pw_gid)

subprocess.run(["su", "-", target_user])