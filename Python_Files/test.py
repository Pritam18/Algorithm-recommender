import os
import pandas as pd


def get_file_extension(input_file):
    file_name, file_extension = os.path.splitext(input_file)
    if file_extension == '.png' or file_extension == '.jpg':
        return 0
    elif file_extension == '.csv':
        return 1
    elif file_extension == '.txt':
        return 2
    else:                       # unknown file format
        return 3


def get_data_type(input_file):
    """
    To extract data knowledge this function is for find the type of data. Initially I work with numerical and
    nominal data like WEKA. Our next target is to find the binary, ordinal, continuous and discrete data.
    :param input_file
    """
    ext_type = get_file_extension(input_file)
    if ext_type == 1:
        data = pd.read_csv(input_file)
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


def get_linearity(input_file):
    """
    To extract data knowledge this function is for find the type of data. Initially I work with numerical and
    nominal data like WEKA. Our next target is to find the binary, ordinal, continuous and discrete data.
    :param input_file
    """
    ext_type = get_file_extension(input_file)
    if ext_type == 1:
        data = pd.read_csv(input_file)
        data_type = get_data_type(input_file)
    print("Hello")


def get_data_context():
    print("Hello")


def get_location():
    print("Hello")


def feature_size(input_file):
    """
    To extract data knowledge this function is for find the total number of features.
    :param input_file
    """
    ext_type = get_file_extension(input_file)
    if ext_type == 1:
        data = pd.read_csv(input_file)
        return len(data.columns)


def extract_data_knowledge(input_file):
    ext_type = get_file_extension(input_file)
    if ext_type == 1:
        data = pd.read_csv(input_file)
        # print(data['UNITS'].dtype)
        # print(len(data.columns))
        return data.dtypes
        

# def extract_goal_knowledge(input_file):
#     print('hello')

# def extract_algo_knowledge():

location = '/Users/pritamkhan/Desktop/Research/Algorithm_Recommender/test_data/Machine_readable_file_bdcsf2020sep.csv'

# print(extract_data_knowledge(location))
# print(extract_data_knowledge(location))
print(get_data_type(location))
# d = pd.read_csv(location)
# print(d['Series_title_4'].isnull().values.all())

print(feature_size(location))

