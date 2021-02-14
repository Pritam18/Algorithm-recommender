import pandas as pd
import csv


class GoalKnowledge:
    def __init__(self, goal_input):
        self.goal_input = pd.read_csv(goal_input)

    def get_goal_process(self):
        process_list = []
        for line in csv.reader(self.goal_input['Process']):
            process_list.append(line[0])
        return process_list

    def get_goal_data_type(self):
        data_type_list = []
        for line in csv.reader(self.goal_input['Data Type']):
            data_type_list.append(line[0])
        return data_type_list

    def get_goal_model_type(self):
        model_type_list = []
        for line in csv.reader(self.goal_input['Model Type']):
            model_type_list.append(line[0])
        return model_type_list

    def get_goal_context(self):
        goal_target_list = []
        print(self.goal_input.iloc[0]['Goal Context'])
        for line in csv.reader(self.goal_input['Goal Context']):
            goal_target_list.append(line[0])
        return goal_target_list

    def get_goal_location(self):
        goal_location_list = []
        for line in csv.reader(self.goal_input['Goal Location']):
            # print(line[0])
            goal_location_list.append(line[0])
        return goal_location_list

    def extract_goal_knowledge(self):
        print('hello')


location = '../../Goal/goals.csv'
gk = GoalKnowledge(location)
print(gk.get_goal_context())