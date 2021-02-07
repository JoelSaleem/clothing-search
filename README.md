# clothing-search

## Installation

1. Ensure that python is installed on the machine on which the query will be executed (https://www.python.org/downloads/)
2. Ensure that pipenv is installed
3. from a terminal, in the root of the director, run the command `pipenv shell`
4. Within the shell run `pipenv install`.

## Running a query

1. from the root of the directory, run the command  
   `python search.py "\<query\>" \<path to dataset\>`
   (Note, your python path variable may differ from the above, if so, you will have to use the path variable selected at installation)  
   E.g. `python search.py "jumper h&m" sample_data.json`

## Running tests

1. Within the shell (see installation), run `pytest`.

## How are scores calculated?

Each result for a query is given a particular score, which is used to rank the relevance of the item. Scores can range from 0 (no match) to 1 (complete match).

The 10 most relevant items are printed to the terminal. Should you wish to adjust the number of most relevant items seen for a particular query, max_size can be changed for the Results (search.py, line 12).

Before calculating the score, the query and fields to be searched (target) are parsed to tokens (list of individual words). The intersection between query tokens and target tokens is calculated.  
The score is equal to the ratio of:  
total length of words in intersection / maximum length of words in either query or target

#### Why is the maximum length of either query or target used?

Calculating the score like this allows for a distribution in which a query that exactly matches the target has a score of 1.  
E.g. target: 'jeans H&M', query: 'jeans H&M' => score: 1

If only the length of the query was used  
target: 'jeans H&M abcd xyz', query: 'jeans H&M' => score: 1  
However, we would like this to be a lower score than the exact match, presented in the first case.

The same reasoning can be applied to understand why the length of the target was not used.

## Tradeoffs

1. Queries of 'jump jumper' can have different scores to 'jumper jump'.  
   I have decided to allow the matching of words to be partial e.g. 'jea' can match 'jeans'. Words can also only be matched once (query 'jeans' will only match one of words in target 'jeans jeans').  
   This is a problem that I would solve if I had more time. It can be solved by trying all permutations and choosing the maximum, however this may come with a significant cost in time complexity (introducing an O(n!) factor, where n is the number of words in the query).

2. Performance:  
   To search, a loop is performed over all items in the dataset. This is not the most performant way of doing things. For example, using a hashmap would be more performant than a bruteforce search, however, this would not allow for a partial search.  
   Alternatively a trie could potentially be used, however, it would not allow for partial matches where the target does not start with the same characters as the query. Permutations would need to be used, increasing time complexity. If I had more time, this avenue would be explored.  
   Also, if one were optimising for space requirements, the solution should involve reading the data in batches rather than loading all of the data into ram at once.

3. Using total **length** of words matched vs ratio of **number** of words matched.  
   In this solution the total length of words were used. This has the benefit of neatly using partial matches on words in the query. However, downsides are that the algorithm prioritises brands with shorter names.  
   E.g. query: 'jeans' for targets: ['jeans asos', 'jeans topman'].  
   'jeans asos' would have a higher ranking, despite the matches being equally relevant.  
   Matching the total number of words could alternatively be used to fix the aforementioned problem. However, this may mean the queries 'jea' and 'jeans' would both equally match the targets 'jeans asos'.  
   Given more time, the algorithm would ideally combine these two approaches.
