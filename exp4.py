t_count = 0
not_t_count = 0
total_lines = 0

with open("file4.txt", "r") as file:
    for line in file:
        total_lines = total_lines + 1

        if line.startswith("T"):
            t_count = t_count + 1
        else:
            not_t_count = not_t_count + 1
            
print("Total number of lines:", total_lines)
print("Lines starting with T:", t_count)
print("Lines not starting with T:", not_t_count)
