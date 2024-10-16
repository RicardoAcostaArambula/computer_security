import os

rootPassword = "toor"
homeDirectory = os.path.expanduser("~")
desktopPath = os.paht.join(homeDirectory, "Desktop")
fileName = "my_password"
filePath = os.path.join(desktopPath, fileName)
with open(filePath, "w") as file:
    file.write(f"root password: {rootPassword}")

print(f"File created at {filePath} with the root password")
