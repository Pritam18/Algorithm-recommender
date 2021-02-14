import os
import pandas as pd


class DataKnowledge:
    def __init__(self, input_file):
        self.input_file = input_file

    def get_file_extension(self):
        file_name, file_extension = os.path.splitext(self.input_file)
        if file_extension == '.png' or file_extension == '.jpg':
            return 0
        elif file_extension == '.csv':
            return 1
        elif file_extension == '.txt':
            return 2
        else:  # unknown file format
            return 3

    def get_data_type(self):
        """
        To extract data knowledge this function is for find the type of data. Initially I work with numerical and
        nominal data like WEKA. Our next target is to find the binary, ordinal, continuous and discrete data.
        """
        ext_type = self.get_file_extension()
        if ext_type == 1:
            data = pd.read_csv(self.input_file)
            # print(data['UNITS'].dtype)
            data_type = {}
            for i in range(len(data.columns)):
                if data.dtypes[i] == 'object':
                    data_type[data.columns[i]] = 'nominal'
                elif data[data.columns[i]].isnull().values.all():
                    data_type[data.columns[i]] = 'Empty'
                else:
                    data_type[data.columns[i]] = 'numerical'
            # print(data_type)
            return data_type

    def get_linearity(self):
        ext_type = self.get_file_extension()
        linearity = {}
        if ext_type == 1:
            data_type = self.get_data_type()
            for d_t in data_type:
                if data_type[d_t] == 'numerical':
                    linearity.update({d_t: 'linear'})
                    # print(d_t)
                else:
                    linearity.update({d_t: 'Nonlinear'})
        return linearity
        # print("Hello")

    def get_data_context(self):
        print("Hello")

    def get_location(self):
        print("Hello")

    def feature_size(self):
        """
        To extract data knowledge this function is for find the total number of features.
        """
        ext_type = self.get_file_extension()
        if ext_type == 1:
            data = pd.read_csv(self.input_file)
            return len(data.columns)

    def extract_data_knowledge(self):
        ext_type = self.get_file_extension()
        if ext_type == 1:
            data = pd.read_csv(self.input_file)
            # print(data['UNITS'].dtype)
            # print(len(data.columns))
            return data.dtypes


location = '/Users/pritamkhan/Desktop/Research/Algorithm_Recommender/test_data/Machine_readable_file_bdcsf2020sep.csv'

dk = DataKnowledge(location)
print(dk.get_linearity())
