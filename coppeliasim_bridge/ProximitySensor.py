from coppeliasim_bridge.SensorBase import SensorBase


# Return values
#
#     res: detection state (0 or 1)
#     dist: distance to the detected point
#     point: array of 3 numbers indicating the relative coordinates of the detected point
#     obj: handle of the object that was detected
#     n: normal vector (normalized) of the detected surface. Relative to the sensor reference frame



class ProximitySensor(SensorBase):
    def __init__(self):
        super().__init__()
        self.sensors = self.scan('proximitysensor')

        for sensor in self.sensors:
            handle = self.sensors[sensor]['handle']
            self.sensors[sensor]['range'] = self.coppelia.sim.getFloatProperty(handle, 'volume_range')

    def get_data(self):
        result = {}
        for sensor in self.sensors:
            handle = self.sensors[sensor]['handle']

            res, dist, point, obj, n = self.coppelia.sim.readProximitySensor(handle)
            result[sensor] = { 'detected': res, 'distance': dist, 'point': point, 'range':  self.sensors[sensor]['range']}

        return result