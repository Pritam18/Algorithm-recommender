import os
import pandas as pd
import csv
from nltk.corpus import wordnet as wn


def get_file_extension(input_file):
    file_name, file_extension = os.path.splitext(input_file)
    if file_extension == '.png' or file_extension == '.jpg':
        return 0
    elif file_extension == '.csv':
        return 1
    elif file_extension == '.txt':
        return 2
    else:  # unknown file format
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


def get_goal_process():
    print("Hello")


def get_goal_data_type():
    print("Hello")


def get_goal_model_type():
    print("Hello")


def get_goal_target():
    print("Hello")


def get_goal_location():
    print("Hello")


def extract_goal_knowledge(input_file):
    print('hello')


def extract_algo_knowledge():
    algo_property = '../Algorithm_properties/Algorithm_info.csv'
    algo_info_list = []
    # print(pd.read_csv(algo_property))
    with open(algo_property, 'r') as info:
        for line in csv.reader(info):
            algo_info_list.append(line)
    return algo_info_list[1:]


def match_knowledge():
    algo_info = extract_algo_knowledge()
    a = wn.synsets('classify')[0]
    for a_i in algo_info[0]:
        print(a_i)
        print(wn.synsets(a_i))
        b = wn.synsets(a_i)
        if b:
            for tr in range(len(b)):
                print(a.wup_similarity(b[tr]))


location = '/Users/pritamkhan/Desktop/Research/Algorithm_Recommender/test_data/Machine_readable_file_bdcsf2020sep.csv'

# print(extract_data_knowledge(location))
# print(extract_data_knowledge(location))
print(get_data_type(location))
# d = pd.read_csv(location)
# print(d['Series_title_4'].isnull().values.all())

print(feature_size(location))
print(extract_algo_knowledge())
match_knowledge()
