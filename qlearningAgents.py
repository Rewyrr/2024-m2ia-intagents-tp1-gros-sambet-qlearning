# qlearningAgents.py
# ------------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

from game import *
from learningAgents import ReinforcementAgent
from featureExtractors import *

import random,util,math

class QLearningAgent(ReinforcementAgent):
  """
    Q-Learning Agent

    Functions you should fill in:
      - getQValue
      - getAction
      - getValue
      - getPolicy
      - update

    Instance variables you have access to
      - self.epsilon (exploration prob)
      - self.alpha (learning rate)
      - self.discount (discount rate)

    Functions you should use
      - self.getLegalActions(state)
        which returns legal actions
        for a state
  """
  def __init__(self, **args):
    "You can initialize Q-values here..."
    ReinforcementAgent.__init__(self, **args)

    "*** YOUR CODE HERE ***"
    
    self.qvalues = util.Counter()

  def setQValue(self,state,action,value):
    """
      Set Q(state,action) to the value
    """
    "*** YOUR CODE HERE ***"
    self.qvalues[(state,action)] = value

  def getQValue(self, state, action):
    """
      Returns Q(state,action)
      Should return 0.0 if we never seen
      a state or (state,action) tuple
    """
    "*** YOUR CODE HERE ***"
    return self.qvalues[(state,action)]

  def getValue(self, state):
    """
      Returns max_action Q(state,action)
      where the max is over legal actions.  Note that if
      there are no legal actions, which is the case at the
      terminal state, you should return a value of 0.0.
    """
    "*** YOUR CODE HERE ***"
    bestValue = float('-inf')
    if len(self.getLegalActions(state)) == 0:
      return 0.0
    for action in self.getLegalActions(state):
      if self.getQValue(state,action) > bestValue:
        bestValue = self.getQValue(state,action)
    return bestValue

  def getPolicy(self, state):
    """
      Compute the best action to take in a state.
      Note that the policy does not return here all the best actions, but break ties randomly
      to return one of the best actions.
      Note that if there
      are no legal actions, which is the case at the terminal state,
      you should return None.
    """
    "*** YOUR CODE HERE ***"
    bestValue = float('-inf')
    bestAction = None
    for action in self.getLegalActions(state):
      if self.getQValue(state,action) > bestValue:
        bestValue = self.getQValue(state,action)
        bestAction = action
    return bestAction


  def getAction(self, state):
    """
      Compute the action to take in the current state.  With
      probability self.epsilon, we should take a random action and
      take the best policy action otherwise.  Note that if there are
      no legal actions, which is the case at the terminal state, you
      should choose None as the action.

      HINT: You might want to use util.flipCoin(prob)
      HINT: To pick randomly from a list, use random.choice(list)
    """
    "*** YOUR CODE HERE ***"
    bestAction = self.getPolicy(state)
    all_actions = self.getLegalActions(state)
    randomAction = random.choice(all_actions)
    if util.flipCoin(self.epsilon) or bestAction == None:
      return randomAction
    return bestAction


  def update(self, state, action, nextState, reward):
    """
      The parent class calls this to observe a
      state = action => nextState and reward transition.
      You should do your Q-Value update here

      NOTE: You should never call this function,
      it will be called on your behalf
    """
    "*** YOUR CODE HERE ***"
    currentQValue = self.getQValue(state, action)

    nextValue = self.getValue(nextState)

    updatedQValue = ((1-self.alpha)*currentQValue) + (self.alpha * (reward + (self.discount * (nextValue))))

    self.setQValue(state, action, updatedQValue)


class PacmanQAgent(QLearningAgent):
  "Exactly the same as QLearningAgent, but with different default parameters"

  def __init__(self, epsilon=0.05,gamma=0.8,alpha=0.2, numTraining=0, **args):
    """
    These default parameters can be changed from the pacman.py command line.
    For example, to change the exploration rate, try:
        python pacman.py -p PacmanQLearningAgent -a epsilon=0.1

    alpha    - learning rate
    epsilon  - exploration rate
    gamma    - discount factor
    numTraining - number of training episodes, i.e. no learning after these many episodes
    """
    args['epsilon'] = epsilon
    args['gamma'] = gamma
    args['alpha'] = alpha
    args['numTraining'] = numTraining
    self.index = 0  # This is always Pacman
    QLearningAgent.__init__(self, **args)

  def getAction(self, state):
    """
    Simply calls the getAction method of QLearningAgent and then
    informs parent of action for Pacman.  Do not change or remove this
    method.
    """
    action = QLearningAgent.getAction(self,state)
    self.doAction(state,action)
    return action


class PacmanQAgent2(QLearningAgent):
  """Exactly the same as QLearningAgent, but with expert MDP state
     methods from QLearning must use getQValue and setQValue only !!!
  """

  def __init__(self, **args):
    self.index = 0  # This is always Pacman
    QLearningAgent.__init__(self, **args)

  def expertState(self, state):
    """
      Redefine the MDP state from the state of the pacman game (type GameState)
    """

    return GameStateDataSmall(state)


  def setQValue(self,state,action,value):
    """
      Must be redefined to use the update function of the parent class
      """
    self.qvalues[(self.expertState(state), action)] = value

  def getQValue(self, state, action):
    """
      Must be redefined to use functions of the parent class
      """
    return QLearningAgent.getQValue(self,self.expertState(state),action)

  def getAction(self, state):
    """
    Simply calls the getAction method of QLearningAgent and then
    informs parent of action for Pacman.  Do not change or remove this
    method.
    """

    action = QLearningAgent.getAction(self,state)
    self.doAction(state,action)
    return action



class ApproximateQAgent(PacmanQAgent):
  """
     ApproximateQLearningAgent

     You should only have to overwrite getQValue
     and update.  All other QLearningAgent functions
     should work as is (assuming that your methods
     in QLearningAgent call getQValue instead of accessing Q-values directly)
  """
  def __init__(self, extractor='IdentityExtractor', **args):
    self.featExtractor = util.lookup(extractor, globals())()
    PacmanQAgent.__init__(self, **args)

    # You might want to initialize weights here.
    "*** YOUR CODE HERE ***"
    self.weights = util.Counter()

  def getQValue(self, state, action):
    """
      Should return Q(state,action) = w * featureVector
      where * is the dotProduct operator
    """
    "*** YOUR CODE HERE ***"
    features = self.featExtractor.getFeatures(state, action)

    q_value = 0.0
    for feature, value in features.items():
        q_value += self.weights[feature] * value

    return q_value

  def update(self, state, action, nextState, reward):
    """
       Should update your weights based on transition
    """
    "*** YOUR CODE HERE ***"
    features = self.featExtractor.getFeatures(state, action)
        
    nextValue = self.getValue(nextState)  # max_a' Q(nextState, a')
    currentQValue = self.getQValue(state, action)  # Q(state, action)
    td_error = (reward + self.discount * nextValue) - currentQValue
        
    for feature, value in features.items():
        self.weights[feature] += self.alpha * td_error * value

  def final(self, state):
    "Called at the end of each game."
    # call the super-class final method
    PacmanQAgent.final(self, state)

    # did we finish training?
    if self.episodesSoFar == self.numTraining:
      # you might want to print your weights here for debugging
      "*** YOUR CODE HERE ***"
      for feature, weight in self.weights.items():
        print(f"Feature: {feature}, Weight: {weight}")
