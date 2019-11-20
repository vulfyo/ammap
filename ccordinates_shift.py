import re
import ast

with open('ukraineLow.js', 'r') as source_file:
    with open('ukraineLow_new.js', 'w') as dest_file:
        for source_line in source_file:
            if re.search(r'^\[[-\w\.,\s]+\]', source_line.strip()):
                source_line = source_line.strip()
                if source_line[-1] == ',':
                    was_comma = True
                    source_line = source_line[0:-1]
                else:
                    was_comma = False

                coord = ast.literal_eval(source_line)
                if coord[0] < 0:
                    # меньше - вправо
                    # больше влево
                    coord[0] = round(coord[0] - 100 + 360, 3)
                    coord[1] = round(coord[1] + 0.0015, 3)
                else:
                    coord[0] = round(coord[0] - 100, 3)
                    coord[1] = round(coord[1], 3)
                if was_comma:
                    dest_line = '[{}, {}],'.format(coord[0], coord[1])
                else:
                    dest_line = '[{}, {}]'.format(coord[0], coord[1])
            else:
                dest_line = source_line
            dest_file.writelines(dest_line)

