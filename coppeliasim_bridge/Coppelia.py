from coppeliasim_zmqremoteapi_client import RemoteAPIClient

class Coppelia():
    sim = None
    def __init__(self):
        client = RemoteAPIClient()
        self.sim = client.require('sim')
    
    def get_type(self, type_str):
        if type_str == 'forcesensor':
            return self.sim.sceneobject_forcesensor
        
        return None

    def get_objects(self, obj_type):
        objects = {}
        object = 0
        pos = 0
        while object != -1:
            object = self.sim.getObjects(pos, obj_type)
            if object != -1:

                # Sensor name
                name = self.sim.getStringProperty(object, 'alias')

                # Sensor parent name
                parent_handle = self.sim.getIntProperty(object, 'parentHandle')
                parent_name = self.sim.getStringProperty(parent_handle, 'alias')

                # object name will be "<parent_name>/<name>" (like "MyRobot/Sensor1")
                full_name = '{}/{}'.format(parent_name, name)

                objects[full_name] = {}
                objects[full_name]['handle'] = object

            pos += 1

        return objects
