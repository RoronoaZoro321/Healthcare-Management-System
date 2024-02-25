# from Person import Person
import persistent
from persistent.list import PersistentList
from datetime import datetime

class Log(persistent.Persistent):
    def __init__(self, id: int, actor, action: str, target):
        self.id = id
        self.time = datetime.now()
        self.actor = actor
        self.action = action
        self.target = target
    
    def get_id(self):
        return self.id
    
    def get_time(self):
        return self.time.strftime("%m/%d/%Y, %H:%M:%S")

    def get_actor(self):
        return self.actor    
    
    def get_action(self):
        return self.action
    
    def get_target(self):
        return self.target
    
    def get_details(self):
        return f"{self.id} {self.time} {self.actor.get_fname()} {self.action} {self.target.get_fname()}"
    
    def get_actor_fname(self):
        return self.actor.get_fname()
    
    def get_target_fname(self):
        return self.target.get_fname()
