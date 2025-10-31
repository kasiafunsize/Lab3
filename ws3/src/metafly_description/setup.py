from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'metafly_description'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        # required for ROS 2 to find the package
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),

        # install launch and urdf folders
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*')),
    ],
    install_requires=['setuptools', 'xacro'],
    zip_safe=True,
    maintainer='khochwal',
    maintainer_email='kshochwald@gmail.com',
    description='Metafly description (xacro + launch)',
    license='MIT',
    entry_points={},
)
