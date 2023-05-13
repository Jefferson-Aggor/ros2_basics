#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class SmartphoneNode(Node):
    def __init__(self):
        self.topic_ = "robot_news"
        super().__init__("smartphone")
        self.subscriber_ = self.create_subscription(String, self.topic_, self.callback_robot_news, 10)
        self.get_logger().info("Smartphone node has been started.")

    def callback_robot_news(self, msg):
        self.get_logger().info(f'I heard {msg.data} from {self.topic_}')   
    
def main(args=None):
    rclpy.init(args=args)
    node = SmartphoneNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()