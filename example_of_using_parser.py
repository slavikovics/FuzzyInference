#%%
from parser import parse_fuzzy_set, parse_fuzzy_implication

list_of_sets = []
list_of_imps = []

list_of_sets.append(parse_fuzzy_set('A = {<a, 1>, <c, 0>, <b, 0.9>}'))
list_of_sets.append(parse_fuzzy_set('B = {<a, 1>, <c, 0>, <b, 0.9>}'))
list_of_sets.append(parse_fuzzy_set('C = {<a, 1>, <c, 0>, <b, 0.9>}'))

list_of_imps.append(parse_fuzzy_implication('A ~> B'))
list_of_imps.append(parse_fuzzy_implication('B ~> C'))

print(list_of_sets)
print(list_of_imps)