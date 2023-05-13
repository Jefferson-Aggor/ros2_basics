from setuptools import setup

package_name = 'my_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='dev',
    maintainer_email='dev@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "my_pkg = my_pkg.my_first_node:main",
            "greetings = my_pkg.helloworld_node:main",
            "activity_001 = my_pkg.act_1:main",
            "long_name = my_pkg.long_name:main",
            "robot_news_station = my_pkg.robot_news_station:main", 
            "smartphone = my_pkg.smartphone:main",
            "number_publisher = my_pkg.act_2_pub:main",
            "number_counter = my_pkg.act_2_sub:main"
        ],
    },
)
