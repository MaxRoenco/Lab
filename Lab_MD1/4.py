from prettytable import PrettyTable


org_exp = input("Your expression: ")

variables = {}
for e in list(org_exp):
    if e.isalpha():
        variables[e] = []

exp = org_exp.replace('+', ' | ')
exp = exp.replace('*', ' & ')
exp = exp.replace('!', ' ~ ')

num_vars = len(variables)
num_combinations = 2 ** len(variables)

for i in range(num_combinations):
    binary = f'{i:0{num_vars}b}'
    bin = str(binary)
    j = 0
    for key in variables:
        variables[key].append(int(bin[j]))
        j += 1

results = []
for i in range(num_combinations):
    new_exp = exp
    for key in variables:
        new_exp = new_exp.replace(key, str(variables[key][i]))
    results.append(int(eval(new_exp)))

table = PrettyTable()

for key in variables:
    table.field_names.append(key)
    table.align[key] = 'l'
    table.valign[key] = 'm'
table.field_names.append(org_exp)
table.align[org_exp] = 'm'
table.valign[org_exp] = 'm'

for i in range(num_combinations):
    row = []
    for key in variables:
        row.append(variables[key][i])
    row.append(results[i])
    table.add_row(row)

print(table)
