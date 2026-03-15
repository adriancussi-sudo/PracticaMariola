from setuptools import find_packages, setup

package_name = 'ej1'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mariola',
    maintainer_email='adrian.cussi@ucb.edu.bo',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'robot_sensor_publisher = ej1.robot_sensor_publisher:main',
            'robot_monitor = ej1.robot_monitor:main',
            'robot_state_node = ej1.robot_state_node:main',
        ],
    },
)
