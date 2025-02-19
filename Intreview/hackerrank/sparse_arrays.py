def matching_strings(stringList, queries):
    results = []
    for query in queries:
        count = 0
        for string in stringList:
            if string == query:
                count += 1
        results.append(count)
    return results


def matching_strings_optimal(stringList, queries):
    counters = {}
    for string in stringList:
        if string in counters:
            counters[string] += 1
        else:
            counters[string] = 1
    return [counters[query] if query in counters else 0 for query in queries]


from collections import Counter
def matching_strings_counter(stringList, queries):
    counters = Counter(stringList)
    return [counters.get(query,0) for query in queries]