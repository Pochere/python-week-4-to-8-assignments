import os
 # 1. Reading a file
def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()  #reads the file's content
            print("File content:") #outputs a message indicating the file's content
            print(content) #displays the content in the terminal
            return content #returns the content of the file
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
    except IOError:
        print(f"Error: The file '{file_name}' could not be read.")
    return None

# Calling the function with the filename
read_file("myData.txt")


# 2. Modifying a file.
def modify_content(content):
    # Checking if the content is provided
    if content:
    # Converting the content to uppercase   
        modified_content = content.upper()  #converts the text to uppercase
        print("\nModified content:")
        print(modified_content) #displays the modified content
        return modified_content #returns the modified content
    else:
        # If the content was not passed
        print("No content to modify.")
        return None
    
    # 3. Writing the modified content into a new file
    
def write_to_file(file_name, content):
    try:
    
        with open(file_name, 'w') as file:
            file.write(content)
            print(f"\nModified content written to '{file_name}'")
    except IOError:
        print(f"Error: Could not write to the file '{file_name}'.")

# The main function
def main():
    # Asks the user for the file name to read
    input_file = input("Enter the name of the file to read: ")
    content = read_file(input_file)
    
    if content:
        # Modifies the content
        modified_content = modify_content(content)
        
        # Writes to a new file
        if modified_content:
            output_file = "modified_myData.txt"
            write_to_file(output_file, modified_content)

if __name__ == "__main__":
    main()




