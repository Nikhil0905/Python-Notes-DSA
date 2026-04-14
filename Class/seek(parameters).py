# Open a file in write mode ('w')
file_path = "example.txt"
with open(file_path, 'w') as file:
    # Write some content to the file
    file.write("This is line 1.\nThis is line 2.\nThis is line 3.")

# Open the file in read mode ('r')
with open(r"C:\Users\nikhi\OneDrive\Documents\Notepad File Handling\GD Rules.txt") as file:
    # Read and print the initial content
    content = file.read()
    print("Initial Content:")
    print(content)

    # Move the file pointer to the beginning and read the content again
    file.seek(0)
    content_at_beginning = file.read()
    print("\nContent after seeking to the beginning:")
    print(content_at_beginning)

    # Move the file pointer 10 characters forward from the current position
    file.seek(10, 1)
    content_after_forward_seek = file.read()
    print("\nContent after seeking 10 characters forward:")
    print(content_after_forward_seek)

    # Move the file pointer 5 characters backward from the current position
    file.seek(-5, 1)
    content_after_backward_seek = file.read()
    print("\nContent after seeking 5 characters backward:")
    print(content_after_backward_seek)
