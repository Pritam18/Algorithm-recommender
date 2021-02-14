import csv


class Algorithms:
    @staticmethod
    def extract_algo_knowledge():
        algo_property = '../../Algorithm_properties/Algorithm_info.csv'
        algo_info_list = []
        with open(algo_property, 'r') as info:
            for line in csv.reader(info):
                algo_info_list.append(line)
        return algo_info_list[1:]


a = Algorithms()
print(a.extract_algo_knowledge())
