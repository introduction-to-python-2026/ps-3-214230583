def approximate_pi(n_terms):
    leibniz_series = []
    for i in range(n_terms):
        term = ((-1)**i) / (2 * i + 1)
        leibniz_series.append(term)
    
    sum_leibniz_series = sum(leibniz_series)
    pi_approximation = 4 * sum_leibniz_series
    return pi_approximation
