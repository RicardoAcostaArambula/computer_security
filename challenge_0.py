from pathlib import Path
#Script that creates a file with the root password under home directory
rootPassword = "dees"
homePath = Path.home()
fileName = "my_password"
filePath = homePath / fileName
filePath.write_text(f"root password: {rootPassword}\n")
print(f"File created at {filePath} with the root password")
