Project 3: Reinforcement Learning
=================================

Introduction
------------

In this project, you will implement value iteration and Q-learning. You will test your agents first on Gridworld (from
class), then apply them to a simulated robot controller (Crawler) and Pacman.

As in previous projects, this project includes an autograder for you to grade your solutions on your machine. This can
be run on all questions with the command:

    python autograder.py

Questions
---------
**Question 1: Value Iteration (6 points)**

Write a value iteration agent in ValueIterationAgent, which has been partially specified for you in
valueIterationAgents.py. Your value iteration agent is an offline planner, not a reinforcement learning agent, and so the
relevant training option is the number of iterations of value iteration it should run (option -i) in its initial planning
phase. ValueIterationAgent takes an MDP on construction and runs value iteration for the specified number of iterations
before the constructor returns.

Value iteration computes k-step estimates of the optimal values, Vk. In addition to running value iteration, implement the
following methods for ValueIterationAgent using Vk.

computeActionFromValues(state) computes the best action according to the value function given by self.values.
computeQValueFromValues(state, action) returns the Q-value of the (state, action) pair given by the value function given
by self.values. These quantities are all displayed in the GUI: values are numbers in squares, Q-values are numbers in
square quarters, and policies are arrows out from each square.

**Question 2: Bridge Crossing Analysis (1 point)**

BridgeGrid is a grid world map with the a low-reward terminal state and a high-reward terminal state separated by a narrow
"bridge", on either side of which is a chasm of high negative reward. The agent starts near the low-reward state. With
the default discount of 0.9 and the default noise of 0.2, the optimal policy does not cross the bridge. Change only ONE
of the discount and noise parameters so that the optimal policy causes the agent to attempt to cross the bridge. Put
your answer in question2() of analysis.py. (Noise refers to how often an agent ends up in an unintended successor state
when they perform an action.)

**Question 3: Policies (5 points)**

Consider the DiscountGrid layout, shown below. This grid has two terminal states with positive payoff (in the middle row),
a close exit with payoff +1 and a distant exit with payoff +10. The bottom row of the grid consists of terminal states
with negative payoff (shown in red); each state in this "cliff" region has payoff -10. The starting state is the yellow
square. We distinguish between two types of paths: (1) paths that "risk the cliff" and travel near the bottom row of the
grid; these paths are shorter but risk earning a large negative payoff, and are represented by the red arrow in the
figure below. (2) paths that "avoid the cliff" and travel along the top edge of the grid. These paths are longer but are
less likely to incur huge negative payoffs. These paths are represented by the green arrow in the figure below.

<img src="https://github.com/drolando/CS188.1-Artificial-Intelligence/blob/master/reinforcement/discountgrid.png" width="300">

In this question, you will choose settings of the discount, noise, and living reward parameters for this MDP to produce
optimal policies of several different types. Your setting of the parameter values for each part should have the property
that, if your agent followed its optimal policy without being subject to any noise, it would exhibit the given behavior.
If a particular behavior is not achieved for any setting of the parameters, assert that the policy is impossible by
returning the string 'NOT POSSIBLE'.

Here are the optimal policy types you should attempt to produce:

1. Prefer the close exit (+1), risking the cliff (-10)
2. Prefer the close exit (+1), but avoiding the cliff (-10)
3. Prefer the distant exit (+10), risking the cliff (-10)
4. Prefer the distant exit (+10), avoiding the cliff (-10)
5. Avoid both exits and the cliff (so an episode should never terminate)

**Question 4: Q-Learning (5 points)**

You will now write a Q-learning agent, which does very little on construction, but instead learns by trial and error
from interactions with the environment through its update(state, action, nextState, reward) method. A stub of a Q-learner
is specified in QLearningAgent in qlearningAgents.py, and you can select it with the option '-a q'. For this question,
you must implement the update, computeValueFromQValues, getQValue, and computeActionFromQValues methods.

**Question 5: Epsilon Greedy (3 points)**

Complete your Q-learning agent by implementing epsilon-greedy action selection in getAction, meaning it chooses random
actions an epsilon fraction of the time, and follows its current best Q-values otherwise. Note that choosing a random
action may result in choosing the best action - that is, you should not choose a random sub-optimal action, but rather
any random legal action.

Your final Q-values should resemble those of your value iteration agent, especially along well-traveled paths. However,
your average returns will be lower than the Q-values predict because of the random actions and the initial learning phase.

**Question 6: Bridge Crossing Revisited (1 point)**

First, train a completely random Q-learner with the default learning rate on the noiseless BridgeGrid for 50 episodes
and observe whether it finds the optimal policy.

    python gridworld.py -a q -k 50 -n 0 -g BridgeGrid -e 1

Now try the same experiment with an epsilon of 0. Is there an epsilon and a learning rate for which it is highly likely
(greater than 99%) that the optimal policy will be learned after 50 iterations? question6() in analysis.py should
return EITHER a 2-item tuple of (epsilon, learning rate) OR the string 'NOT POSSIBLE' if there is none. Epsilon is
controlled by -e, learning rate by -l.

**Question 7: Q-Learning and Pacman (1 point)**

Time to play some Pacman! Pacman will play games in two phases. In the first phase, training, Pacman will begin to
learn about the values of positions and actions. Because it takes a very long time to learn accurate Q-values even
for tiny grids, Pacman's training games run in quiet mode by default, with no GUI (or console) display. Once Pacman's
training is complete, he will enter testing mode. When testing, Pacman's self.epsilon and self.alpha will be set to
0.0, effectively stopping Q-learning and disabling exploration, in order to allow Pacman to exploit his learned policy.
Test games are shown in the GUI by default.

Note that PacmanQAgent is already defined for you in terms of the QLearningAgent you've already written. PacmanQAgent
is only different in that it has default learning parameters that are more effective for the Pacman problem
(epsilon=0.05, alpha=0.2, gamma=0.8). You will receive full credit for this question if the command above works without
exceptions and your agent wins at least 80% of the time. The autograder will run 100 test games after the 2000 training
games.

**Question 8: Approximate Q-Learning (3 points)**

Implement an approximate Q-learning agent that learns weights for features of states, where many states might share the
same features. Write your implementation in ApproximateQAgent class in qlearningAgents.py, which is a subclass of
PacmanQAgent.

Note: Approximate Q-learning assumes the existence of a feature function f(s,a) over state and action pairs, which
yields a vector f1(s,a) .. fi(s,a) .. fn(s,a) of feature values. We provide feature functions for you in
featureExtractors.py. Feature vectors are util.Counter (like a dictionary) objects containing the non-zero pairs of
features and values; all omitted features have value zero.

