import numpy as np

class ReinforcementLearningAgent:
    def __init__(self, learning_rate=0.1, discount_factor=0.9):
        self.q_table = {}
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor

    def choose_action(self, state):
        if state not in self.q_table:
            self.q_table[state] = np.zeros(2)  # Assume two actions
        return np.argmax(self.q_table[state])

    def update_q_value(self, state, action, reward, next_state):
        if state not in self.q_table:
            self.q_table[state] = np.zeros(2)
        best_next_action = np.argmax(self.q_table[next_state])
        td_target = reward + self.discount_factor * self.q_table[next_state][best_next_action]
        self.q_table[state][action] += self.learning_rate * (td_target - self.q_table[state][action])