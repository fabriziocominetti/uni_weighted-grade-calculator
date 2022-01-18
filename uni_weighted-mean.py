# Python - Weighted Mean

def weighted_average_uni(score, cfu):
    numerator = sum([score[i]*cfu[i] for i in range(len(score))])
    denominator = sum(cfu)
    return round(numerator/denominator,2)

weighted_average_uni(score, cfu)
