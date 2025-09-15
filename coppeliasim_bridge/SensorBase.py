from coppeliasim_bridge.Coppelia import Coppelia

class SensorBase():
    coppelia = None
    sim = None
    handle = None
    parent_handle = None
    name = None
    sensors = None

    objects = {}

    def __init__(self):
        self.connect()

    def connect(self):
        self.coppelia = Coppelia()

    def scan(self, obj_type):
        type = self.coppelia.get_type(obj_type)
        if type is not None:
            self.objects = self.coppelia.get_objects(type)
            return self.objects
        
        return None
    
    def get_sensors(self):
        return self.sensors
