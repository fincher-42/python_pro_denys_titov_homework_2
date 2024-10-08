tasks = []


def to_do_list():
    def add_task(description):
        tasks.append(description)
        print(f"Task added: {description}")

    def remove_task(index):
        if 1 <= index < len(tasks) + 1:
            removed_task = tasks.pop(index - 1)
            print(f"Task removed: {removed_task}")
        else:
            print("Invalid task index.")

    def view_tasks():
        if tasks:
            print("To-do list:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
        else:
            print("To-do list is empty.")

    return add_task, remove_task, view_tasks


add_task, remove_task, view_tasks = to_do_list()


def main():
    while True:
        print("–––––––––––––")
        print("To-do list:")
        print("1. Add task")
        print("2. Remove task")
        print("3. View tasks")
        print("4. Exit")
        print()
        choice = input("Select an option (1/2/3/4): ")
        print()

        match choice:
            case "1":
                task = input("Enter a case description: ")
                print()
                add_task(task)
                print()
            case "2":
                if tasks:
                    view_tasks()
                    index = int(input("Enter a task index: "))
                    try:
                        remove_task(index)
                    except ValueError:
                        print("Please enter the correct task number.")
                else:
                    print("The to-do list is empty.")
            case "3":
                view_tasks()
            case "4":
                print("Thank you. Have a nice day!")
                break
            case _:
                print("Invalid input. Try again.")


main()
