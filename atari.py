import gym
import random
import numpy as np

env = gym.make("Breakout-v0")

LEARNING_RATE = 0.1
DISCOUNT_RATE = 0.9
EPISODES = 10000
STEPS_PER_EPISODE = 100

EPSILON_RATE = 1
EPSILON_DECAY_RATE = 0.01
MIN_EPSILON = 0.01
MAX_EPSILON = 1


for i in range(EPISODES):
	env.seed(0)

	env.reset()
	episode_reward = 0
	while True:
		env.render()
		action = env.action_space.sample()
		_, reward, done, _ = env.step(action)
		episode_reward += reward
		if done:
			print('Reward: %s' % episode_reward)
			break
