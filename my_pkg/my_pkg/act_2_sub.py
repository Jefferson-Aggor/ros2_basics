#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64

class NumberCounterNode(Node):
    def __init__(self):
        super().__init__("number_counter")
        self.publisher_ = self.create_publisher(Int64, 'number_count', 10)
        self.subscriber_ = self.create_subscription(Int64, 'number', self.callback_number_counter, 10)
        
    def callback_number_counter(self,msg):
        new_msg = Int64()
        new_msg.data = msg.data
        self.publisher_.publish(new_msg)
        self.get_logger().info(f'Count: {msg.data}')
        


def main(args=None):
    rclpy.init(args=args)
    node = NumberCounterNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()