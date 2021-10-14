def load_lines_from_file(filename):
    #example = "Users/sberkson/desktop/CPSC222/data.py"
    infile = open(filename, "r")
    lines = infile.readlines()
    infile.close()
    return lines

def clean_lines(lines):
    for i in range(len(lines)):
        lines[i] = lines[i].strip()

def restructure_data_into_table(lines):
    data = []
    for line in lines:
        values = line.split (",")
        data.append(values)
    return data

def pretty_print(data):
    for line in data:
        for point in line:
            print(point, end=" ")
        print()

def remove_whitespace(data):
    for line in data:
        for i in range(len(line)):
            line[i] = line[i].strip(" ")

def convert_column_to_nums(data, column_index):
    for line in data:
        line[column_index] = float(line[column_index])

lines = load_lines_from_file("data.csv")
clean_lines(lines)
data = restructure_data_into_table(lines)
remove_whitespace(data)
header = data.pop(0)
convert_column_to_nums(data, 2)
print(header)
pretty_print(data)