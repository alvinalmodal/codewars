def count_positives_sum_negatives(numbers):
    if len(numbers) == 0:
        return []
    positive_count = 0
    sum_of_negatives = 0
    for number in numbers:
        if number > 0:
            positive_count += 1
        else:
            sum_of_negatives += number
    return [positive_count, sum_of_negatives]