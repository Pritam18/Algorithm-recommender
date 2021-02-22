import pandas as pd


class Algorithms:
    def __init__(self, algorithm_properties, iterator):
        self.algorithm_properties = pd.read_csv(algorithm_properties)
        self.iterator = iterator

    def expected_algorithm(self):
        return self.algorithm_properties.iloc[self.iterator]['Algorithm']

    def algo_sensitivity(self):
        return self.algorithm_properties.iloc[self.iterator]['Sensitivity']

    def algo_expected_data_type(self):
        return self.algorithm_properties.iloc[self.iterator]['Expected Data Type']

    def algo_expected_output_type(self):
        return self.algorithm_properties.iloc[self.iterator]['Expected Output Type']

    def algo_process(self):
        return self.algorithm_properties.iloc[self.iterator]['Expected Process']

    def algo_continuity(self):
        return self.algorithm_properties.iloc[self.iterator]['Continuity']

    def extract_algo_knowledge(self):
        algo_info_list = [self.algo_sensitivity(), self.algo_expected_data_type(),
                          self.algo_expected_output_type(), self.algo_process(), self.algo_continuity()]
        # with open(algo_property, 'r') as info:
        #     for line in csv.reader(info):
        #         algo_info_list.append(line)
        return algo_info_list


algo_property = '../../Algorithm_properties/Algorithm_info.csv'
a = Algorithms(algo_property, 0)
print(a.expected_algorithm())
print(a.extract_algo_knowledge())
