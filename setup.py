from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'coppeliasim_bridge'

setup(
    name=package_name,
    version='0.2.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), 
            glob(os.path.join('launch', '*launch.[pxy][yma]*')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer="Alfredo Dal'Ava Júnior",
    maintainer_email='alfredojr@dalava.com.br',
    description='CoppeliaSim ROS2 bridge',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'forcesensor = coppeliasim_bridge.forcesensor_publisher:main',
            'proximitysensor = coppeliasim_bridge.proximitysensor_publisher:main',
        ],
    },
)
