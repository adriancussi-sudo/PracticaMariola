import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from std_msgs.msg import String


class RobotStateNode(Node):

    def __init__(self):
        super().__init__('robot_state_node')

        # Variables para guardar últimos valores
        self.velocity = None
        self.battery = None

        # Estado actual del robot
        self.current_state = None

        # Publisher del estado
        self.state_publisher = self.create_publisher(String, '/robot_state', 10)

        # Suscripciones
        self.create_subscription(
            Float32,
            '/robot_velocity',
            self.velocity_callback,
            10
        )

        self.create_subscription(
            Float32,
            '/robot_battery',
            self.battery_callback,
            10
        )

    def velocity_callback(self, msg):
        self.velocity = msg.data
        self.evaluate_state()

    def battery_callback(self, msg):
        self.battery = msg.data
        self.evaluate_state()

    def evaluate_state(self):

        if self.velocity is None or self.battery is None:
            return

        new_state = "NORMAL"

        if self.battery < 10:
            new_state = "CRITICAL"

        elif self.battery < 20:
            new_state = "LOW_BATTERY"

        elif self.velocity > 2.0:
            new_state = "OVER_SPEED"

        if new_state != self.current_state:

            self.current_state = new_state

            msg = String()
            msg.data = new_state

            self.state_publisher.publish(msg)

            self.get_logger().info(f'Robot state → {new_state}')


def main(args=None):
    rclpy.init(args=args)

    node = RobotStateNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()