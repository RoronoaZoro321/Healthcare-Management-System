import Person
import persistent
from persistent.list import PersistentList

class Log(persistent.Persistent):
    def __init__(self,date: str, target: Person, action: str):
        self.date = date
        self.target = target
        self.action = action
    
    
    