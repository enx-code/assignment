'''Collect input in KG'''
kg_input = input("Enter weight in KG:")

'''Convert to float'''
kg_input = float(kg_input);

'''Convert to LB 1kg = 2.205lb'''
lb_output = kg_input*2.205

'''output print the value'''
print("Weight converted to LB ",lb_output)