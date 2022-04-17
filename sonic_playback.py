import retro
import csv

movie = retro.Movie('SonicTheHedgehog-Genesis-GreenHillZone.Act1-00000046.bk2')
movie.step()

env = retro.make(
    game=movie.get_game(),
    state=None,
    # bk2s can contain any button presses, so allow everything
    use_restricted_actions=retro.Actions.ALL,
    players=movie.players,
)


env.initial_state = movie.get_state()
env.reset()

while movie.step():
    env.render()
    keys = []
    for p in range(movie.players):
        for i in range(env.num_buttons):
            keys.append(movie.get_key(i, p))
         
    env.step(keys)
