'''
Kevin Guerra
Startup script to install dependencies needed for 
CS 5352 Team 4 Project

Installations include:
    Ghidra
    Netcat
    Wireshark
    Auditd
If applications are already installed, 
this script will update to ensure consinstency

Also, we assume this is running on Ubuntu 20.04 distro.

Finally, to execute type on terminal
sudo python3 startup.py
'''
import os

def apt_upgrade():
    os.system('sudo apt update')

def install_jdk():
    os.system('sudo apt install openjdk-21-jdk')

def install_ghidra():
    print('Now installing Ghidra')
    install_jdk() # This ghidra needs jdk 21 :(
    os.system('sudo wget --no-check-certificate https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra_11.2_build/ghidra_11.2_PUBLIC_20240926.zip')
    os.system('unzip ghidra_11.2_PUBLIC_20240926.zip')
    os.system('sudo rm ghidra_11.2_PUBLIC_20240926.zip')
    os.system('mv ghidra_11.2_PUBLIC ghidra')
    print('#'*50)
    print('Ghidra installed')
    print('To open, use the command ./ghidraRun through the ghidra/ directory')
    
def install_and_configure_auditd():
    print('Now installing and configuring Auditd...')
    # Install Auditd:
    os.system('sudo apt install auditd audispd-plugins -y')
    
    # Configure Auditd Rules:
    # Get the current working directory (where the repository is cloned):
    repo_path = os.getcwd()
    
    # Define absolute paths for each challenge file
    challenge0_path = os.path.join(repo_path, "Ricardo/challenge_0.py")
    challenge1_path = os.path.join(repo_path, "Ricardo/challenge_1.py")
    challenge2_path = os.path.join(repo_path, "Ricardo/challenge_2.py")
    pcap_file_path = os.path.join(repo_path, "Kevin/TrafficDump_v2.0.pcapng")
    challenge3_path = os.path.join(repo_path, "Task Descriptions/Task3.txt")
    challenge4_path = os.path.join(repo_path, "Jazmin/challenge4.py")
    c5_1_path = os.path.join(repo_path, "Adrian/c5_1.c")
    c5_2_path = os.path.join(repo_path, "Adrian/c5_2.c")
    c5_3_path = os.path.join(repo_path, "Adrian/c5_3.c")
    challenge5_path = os.path.join(repo_path, "Adrian/challenge5.c")

    audit_rules = f"""
    # Track all command executions on machines using 32 and 64 bit arch:
    -a always,exit -F arch=b64 -S execve -k command_tracking
    -a always,exit -F arch=b32 -S execve -k command_tracking
    
    # Track Wireshark usage for Task 3:
    -a always,exit -F arch=b64 -S execve -F exe=/usr/bin/wireshark -k wireshark_usage

    # Track access to Challenges files:
    -w {challenge0_path} -p rwa -k file_access_tracking
    -w {challenge1_path} -p rwa -k file_access_tracking
    -w {challenge2_path} -p rwa -k file_access_tracking
    -w {pcap_file_path} -p rwa -k pcap_access
    -w {challenge3_path} -p rwa -k challenge3_activity
    -w {challenge4_path} -p rwa -k file_access_tracking
    -w {c5_1_path} -p rwa -k challenge5_activity
    -w {c5_2_path} -p rwa -k challenge5_activity
    -w {c5_3_path} -p rwa -k challenge5_activity
    -w {challenge5_path} -p rwa -k challenge5_activity

    # Log failed login attempts
    -w /var/log/auth.log -p wa -k failed_attempts
    """

    with open('/etc/audit/rules.d/ctf.rules', 'w') as f:
        f.write(audit_rules)
    
    # Restart Auditd to apply rules
    os.system('sudo systemctl restart auditd')
    print('#' * 50)
    print('Auditd installed and configured.')
    print("Auditd configured for challenge files:")
    for path in [challenge0_path, challenge1_path, challenge2_path, pcap_file_path, 
                 challenge3_path, challenge4_path, c5_1_path, c5_2_path, c5_3_path, 
                 challenge5_path]:
        print(f" - {path}")
    
def main():
    #apt_upgrade()
    install_ghidra()
    install_and_configure_auditd()

if __name__ == '__main__':
    main()