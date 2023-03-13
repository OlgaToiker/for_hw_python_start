def print_operation_table(operation, num_rows, num_columns):
    for x in range(1, num_rows + 1):
        tbl = []
        for y in range(1, num_columns + 1):
            tbl.append(str(operation(x, y)))
        print("\t".join(tbl))

print_operation_table(lambda x, y: x * y, 6, 6)