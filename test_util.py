from util import calculate_score


def test_calc_score_full_match():
    score = calculate_score(
        ['item', 'name', 'brand'], ['item', 'name', 'brand']
    )
    assert score == 1

    score = calculate_score(
        ['item', 'name', 'brand'], ['brand', 'item', 'name']
    )
    assert score == 1

    score = calculate_score(
        ['item', 'name', 'brand'], ['name', 'brand', 'item']
    )
    assert score == 1


def test_calc_score_partial_match():
    score = calculate_score(['descr', 'brand'], ['descr'])
    assert score == 0.5

    score = calculate_score(['descr', 'brand'], ['brand'])
    assert score == 0.5

    score = calculate_score(['item'], ['te'])
    assert score == 0.5


def test_no_match():
    score = calculate_score(['descr', 'brand'], ['jumper'])
    assert score == 0


def test_invalid():
    assert calculate_score(['descr', 'brand'], []) == 0
    assert calculate_score([], ['']) == 0