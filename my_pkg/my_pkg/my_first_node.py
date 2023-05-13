#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):
    counter  = 0
    def __init__(self):
        super().__init__("py_test")
        self.create_timer(0.5, self.timer)

    def timer(self):
        self.get_logger().info(f'Hello ROS2')


def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()