import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class RobotMonitor(Node):

    def __init__(self):
        super().__init__('robot_monitor')

        # Variables para guardar últimos valores
        self.velocity = None
        self.battery = None

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

        # Revisar velocidad
        if self.velocity is not None:
            if self.velocity > 2.0:
                self.get_logger().info(
                    f'Velocity: {self.velocity:.2f} → WARNING'
                )
            else:
                self.get_logger().info(
                    f'Velocity: {self.velocity:.2f}'
                )

        # Revisar batería
        if self.battery is not None:

            if self.battery < 10:
                self.get_logger().info(
                    f'Battery: {self.battery:.1f} → CRITICAL BATTERY'
                )

            elif self.battery < 20:
                self.get_logger().info(
                    f'Battery: {self.battery:.1f} → LOW BATTERY'
                )

            else:
                self.get_logger().info(
                    f'Battery: {self.battery:.1f}'
                )


def main(args=None):
    rclpy.init(args=args)

    node = RobotMonitor()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()