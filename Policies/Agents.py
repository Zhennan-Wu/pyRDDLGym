from abc import ABCMeta, abstractmethod
import random


class BaseAgent(metaclass=ABCMeta):

    @abstractmethod
    def sample_action(self, state):
        pass


class RandomAgent(BaseAgent):
    def __init__(self, action_space, num_actions=1):
        self.action_space = action_space
        self.num_actions = num_actions

    def sample_action(self, state=None):
        s = self.action_space.sample()
        action = {}
        selected_actions = random.sample(list(s), self.num_actions)
        for sample in selected_actions:
            action[sample] = s[sample][0].item()
        return action

    # used to test rover, delete later
    def sample_action_rover(self, state=None):
        s = self.action_space.sample()
        action = {}
        selected_actions = random.sample(list(s), self.num_actions)
        for sample in selected_actions:
            # print(s[sample])
            if sample == 'snapPicture':
                if s[sample] == 1:
                    action[sample] = True
                else:
                    action[sample] = False
            else: 
                action[sample] = s[sample][0].item()
        return action
    