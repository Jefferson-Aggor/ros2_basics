import rclpy
from rclpy.node import Node

class Greetings(Node):
    def __init__(self):
      self.counter = 0
      super().__init__("greetings")
      self.create_timer(1, self.timer)

    def timer(self):
       self.get_logger().info(f'Hello World [{self.counter}]')
       self.counter += 1


def main(args=None):
    rclpy.init(args=args)
    node = Greetings()
    rclpy.spin(node)
    rclpy.shutdown()

if "__name__" == "__main__":
    main()