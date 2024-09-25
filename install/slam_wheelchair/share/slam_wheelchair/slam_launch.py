from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use simulation clock if true'),

        DeclareLaunchArgument(
            'slam_params_file',
            default_value='~/tfm-robot-wheelchair/src/slam_wheelchair/config/cartographer_params.lua',
            description='Full path to the ROS 2 parameters file to use'),

        # Nodo de Cartographer para SLAM
        Node(
            package='cartographer_ros',
            executable='cartographer_node',
            name='cartographer_node',
            output='screen',
            parameters=[{
                'use_sim_time': LaunchConfiguration('use_sim_time'),
            }],
            arguments=[
                '-configuration_directory', '/home/gesepulveda/tfm-robot-wheelchair/src/slam_wheelchair/config',
                '-configuration_basename', 'cartographer_params.lua',
            ],
        ),

        # Nodo de tf2 para la transformación entre el marco base del robot y el odometría/mapa
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_transform_publisher',
            output='screen',
            arguments=['0', '0', '0', '0', '0', '0', 'base_link', 'odom'],
        ),
    ])
