from nltk.corpus import wordnet as wn
from pyjarowinkler import distance as ds

from Python_Files.Algorithm_Knowledge import Algorithms


def word_similarity(word1, word2):
    w1 = wn.synsets(word1)
    w2 = wn.synsets(word2)
    if not w1 or not w2:
        jaro_winkler_dist = ds.get_jaro_distance(word1, word2)
        return jaro_winkler_dist
    else:
        w1 = wn.synsets(word1)[0]
        w2 = wn.synsets(word2)[0]
        wu_palmer_dist = w1.wup_similarity(w2)
        return wu_palmer_dist


def info_similarity(information1, information2):
    summed_distance = 0
    for info1 in information1:
        info1_info2_dist_list = []
        for info2 in information2:
            info1_info2_dist_list.append(word_similarity(info1, info2))
        summed_distance += max(info1_info2_dist_list)
    return summed_distance / len(information1)


def similarity_hausdorff(information1, information2):
    return min([info_similarity(information1, information2), info_similarity(information2, information1)])


def match_knowledge(knowledge_datasets, knowledge_goals, knowledge_algorithms, datasets, goals, algorithms):
    for goal in goals:
        max_sim_dataset = -999999
        max_sim_algo = -999999
        for data in datasets:
            sim_g_d = similarity_hausdorff()


# match_knowledge()
wo1 = 'Phone'
wo2 = 'Phonetics'
c = wn.synsets(wo1)
d = wn.synsets(wo2)
# print(d)
# if not c or not d:
#     print("True")
# else:
#     print("False")
# print(c.wup_similarity(d))
# if c is not in wn:
print(word_similarity(wo1, wo2))
