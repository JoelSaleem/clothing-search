from functools import cmp_to_key


def score_comparer(a, b):
    if a['score'] < b['score']:
        return 1
    if a['score'] > b['score']:
        return -1
    return 0


class Results(list):
    '''Hold and display the top results for the search'''

    def __init__(self, max_size):
        self.lowest_score = float('inf')
        self.max_size = max_size

    def assign_lowest_score(self):
        if len(self) == 0:
            self.lowest_score = None
        lowest_score = float('inf')

        for item in self:
            lowest_score = min(item['score'], lowest_score)

        self.lowest_score = lowest_score

    def add_item(self, new_item):
        if len(self) < self.max_size:
            self.append(new_item)
            self.lowest_score = min(self.lowest_score, new_item['score'])
        else:
            if new_item['score'] > self.lowest_score:
                self.append(new_item)
                self.evict_lowest()
                self.assign_lowest_score()

    def evict_lowest(self):
        lowest_score, lowest_idx = float('inf'), -1
        for idx, item in enumerate(self):
            if item['score'] < lowest_score:
                lowest_score, lowest_idx = item['score'], idx

        if lowest_idx > -1:
            del self[lowest_idx]

    def __str__(self):
        ordered_data = sorted(self, key=cmp_to_key(score_comparer))
        data_to_print = []
        for item in ordered_data:
            score = f'Score: {item["score"]}'
            item = str(item['item'])
            data_to_print.append((score, item))

        return '\n'.join('\t'.join(item_details) for item_details in data_to_print)
