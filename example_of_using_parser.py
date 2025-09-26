#%%
from parser import FuzzySetParser, ImplicationParser

list_of_sets = []
list_of_imps = []

set_parser = FuzzySetParser(list_of_sets)
imp_parser = ImplicationParser(list_of_imps, list_of_sets)

set_parser.parse('A = {<a, 1>, <c, 0>, <b, 0.9>}')
set_parser.parse('B = {<a, 1>, <c, 0>, <b, 0.9>}')
set_parser.parse('C = {<a, 1>, <c, 0>, <b, 0.9>}')

imp_parser.parse('A ~> B')
imp_parser.parse('B ~> C')

print(list_of_sets)
print(list_of_imps)