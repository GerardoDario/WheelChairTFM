from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
import os

def generate_launch_description():
    sdf_file = os.path.join(
        FindPackageShare('<tu_paquete>').find('<tu_paquete>'),
        'models',
        'robot.sdf'
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use simulation (Gazebo) clock if true'),

        # Nodo para lanzar Gazebo y cargar el modelo del robot
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=['-file', sdf_file, '-entity', 'robot'],
            output='screen',
        ),

        # Lanzar el controller_manager
        Node(
            package='controller_manager',
            executable='ros2_control_node',
            parameters=[{
                'robot_description': Command(['xacro ', sdf_file]),
            }],
            output='screen',
        ),

        # Spawner para el controlador diferencial
        Node(
            package='controller_manager',
            executable='spawner',
            arguments=['diff_drive_controller'],
            output='screen',
        ),

        # Lanzar Nav2
        Node(
            package='nav2_bringup',
            executable='bringup_launch.py',
            name='nav2_bringup',
            output='screen',
            parameters=[{
                'use_sim_time': LaunchConfiguration('use_sim_time'),
            }],
        )
    ])
