from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
import os

def generate_launch_description():
    # Directorio del archivo .world
    world_path = os.path.join(
        os.getenv('HOME'), 'tfm-robot-wheelchair', 'src', 'wheelchairpkg', 'worlds', 'init_world.world'
    )

    return LaunchDescription([
        # Iniciar Gazebo y cargar el mundo
        ExecuteProcess(
            cmd=['gazebo', '--verbose', world_path, '-s', 'libgazebo_ros_factory.so'],
            output='screen'
        ),
    ])
