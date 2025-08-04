import os

def read_and_write_file():
    """
    Reads a specified text file, modifies its content, and writes the
    modified content to a new file.
    Includes robust error handling for file operations.
    """

    # --- 1. Ask the user for a filename ---
    input_filename = input("Please enter the name of the file you want to process: ")

    # Use a try-except block to handle potential file-related errors
    try:
        # --- 2. Read the original file ---
        # The 'with' statement ensures the file is automatically closed, even if errors occur.
        print(f"\nAttempting to read file: '{input_filename}'...")
        with open(input_filename, 'r') as original_file:
            # Read the entire content of the file into a string variable
            original_content = original_file.read()
        print("File read successfully!")

        # --- 3. Modify the content ---
        # For this example, we'll convert all the text to uppercase.
        modified_content = original_content.upper()
        print("Content has been modified (converted to uppercase).")

        # --- 4. Write the modified content to a new file ---
        # Create a new filename to avoid overwriting the original.
        # We add '_MODIFIED' before the file extension.
        base, extension = os.path.splitext(input_filename)
        output_filename = f"{base}_MODIFIED{extension}"

        print(f"Writing modified content to new file: '{output_filename}'...")
        with open(output_filename, 'w') as new_file:
            new_file.write(modified_content)
        
        # --- 5. Provide success feedback ---
        print(f"\nSuccess! The modified file has been created as '{output_filename}'.")
        print("-" * 50)
        print("Original Content:")
        print("-" * 50)
        print(original_content)
        print("-" * 50)
        print("Modified Content:")
        print("-" * 50)
        print(modified_content)
        print("-" * 50)

    except FileNotFoundError:
        # This error is raised if the file does not exist
        print(f"\nError: The file '{input_filename}' was not found. Please check the file name and try again.")
    except PermissionError:
        # This error is raised if the program doesn't have permission to access the file
        print(f"\nError: You do not have permission to access the file '{input_filename}'.")
    except Exception as e:
        # This is a general catch-all for any other unexpected errors
        print(f"\nAn unexpected error occurred: {e}")

# --- Call the function to start the program ---
if __name__ == "__main__":
    # Create a sample file for testing
    with open("sample.txt", "w") as f:
        f.write("This is a sample file.\n")
        f.write("We will read this content and make it uppercase.")
    
    print("A sample file named 'sample.txt' has been created for you to test.\n")
    read_and_write_file()