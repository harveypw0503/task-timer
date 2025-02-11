# Task Timer Assignment
# YEah, this is late, i know :(
# Author: Harvey Walter
# How do I use Github, and linux stuff! HELP!
# (inaudible screaming)
# (homie totally not chilling)

# import stuffs
import time # Tracks time and allows to start and stop it.
import csv # Exports task history as csv file, (I knew you could do this from where I worked over the summer but I wasn't the code I was the graphic designer and so I learned what a csv file was)



class TaskTimer: 
    def __init__(self):
        self.tasks = {} # make empty dic for tasks
        self.history = [] # list for completed tasks
    def start_task(self, task_name): # function to start tasky timer
        if task_name in self.tasks:
            print("Task already running, either stop it or try calling it '{task_name} V2' if you want another one, my homie.")
        else:
            self.tasks[task_name] = time.time() # store the time as the task's start time 
            print(f"Started task: {task_name}") # make sure it started homie

    def stop_task(self, task_name): # fucntion to stop a timer
        if task_name not in self.tasks: # check if there are finished tasks
            print("Homie, that isn't a task!") # bring homie his brain back
            
        else:
            start_time = self.tasks.pop(task_name) # remove task and take its time
            duration = time.time() - start_time # how long homie?
            self.history.append((task_name, duration)) # store tak names and durations
            print(f"Stopped {task_name}: {duration:.2f} seconds") # homie gets info

    def show_summary(self): #function to display summary of all finished tasks
        if not self.history: # check finished tasks
            print("No tasks recorded homie, try starting one next time bub!.") # let the homie know he's done jack all with your code
        else:
            print("\nTask Summary:") # make header with enter thingy
            for task, duration in self.history: #loop through stored tasks
                print(f"- {task}: {duration:.2f} seconds") # tell homie how long his task has been going

    def export_csv(self): # export history as x̶l̶s, i mean csv
        with open("homie_time_sheet.csv", "w", newline="") as file: # open csv
            writer = csv.writer(file) 
            writer.writerow(["Task Name", "Duration (seconds)"]) # make colume heading
            writer.writerows(self.history) # this was a pain to do and learn and i'd need research it again i'm sure if i had to do it, homie not having fun
        print("Homie! I exported it to homie_time_sheet.csv for ya!") 

def main(): #runs task timer
    timer = TaskTimer() 
    
    while True: # start infinite loop
        print("\n1. Start Task  2. Stop Task  3. Show Summary  4. Export CSV  5. Exit") #ask homie to make a choice
        choice = input("Choose: ")

        if choice == "1":
            timer.start_task(input("Task name: ")) #start task
        elif choice == "2":
            timer.stop_task(input("Task name: ")) # stop task of homie's choice
        elif choice == "3":
            timer.show_summary() #display summary
        elif choice == "4":
            timer.export_csv() # save task to csv for homie
        elif choice == "5":
            break
        else:
            print("Invalid choice my homie!") #homie is not smart

if __name__ == "__main__": # make it run directly # lol, line 69 😂
    main()