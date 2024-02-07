# Function to print intro
def print_intro():
    banner = f"""
               **************************************************
               *                                                *
               *      Welcome to Automated Network Scanner      *
               *                                                *
               * Warning: This tool is intended for educational *
               *               purposes only!                   *
               *                                                *
               *            https://github.com/fmazmz           *
               *                                                *
               *   Read more about NMAP at: https://nmap.org/   *    
               **************************************************
"""
    return(banner)

# Main Function
def main():

    # Print intro
    print(print_intro())

    # Inputs (Modify this to your liking)
    ip = "192.168.1.1/24"
    script = "vuln"  # Leave empty for no scripts
    ports = "445,80"  # Leave empty for ports 1-1000 / "-p-" for all ports
    scan_type = "-sV -sT"  # Leave empty for SYN scan

if __name__ == "__main__":
    main()