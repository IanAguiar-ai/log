"""
Class for assembling logs
"""
from time import time, localtime, sleep
import os
from threading import Thread, active_count, current_thread

class Log:
    """
    Creates a txt log that stores information along with the machine's local time
    """
    def __init__(self, file:str = "log", check_thread:bool = False):
        """
        file: File name next to directory
        """
        if file == "log":
            t:list = time_now()
            file += f"_{t[0]}_{t[1]:02}_{t[2]:02}"
        if file.find(".txt") == -1:
            file += ".txt"
        self.file:str = file
        self.name:id = id(self)
        self.time_initial:list = time_now()
        self.create_file()
        if check_thread:
            self.check()

    def create_file(self) -> None:
        """
        Create txt file if file does not exist
        """
        if not os.path.isfile(self.file):
            with open(self.file, 'w') as arq:
                t:list = self.time_initial
                arq.write(f"<log creation> {t[2]:02}/{t[1]:02}/{t[0]} - {t[3]:02}:{t[4]:02}:{t[5]:02}")

        else:
            self.add(text = f"connecting to the log", description = "action")

    def add(self, text:str, description:str = "information") -> None:
        """
        Add the requested text next to the time
        """
        if os.path.isfile(self.file):
            with open(self.file, 'r') as arq:
                old:str = arq.read()
        else:
            print("The log has been lost!")

        if os.path.isfile(self.file):
            with open(self.file, 'w') as arq:
                t:list = time_now()
                arq.write(f"{old}\n<{description}> {t[2]:02}/{t[1]:02}/{t[0]} - {t[3]:02}:{t[4]:02}:{t[5]:02} | {text}")
        else:
            print("The log has been lost!")

    def backup(self, new_log:str = "backup_log") -> None:
        """
        Back up the specified log
        new_log: Backup txt name
        """
        if new_log.find(".txt") == -1:
            new_log += ".txt"
        self.add(text = f"Make copy to '{new_log}'", description = "backup")
        with open(self.file, 'r') as arq:
            old:str = arq.read()
        if not os.path.isfile(new_log):
            with open(new_log, 'w') as arq:
                arq.write(old)

    def check(self) -> None:
        """
        Check if the program is still running
        """
        self.ch:Thread = Thread(target = check_continuous, args = [self, current_thread()])
        self.ch.start()
        self.add(text = "turning on recurring check", description = "action")

    def read(self) -> list:
        """
        Reads the log and returns a dictionary
        """
        self.add(text = f"getting log", description = "action")
        
        with open(self.file, 'r') as arq:
            old:str = arq.read()
        all_log:list = old.split("\n")
        
        all_log_dict:dict = {}
        for i in range(len(all_log)):
            all_log[i]:list = all_log[i].replace("<","").split(">")
            if not all_log[i][0] in all_log_dict:
                all_log_dict[all_log[i][0]] = [all_log[i][1][1:]]
            else:
                all_log_dict[all_log[i][0]].append(all_log[i][1][1:])

        all_log_dict["all"]:list = old.split("\n")        
        return all_log_dict

    def clean(self) -> str:
        """
        Clear the log
        """
        if os.path.isfile(self.file):
            with open(self.file, 'w') as arq:
                t:list = time_now()
                arq.write(f"<log creation> {t[2]:02}/{t[1]:02}/{t[0]} - {t[3]:02}:{t[4]:02}:{t[5]:02}")
        else:
            print("The log has been lost!")

    def __repr__(self) -> str:
        log:list = self.read()
        t:list = self.time_initial
        text:str = f"Log: {self.file}\nCreation Log: {log['log creation'][0]}\nOpen log: {t[2]:02}/{t[1]:02}/{t[0]} - {t[3]:02}:{t[4]:02}:{t[5]:02}\nLines Log: {len(log['all'])}"
        return text

def time_now() -> list:
    data:localtime = localtime()
    d:int = data.tm_mday
    mt:int = data.tm_mon
    y:int = data.tm_year
    h:int = data.tm_hour
    m:int = data.tm_min
    s:int = data.tm_sec
    return [y, mt, d, h, m, s]

def check_continuous(obj:Log, thread_main:Thread) -> None:
    """
    Check if the program is still running
    """
    num_threads:int = 1
    while True:
        if active_count() == 1:
            obj.add(text = "The program is not running", description = "error")

        if num_threads != active_count():
            num_threads:int = active_count()
            obj.add(text = f"{num_threads} threads are active")     
        sleep(3)
