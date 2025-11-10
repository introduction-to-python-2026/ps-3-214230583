n_terms = 10
list_of_numbers = []
for i in range(n_terms):
    list_of_numbers.append(i)
list_of_alternating_signs = []
for i in range (n_terms):
  if i % 2 == 0:
    list_of_alternating_signs.append(1)
  else:
    list_of_alternating_signs.append(-1)

list_of_alternating_signs
leibniz_series = []
for i in range(n_terms):
    term = ((-1)**i) / (2 * i + 1)
    leibniz_series.append(term)

leibniz_series
sum_leibniz_series = sum(leibniz_series)
sum_leibniz_series
pi = 4 * sum_leibniz_series
pi
    def approximate_pi(n_terms):
    leibniz_series = []
    for i in range(n_terms):
        term = ((-1)**i) / (2 * i + 1)
        leibniz_series.append(term)
    
    sum_leibniz_series = sum(leibniz_series)
    pi_approximation = 4 * sum_leibniz_series
    return pi_approximation
