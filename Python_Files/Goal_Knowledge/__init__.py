import pandas as pd
import csv


class GoalKnowledge:
    def __init__(self, goal_input, iterator):
        self.goal_input = pd.read_csv(goal_input)
        self.iterator = iterator

    def get_goal_process(self):
        # process_list = []
        # for line in csv.reader(self.goal_input['Process']):
        #     process_list.append(line[0])
        return self.goal_input.iloc[self.iterator]['Process']

    def get_goal_data_type(self):
        return self.goal_input.iloc[self.iterator]['Data Type']

    def get_goal_model_type(self):
        return self.goal_input.iloc[self.iterator]['Model Type']

    def get_goal_context(self):
        return self.goal_input.iloc[self.iterator]['Goal Context']

    def get_goal_location(self):
        return self.goal_input.iloc[self.iterator]['Goal Location']

    def extract_goal_knowledge(self):
        goal_list = [self.get_goal_process(), self.get_goal_data_type(), self.get_goal_model_type(),
                     self.get_goal_context(), self.get_goal_location()]
        return goal_list


location = '../../Goal/goals.csv'
for i in range(2):
    gk = GoalKnowledge(location, i)
    print(gk.extract_goal_knowledge())