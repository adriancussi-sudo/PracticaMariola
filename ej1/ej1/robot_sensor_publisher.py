import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random


class RobotSensorPublisher(Node):

    def __init__(self):
        super().__init__('robot_sensor_publisher')

        # Publicadores
        self.velocity_pub = self.create_publisher(Float32, '/robot_velocity', 10)
        self.battery_pub = self.create_publisher(Float32, '/robot_battery', 10)

        # Timer para publicar a 2 Hz (cada 0.5 segundos)
        self.timer = self.create_timer(0.5, self.publish_sensors)

    def publish_sensors(self):

        # Generar valores simulados
        velocity = random.uniform(0, 2.5)
        battery = random.uniform(0, 100)

        # Crear mensajes
        velocity_msg = Float32()
        battery_msg = Float32()

        velocity_msg.data = velocity
        battery_msg.data = battery

        # Publicar
        self.velocity_pub.publish(velocity_msg)
        self.battery_pub.publish(battery_msg)

        # Mostrar en consola
        self.get_logger().info(f'Velocity: {velocity:.2f} m/s')
        self.get_logger().info(f'Battery: {battery:.1f} %')


def main(args=None):
    rclpy.init(args=args)

    node = RobotSensorPublisher()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()