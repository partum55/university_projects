# truth_table_combined.py

def check_statements(a_in_M1, a_in_M2, a_in_M3, b_in_M1, b_in_M2, b_in_M3):
    condition_1 = not (a_in_M1 and a_in_M2)
    condition_2 = (a_in_M2 == a_in_M3)
    condition_3 = not (a_in_M2 and not b_in_M3)
    condition_4 = (not b_in_M3 or a_in_M1)
    condition_5 = (a_in_M2 and b_in_M3) or (not a_in_M1 and a_in_M3)

    return condition_1, condition_2, condition_3, condition_4, condition_5

def print_truth_table():
    headers = ['a ∈ M1', 'a ∈ M2', 'a ∈ M3', 'b ∈ M1', 'b ∈ M2', 'b ∈ M3', 
               'Висл. 1', 'Висл. 2', 'Висл. 3', 'Висл. 4', 'Висл. 5', 'Несуперечність']

    print(f"{headers[0]:<8} {headers[1]:<8} {headers[2]:<8} {headers[3]:<8} {headers[4]:<8} {headers[5]:<8} "
          f"{headers[6]:<8} {headers[7]:<8} {headers[8]:<8} {headers[9]:<8} {headers[10]:<8} {headers[11]:<15}")

    for a_in_M1 in [1, 0]:
        for a_in_M2 in [1, 0]:
            for a_in_M3 in [1, 0]:
                for b_in_M1 in [1, 0]:
                    for b_in_M2 in [1, 0]:
                        for b_in_M3 in [1, 0]:
                            cond1, cond2, cond3, cond4, cond5 = check_statements(a_in_M1, a_in_M2, a_in_M3, b_in_M1, b_in_M2, b_in_M3)
                            consistency = all([cond1, cond2, cond3, cond4, cond5])

                            cond1, cond2, cond3, cond4, cond5 = int(cond1), int(cond2), int(cond3), int(cond4), int(cond5)
                            consistency = int(consistency)
                            print(f"{a_in_M1:<8} {a_in_M2:<8} {a_in_M3:<8} {b_in_M1:<8} {b_in_M2:<8} {b_in_M3:<8} "
                                  f"{cond1:<8} {cond2:<8} {cond3:<8} {cond4:<8} {cond5:<8} {consistency:<15}")

def print_filtered_truth_table():
    headers = ['a ∈ M1', 'a ∈ M2', 'a ∈ M3', 'b ∈ M1', 'b ∈ M2', 'b ∈ M3', 
               'Висл. 1', 'Висл. 2', 'Висл. 3', 'Висл. 4', 'Висл. 5', 'Несуперечність']
    print(f"{headers[0]:<8} {headers[1]:<8} {headers[2]:<8} {headers[3]:<8} {headers[4]:<8} {headers[5]:<8} "
          f"{headers[6]:<8} {headers[7]:<8} {headers[8]:<8} {headers[9]:<8} {headers[10]:<8} {headers[11]:<15}")

    for a_in_M1 in [1, 0]:
        for a_in_M2 in [1, 0]:
            for a_in_M3 in [1, 0]:
                for b_in_M1 in [1, 0]:
                    for b_in_M2 in [1, 0]:
                        for b_in_M3 in [1, 0]:
                            cond1, cond2, cond3, cond4, cond5 = check_statements(a_in_M1, a_in_M2, a_in_M3, b_in_M1, b_in_M2, b_in_M3)
                            consistency = all([cond1, cond2, cond3, cond4, cond5])

                            if consistency:  # Виводимо тільки істинні комбінації
                                cond1, cond2, cond3, cond4, cond5 = int(cond1), int(cond2), int(cond3), int(cond4), int(cond5)
                                consistency = int(consistency)
                                print(f"{a_in_M1:<8} {a_in_M2:<8} {a_in_M3:<8} {b_in_M1:<8} {b_in_M2:<8} {b_in_M3:<8} "
                                      f"{cond1:<8} {cond2:<8} {cond3:<8} {cond4:<8} {cond5:<8} {consistency:<15}")

# Спочатку будуємо повну таблицю істинності
print("Повна таблиця істинності:")
print_truth_table()

# Потім фільтруємо і виводимо тільки істинні комбінації
print("\nФільтрована таблиця (тільки несуперечні комбінації):")
print_filtered_truth_table()
