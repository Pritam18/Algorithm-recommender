import os
import pandas as pd


class DataKnowledge:
    def __init__(self, dataset_properties, iterator):
        self.dataset_properties = pd.read_csv(dataset_properties)
        self.iterator = iterator
        self.input_file = self.dataset_properties.iloc[self.iterator]['File Location']

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
            data_type_list = []
            for i in range(len(data.columns)):
                if data.dtypes[i] == 'object':
                    data_type[data.columns[i]] = 'nominal'
                    data_type_list.append('nominal')
                elif data[data.columns[i]].isnull().values.all():
                    data_type[data.columns[i]] = 'Empty'
                else:
                    data_type[data.columns[i]] = 'numerical'
                    data_type_list.append('numerical')
            # print(data_type)
            return data_type, data_type_list

    def get_linearity(self):
        ext_type = self.get_file_extension()
        linearity = {}
        linearity_list = []
        linear_counter = 0
        if ext_type == 1:
            data_type, data_type_list = self.get_data_type()
            for d_t in data_type:
                if data_type[d_t] == 'numerical':
                    linearity.update({d_t: 'linear'})
                    linear_counter += 1
                    linearity_list.append('linear')
                    # print(d_t)
                else:
                    linearity.update({d_t: 'Nonlinear'})
                    linearity_list.append('Nonlinear')
        return linearity, linear_counter, linearity_list
        # print("Hello")

    def get_data_context(self):
        return self.dataset_properties.iloc[self.iterator]['Context']

    def get_location(self):
        return self.dataset_properties.iloc[self.iterator]['Location']

    def get_feature_size(self):
        """
        To extract data knowledge this function is for find the total number of features.
        """
        ext_type = self.get_file_extension()
        if ext_type == 1:
            data = pd.read_csv(self.input_file)
            return len(data.columns)

    def extract_data_knowledge(self):
        data_type, data_type_list = self.get_data_type()
        linearity, linear_counter, linearity_list = self.get_linearity()
        data_list = [data_type_list, linearity_list, self.get_data_context(), self.get_location()]
        return data_list


location = '../../Data/dataset_properties.csv'
dk = DataKnowledge(location, 0)
print(dk.extract_data_knowledge())
for test in dk.extract_data_knowledge():
    print(type(test))
    if isinstance(test, list):
        print(test)
    else:
        print("HELLO")
