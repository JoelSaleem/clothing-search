import json
from results import Results
from util import (
    calculate_score, parse_args,
    parse_str_to_tokens, get_target_str
)

if __name__ == "__main__":
    query, dataset = parse_args()

    data = None
    with open(dataset, 'r', encoding='utf-8') as f:
        data = json.loads(f.readlines()[0])

    results = Results(max_size=10)
    query_tokens = parse_str_to_tokens(query)
    for item in data:
        target = get_target_str(item)
        target_tokens = parse_str_to_tokens(target)

        score = calculate_score(target_tokens, query_tokens)
        results.add_item({'score': score, 'item': item})

    print(results)
