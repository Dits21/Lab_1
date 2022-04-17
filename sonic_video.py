import retro
import imageio
import base64
import IPython



env = retro.make('SonicTheHedgehog-Genesis', 'GreenHillZone.Act1')
num_episodes = 3
video_filename = "SONIC.mp4"

env.reset()
with imageio.get_writer(video_filename, fps=60) as video:
  for _ in range(num_episodes):
    time_step = env.reset()
    video.append_data(env.render(mode='rgb_array'))
    for _ in range(365):
      action = env.action_space.sample()
      ob, rew, done, info = env.step(action)
      print("Action ", action, "Reward ", rew)
      video.append_data(env.render(mode='rgb_array'))
env.close()
embed_mp4(video_filename)