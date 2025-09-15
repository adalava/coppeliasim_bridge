# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Wrench

import time
from coppeliasim_zmqremoteapi_client import RemoteAPIClient

class ForceSensor():
    sim = None
    handle = None
    parent_handle = None
    name = None

    def __init__(self, sim, alias, handle):
        self.sim = sim
        self.name = alias
        self.handle = handle

        self.parent_handle = self.sim.getIntProperty(handle, 'parentHandle')
        self.parent_name = self.sim.getStringProperty(self.parent_handle, 'alias')
        self.full_name = '{}/{}'.format(self.parent_name, self.name)

    def get_force_torque(self):
        result, forceVector, torqueVector = self.sim.readForceSensor(self.handle)
        if result == 0: return None # data unavailable
        
        return forceVector, torqueVector

        


class ForceSensorPublisher(Node):
    
    force_sensors = None
    sim = None
    publishers = []

    def __init__(self):
        super().__init__('forcesensor_publisher')

        self.get_logger().info('Connecting to CoppeliaSim...')
        client = RemoteAPIClient()
        self.sim = client.require('sim')

        #self.get_logger().info('Loading scene...')
        #self.sim.loadScene('/root/Unicamp/roomba/roomba style.ttt')

        self.get_logger().info('Retrieving force sensor objects...')
        self.force_sensors = self.get_forcesensor_objects()

        for sensor in self.force_sensors:
            handle = self.force_sensors[sensor]['handle']
            sensor_obj = ForceSensor(self.sim, sensor, handle)

            self.get_logger().info('Creating publisher topic "{}"'.format(sensor_obj.full_name))

            publisher = self.create_publisher(Wrench, sensor_obj.full_name, 10)

            self.publishers.append((sensor_obj, publisher))

            
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
    
    def get_forcesensor_objects(self):
        sensors = {}
        object = 0
        pos = 0
        while object != -1:
            object = self.sim.getObjects(pos, self.sim.sceneobject_forcesensor)
            if object != -1:
                alias = self.sim.getStringProperty(object, 'alias')
                sensors[alias] = {}
                sensors[alias]['handle'] = object
            pos += 1

        return sensors

    def timer_callback(self):
        msg = Wrench()

        #for sensor in self.force_sensors:
        #    handle = self.force_sensors[sensor]['handle']
        #    print(sensor, self.sim.getVector3Property(handle, 'sensorForce'))
        #    print(sensor, self._check_collision(handle))

        for data in self.publishers:
            sensor, publisher = data
            result = sensor.get_force_torque()
            if result is None: continue

            force, torque = result
            msg.force.x = force[0]
            msg.force.y = force[1]
            msg.force.z = force[2]

            msg.torque.x = torque[0]
            msg.torque.y = torque[1]
            msg.torque.z = torque[2]

            publisher.publish(msg)
            self.get_logger().info('Publishing: "%s"' % msg)


def main(args=None):
    rclpy.init(args=args)

    forcesensor_publisher = ForceSensorPublisher()

    rclpy.spin(forcesensor_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    forcesensor_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
