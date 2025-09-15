from setuptools import find_packages, setup

package_name = 'coppeliasim_bridge'

setup(
    name=package_name,
    version='0.1.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
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
        ],
    },
)
