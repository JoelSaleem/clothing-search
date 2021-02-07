import argparse
from copy import copy


def get_tot_len_of_words(word_arr):
    '''Get the sum of word lengths in an array'''
    return sum(len(word) for word in word_arr)


def find_intersection(target, query):
    '''
    Find intersection of query and target 
    The words in the query do not have to be an exact match
    to those in the target list, but must be a subset.
    '''
    target_tokens, query_tokens = copy(target), copy(query)

    intersection = []
    for query_word in query_tokens:
        for target_idx, target_word in enumerate(target_tokens):
            if query_word in target_word:
                intersection.append(query_word)

                # Don't match same word twice
                target_tokens.pop(target_idx)
                continue

    return intersection


def parse_str_to_tokens(word_str):
    '''Parse a string of words to a list'''

    # Ignore '' as token
    return [word.lower() for word in word_str.split(' ') if word != '']


def is_valid_tokens(tokens_list):
    return tokens_list is not None or len(tokens_list) > 0


def calculate_score(target, query):
    '''Calculate the score of a query matching a particular target'''
    if not is_valid_tokens(target) or not is_valid_tokens(query):
        return 0

    intersection = find_intersection(target, query)
    tot_intersection_len = get_tot_len_of_words(intersection)

    total_target_len = get_tot_len_of_words(target)
    total_query_len = get_tot_len_of_words(query)

    # Find max length between query and target
    max_length = max(total_query_len, total_target_len)
    if max_length == 0:
        # ignore zeroDivError, this will be a score of 0
        return 0

    # Get ratio of match to input
    return tot_intersection_len / max_length


def parse_args():
    '''Parse query from arguments in cli'''
    parser = argparse.ArgumentParser(description='Process query')
    parser.add_argument('query', type=str, help='query the data for items')
    parser.add_argument('dataset', type=str, help='path to dataset')

    args = parser.parse_args()
    return args.query, args.dataset


def get_target_str(item):
    '''Get a string of the target, with relevant fields from item'''
    brand, name = item['brand'].strip(), item['name'].strip()
    return f'{name} {brand}'