import os
import stat

challengeDirectory = "/root/challenge"
subDirectories = ["dir1", "dir2", "dir3", "dir4"]
key = "the key is: 17"
fileWithKey = "dir5"
hintMessage ="The key is in one of the files, but not here..."
def setupChallenge():
    os.makedirs(challengeDirectory, exist_ok=True)
    os.chdir(challengeDirectory)

    #creating subdirectories 
    for subdirectory in subDirectories:
        os.makedir(subdirectory, exist_ok=True)
    

        #creating files
        for i in range(1, 4):
            fileName = f"file{i}.txt"
            with open(fileName, "w") as file:
                file.write(hintMessage)
    #choosing one directory to place the password
    keyDirectory = os.path.join(challengeDirectory, "dir5")
    os.chdir(keyDirectory)

    with open(keyDirectory, "w") as file:
        file.write(key)
    protectFiles()
def protectFiles():
    for root, dirs , files in os.walk(challengeDirectory):
        for directoryName in dirs:
            os.chmod(os.path.join(root, directoryName), stat.SIRWXU) 
        for fileName in files:
            os.chmod(os.path.join(root, fileName), stat.S_IRUSR)
if __name__ == "__main__":
    setupChallenge()
    print(f"Challenge setup complete! Files created under {challengeDirectory}")