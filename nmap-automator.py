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
    print(print_intro())

if __name__ == "__main__":
    main()