try:
    # File Creation
    with open("my_file.txt", "w") as my_file:
        my_file.write("First line:1234567\n")
        my_file.write("Second line:Am a student at PLP.\n")
        my_file.write("Third line: ABCDEFG\n")
        print("File 'my_file.txt' created successfully.")

    # File Reading and Display
    print("\nContents of the file:")
    with open("my_file.txt", "r") as my_file:
        for line in my_file:
            print(line.strip())

    # File Appending
    with open("my_file.txt", "a") as my_file:
        my_file.write("Fourth line:python is an interesting language\n")
        my_file.write("Fifth line:8 9 10 11\n")
        my_file.write("Sixth line: HIJKLMNOPQ\n")
        print("\nAdditional lines appended to the file 'my_file.txt'.")
        
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: No permissions to read or write the file.")
except Exception as e:
    print("Unexpected error:", str(e))
finally:
    print("Script execution completed.")
