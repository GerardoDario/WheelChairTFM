from stable_baselines3 import PPO
from stable_baselines3.common.envs import DummyVecEnv
from src import env_wheelchair  # tu entorno de ROS

# Crear el entorno
env = DummyVecEnv([lambda: env_wheelchair()])

# Crear el modelo
model = PPO("MlpPolicy", env, verbose=1)

# Entrenar el modelo
model.learn(total_timesteps=100000)

# Guardar el modelo entrenado
model.save("ppo_wheelchair_navigation")
