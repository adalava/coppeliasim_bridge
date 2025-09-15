from coppeliasim_bridge.SensorBase import SensorBase

class ForceSensor(SensorBase):
    def __init__(self):
        super().__init__()
        self.sensors = self.scan('forcesensor')

    def get_force_torque(self):
        result = {}
        for sensor in self.sensors:
                handle = self.sensors[sensor]['handle']
                res, forceVector, torqueVector = self.coppelia.sim.readForceSensor(handle)
                if res != -1:
                    result[sensor] = { 'force': forceVector, 'torque': torqueVector } 
                else:
                     result[sensor] = None
        
        return result