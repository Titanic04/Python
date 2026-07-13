student=["mohit","rahul","rohit","shivam"]
def is_skip(name):
    return name.lower() == "none"
  

def add_student():
    add_stud = input("enter to add the student name: ")  # To add student name
    if add_stud in student:
        print(f"{add_stud} is already in the list.")
    else:
        student.append(add_stud)


def remove_student():
    remove_stud = input("Enter the student name to remove or 'none' to skip: ")  # to remove student name
    # if remove_student.lower() == 'none':
    #     pass
    if is_skip(remove_stud):
        return

    elif remove_stud in student:
        student.remove(remove_stud)
    else:
        print(f"{remove_stud} is not in the list.")

def fin_student():
    find_stud = input("Enter the student name to find or 'none' to skip: ") # To find student name

    if is_skip(find_stud):
        pass
    # elif find_student in student:
    #     index = student.index(find_student) +1
    #     print(f"{find_student} is in the list")
    #     print(f"{find_student} is in the list {index}.")
    
    # else:
    #     print(f"{find_student} is not in the list.")
    else:
        try:
            index = student.index(find_stud) + 1
            print(f"{find_stud} is at position {index}")
        except ValueError:
            print(f"{find_stud} is not in the list.")



def show_student():
    print(student)
    print(f"total student: {len(student)} . ")  # Total number of students
    for stud in sorted(student):        # Sorting student names in alphabetical order
        print(stud)


# add_student()
# remove_student()
# fin_student()
# show_student()


while True:
    print("1. Add student")
    print("2. Remove student")
    print("3. Find student")
    print("4. Show students")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_student()
    elif choice == '2':
        remove_student()
    elif choice == '3':
        fin_student()
    elif choice == '4':
        show_student()
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("invalid choice")
