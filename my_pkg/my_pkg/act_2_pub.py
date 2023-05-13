#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.msg import Int64

class NumberNode(Node):
    def __init__(self):
        super().__init__("number_publisher")
        self.counter = 0
        self.publisher_ = self.create_publisher(Int64, "number", 10)
        self.create_timer(1, self.publish_number)
        self.get_logger().info('NumberNode Started!')

    def publish_number(self):
        msg = Int64()
        msg.data =  self.counter
        self.publisher_.publish(msg)
        self.counter += 2

def main(args=None):
    rclpy.init(args=args)
    node = NumberNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()