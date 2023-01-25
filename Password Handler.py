password_file = open("Passwords.txt", "a")


def create_line_break(num_of_lines):
    lines = ""
    for line in range(num_of_lines):
        lines += "-"
    return lines + "\n\n"


def create_container_header(name):
    return name + ":\n\n"


try:
    container_line_input = input("Number of break lines: ")
    container_header_input = input("Name of the section?: ")
    continue_input = ""

    password_file.write(create_line_break(int(container_line_input)))
    password_file.write(create_container_header(container_header_input))

    while continue_input != str.lower("end"):
        container_user_input = input("Name of user line: ")
        container_password_input = input("Name of password line: ")
        password_file.write(container_user_input + ": " + container_password_input + "\n\n")
        continue_input = input("Add more information? \"end\" to end the program and to write it to your file. Answer: ")
    password_file.write(create_line_break(int(container_line_input)))
    password_file.close()

except ValueError as error:
    print("error: " + str(error))
    password_file.close()
