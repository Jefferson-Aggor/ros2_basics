#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class Long_name(Node):
    def __init__(self):
        super().__init__('this_is_a_very_long_name_but_it_works')
        self.get_logger().info('This is a very long name')

def main(args=None):
    rclpy.init(args=args)
    node = Long_name()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()