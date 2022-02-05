from types import FunctionType


class Event():
    def __init__(self):
        self.events = {}

    def on(self, name: str, callback: FunctionType):
        """set an event callback to the event name

        Args:
            name (str): event name
            callback (FunctionType): function called
        """        
        self.events[name] = callback
 
    def emit(self, name: str, args = None):
        """emit a event

        Args:
            name (str): event name
            args ([type], optional): args passed to the event. Defaults to None.
        """
        if self.events[name] != None :
            self.events[name](args)
    
    def remove(self, name: str):
        """remove an event

        Args:
            name (str): event name
        """
        self.events.pop(name)    

if __name__ == "__main__":
    e = Event()
    e.on('message', lambda message: print(f"message: {message}"))

    e.emit('message', 'hello world')

    e.remove('message')
    try:
        e.emit('message')
    except KeyError:
        print("Message event isn't found")


    try:
        e.emit('connect') # throw error
    except KeyError:
        print("connect event isn't set")
