file_handle = open("mynotes.txt", "a")

message = input("Write your message:\n")

file_handle.write(message + "\n")

file_handle.close()

