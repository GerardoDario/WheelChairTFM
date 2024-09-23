from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='nav2_bringup',
            executable='nav2_bringup_launch.py',
            parameters=['path/to/nav2_params.yaml']
        ),
    ])