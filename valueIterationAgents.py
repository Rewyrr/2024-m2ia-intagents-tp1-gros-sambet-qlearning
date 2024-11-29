# valueIterationAgents.py
# -----------------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
  """
      * Please read learningAgents.py before reading this.*

      A ValueIterationAgent takes a Markov decision process
      (see mdp.py) on initialization and runs value iteration
      for a given number of iterations using the supplied
      discount factor.
  """
  def __init__(self, mdp, discount = 0.9, iterations = 100):
    """
      Your value iteration agent should take an mdp on
      construction, run the indicated number of iterations
      and then act according to the resulting policy.

      Some useful mdp methods you will use:
          mdp.getStates()
          mdp.getPossibleActions(state)
          mdp.getTransitionStatesAndProbs(state, action)
          mdp.getReward(state, action, nextState)
    """
    self.mdp = mdp
    self.discount = discount
    self.iterations = iterations
    self.values = util.Counter() # A Counter is a dict with default 0

    if self.iterations == -1:
        self.runValueIterationCv()
        print(f"{self.iterations } iterations to converge")
    else:
        self.runValueIteration(self.iterations)

  def runValueIteration(self,iter):
     """
        Run the indicated number of iterations
     """
     "*** YOUR CODE HERE ***"
      
     for i in range(iter):
        # Copie des valeurs pour éviter de modifier self.values lors de l'itération
        next_values = self.values.copy()
        # Parcourir chaque état du MDP
        for state in self.mdp.getStates():
            # Si l'état est terminal, ne rien changer
            if self.mdp.isTerminal(state):
                continue
            # Calculer la valeur maximale de Q(s, a) sur toutes les actions possibles
            max_value = float('-inf')
            for action in self.mdp.getPossibleActions(state):
                q_value = self.getQValue(state, action)
                max_value = max(max_value, q_value)
            next_values[state] = max_value
        # Mettre à jour les valeurs pour la prochaine itération
        self.values = next_values

  def runValueIterationCv(self):
     """
        Run until convergence
     """
     "*** YOUR CODE HERE ***"
     epsilon = 1e-3  # Critère d'arrêt
     converged = False
     while not converged:
        next_values = self.values.copy()
        converged = True
        for state in self.mdp.getStates():
            if self.mdp.isTerminal(state):
                continue
            max_value = float('-inf') 
            for action in self.mdp.getPossibleActions(state):
                q_value = self.getQValue(state, action)
                max_value = max(max_value, q_value)
            if abs(self.values[state] - max_value) > epsilon:
                converged = False
            next_values[state] = max_value
        self.values = next_values
 
    
  def getValue(self, state):
    """
      Return the value of the state (computed in __init__).
    """
    return self.values[state]


  def getQValue(self, state, action):
    """
      The q-value of the state action pair
      (after the indicated number of value iteration
      passes).  Note that value iteration does not
      necessarily create this quantity and you may have
      to derive it on the fly.
    """
    "*** YOUR CODE HERE ***"
    q_value = 0
    # Obtenir les états de transition et les probabilités associées
    for next_state, prob in self.mdp.getTransitionStatesAndProbs(state, action):
        # Calculer la récompense pour l'état, action, état suivant
        reward = self.mdp.getReward(state, action, next_state)
        # Ajouter la contribution de cet état de transition à la Q-value
        q_value += prob * (reward + self.discount * self.values[next_state])
    return q_value
      
  def getPolicy(self, state):
    """
      The policy is the best action in the given state
      according to the values computed by value iteration.
      You may break ties any way you see fit.  Note that if
      there are no legal actions, which is the case at the
      terminal state, you should return None.
    """
    "*** YOUR CODE HERE ***"
    if self.mdp.isTerminal(state):
        return None
    best_action = None
    max_value = float('-inf')
    # Explorer toutes les actions possibles dans l'état donné
    for action in self.mdp.getPossibleActions(state):
        q_value = self.getQValue(state, action)
        if q_value > max_value:
            max_value = q_value
            best_action = action
    return best_action

  def getAction(self, state):
    "Returns the policy at the state (no exploration)."
    return self.getPolicy(state)
  
