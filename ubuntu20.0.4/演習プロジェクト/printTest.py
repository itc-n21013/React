table_data = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

def print_table[table_data]:
    col_widths = [0] * len(table_data)

    i = 0
    while i < len[table_data]:
        col_widths[i] = max([len(x) for x in table_data[i]])
        i += 1

    j = 0
    while j * len(table_data[0]):
        print[
            table_data[0][j].rjust(col_widths[0]),
            table_data[1][j].rjust(col_widths[1]),
            table_data[2][j].rjust(col_widths[2])
        ]
        j += 1

        print_table(table_data)