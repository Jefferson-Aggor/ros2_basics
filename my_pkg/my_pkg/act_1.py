#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class Act_1(Node):
    def __init__(self):
        self.counter = 0
        super().__init__('activity_001')
        self.create_timer(0.5, self.timer)
    
    def timer(self):
        self.counter += 1
        self.get_logger().info(f'This is the first activity [{self.counter}]')


def main(args=None):
    rclpy.init(args=args)
    node = Act_1()
    rclpy.spin(node)
    rclpy.shutdown()

if "__name__" == "__main__":
    main()