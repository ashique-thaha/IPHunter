import socket
import argparse
import os

def is_alive(ip):
    try:
        # Try to create a socket connection to the IP address
        socket.create_connection((ip, 80), timeout=2)
        return True
    except (socket.timeout, socket.error):
        return False

def print_ascii_title():
    title = """

 ___ ____  _   _ _   _ _   _ _____ _____ ____  
|_ _|  _ \| | | | | | | \ | |_   _| ____|  _ \ 
 | || |_) | |_| | | | |  \| | | | |  _| | |_) |
 | ||  __/|  _  | |_| | |\  | | | | |___|  _ < 
|___|_|   |_| |_|\___/|_| \_| |_| |_____|_| \_\
                                               
                                   
"""
    print(title)

def main():
    parser = argparse.ArgumentParser(description="Check if domains or IPs are alive and save results to a folder.")
    parser.add_argument("input_file", help="Path to the file containing a list of IPs or domains.")
    parser.add_argument("-o", "--output-folder", help="Name of the folder to save output files.")
    args = parser.parse_args()

    with open(args.input_file, "r") as file:
        ip_list = file.read().splitlines()

    # Create the output folder if it doesn't exist
    output_folder = args.output_folder
    os.makedirs(output_folder, exist_ok=True)

    alive_output_file = os.path.join(output_folder, "alive.txt")
    dead_output_file = os.path.join(output_folder, "dead.txt")

    print_ascii_title()

    for ip in ip_list:
        status = "alive" if is_alive(ip) else "dead"
        print(f" {ip} is {status}")

    with open(alive_output_file, "w") as alive_file, open(dead_output_file, "w") as dead_file:
        for ip in ip_list:
            if is_alive(ip):
                alive_file.write(f"{ip}\n")
            else:
                dead_file.write(f"{ip}\n")

    print(f"Results saved to {output_folder}.")

if __name__ == "__main__":
    main()
