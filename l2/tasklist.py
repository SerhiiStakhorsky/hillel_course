lst = ["Проснуться", "Выпить кофе", "Почистить зубы","Позавтракать", "Прочесть новости"]
task_number = 1

def print_task_list(tasks):
    task_number = 1
    for task in tasks:
        print(f"{task_number}. {task}")
        task_number += 1
print("Task list for today:")
print_task_list(lst)


while True:
    answer = input("Do you want to add something else? Y/N: (Print 'stop' if you want to end the list) ")
    if answer.lower() == "stop":
        break
    else:
        new_task = input("Input task: ")
        lst.append(new_task)
        print("Updated task list: ")
        print_task_list(lst)
print(f"Your task list for today:")
print_task_list(lst)

print("\n\n===========================================================================================\n\n")

while True:
    check_completed = input("Press 'Enter' if you need to remove a task or type 'stop' to finish: ")
    if check_completed.lower() == "stop":
        break
    else:
        task_to_remove = int(input("Input task number to remove: "))
        if 1 <= task_to_remove <= len(lst):
            lst.pop(task_to_remove - 1)
            print("Updated task list: ")
            print_task_list(lst)
        else:
            print("Invalid number, Try agan")

print("\nUpdated task list for today:")
if len(lst) == 0:
    print("You did all tasks!")
else:
    print_task_list(lst)

