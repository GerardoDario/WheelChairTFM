import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    # Obtén la ruta del archivo URDF
    urdf_file = os.path.join(
        get_package_share_directory('my_wheelchair_robot'),
        'urdf',
        'wheelchair.urdf')

    return LaunchDescription([
        ExecuteProcess(
            cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_factory.so'],
            output='screen'),

        Node(
            package='gazebo_ros', executable='spawn_entity.py',
            arguments=['-entity', 'wheelchair', '-file', urdf_file, '-x', '0', '-y', '0', '-z', '0.5'],
            output='screen'),

        # Nodo para el controller_manager y configuración de los controladores
        Node(
            package='controller_manager',
            executable='ros2_control_node',
            parameters=[os.path.join(get_package_share_directory('my_wheelchair_robot'), 'config', 'wheelchair_controllers.yaml')],
            output='screen'
        ),

        # Spawners de los controladores
        Node(
            package='controller_manager',
            executable='spawner',
            arguments=['joint_state_broadcaster'],
            output='screen'),

        Node(
            package='controller_manager',
            executable='spawner',
            arguments=['diff_drive_controller'],
            output='screen'),
    ])

