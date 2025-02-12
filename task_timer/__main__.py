'''Task Timer Assignment
Author: Harvey Walter'''


import time 
import csv


class TaskTimer: 
    def __init__(self):
        self.tasks = {}
        self.history = [] 
        
    def start_task(self, task_name):
        if task_name in self.tasks:
            print("Task already running, either stop it or try calling it '{task_name} V2' if you want another one, my homie.")
            
        else:
            self.tasks[task_name] = time.time()
            print(f"Started task: {task_name}")
            


    def stop_task(self, task_name):
        if task_name not in self.tasks:
            print("Homie, that isn't a task!")
            
        else:
            start_time = self.tasks.pop(task_name)
            duration = time.time() - start_time
            self.history.append((task_name, duration))
            print(f"Stopped {task_name}: {duration:.2f} seconds")


    def show_summary(self):
        if not self.history:
            print("No tasks recorded homie, try starting one next time bub!.")
            
        else:
            print("\nTask Summary:")
            for task, duration in self.history:
                print(f"- {task}: {duration:.2f} seconds")


    def export_csv(self):
        with open("homie_time_sheet.csv", "w", newline="") as file:
            writer = csv.writer(file) 
            writer.writerow(["Task Name", "Duration (seconds)"])
            writer.writerows(self.history)
        print("Homie! I exported it to homie_time_sheet.csv for ya!") 


def main():
    timer = TaskTimer() 
    
    while True:
        print("\n1. Start Task  2. Stop Task  3. Show Summary  4. Export CSV  5. Exit")
        choice = input("Choose: ")

        if choice == "1":
            timer.start_task(input("Task name: "))
        elif choice == "2":
            timer.stop_task(input("Task name: "))
        elif choice == "3":
            timer.show_summary()
        elif choice == "4":
            timer.export_csv()
        elif choice == "5":
            break
        
        else:
            print("Invalid choice my homie!")


if __name__ == "__main__":
    main()