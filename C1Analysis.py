import os

# directory = "/home/sammy/Documents/C1/easy-chart-17"
file_paths = []

# for filename in os.listdir(directory):
#     file_path = directory + filename
#     file_paths.append(file_path)
file_path = "/home/sammy/Documents/C1/easy-chart-50 (c1).txt"


def ExtractNotes(file_path):

    lines = []
    lines_after_split = []
    notes = []
    #Used to determine how many taps and holds there are
    note_checker = []
    link_counter = []
    taps = 0
    holds = 0
    drags = 0

    with open(file_path, 'rt') as file:
        for line in file:
            # print(line)
            lines.append(line.rstrip('\n'))

        # Gets rid of \t (TAB) in the file and splits the line into an array
        for x in lines:
            new_lines = x.replace('\t', ' ')
            lines_after_split.append(new_lines.split(' '))
            if (x.find('LINK') != -1):
                drags += 1
            # print(x)

        # Filter between notes
        for y in lines_after_split:
            for x in y:
                if (x.find('NOTE') != -1):
                    notes.append(y)
                else:
                    break

        # Get the value which will determine whether it's a tap or a hold
        for note in notes:
            value = float(note[4])
            note_checker.append(value)

        for num in note_checker:
            if (num > 0.0):
                holds += 1
            elif (num == 0.0):
                taps += 1
            else:
                break
    print("BPM:" + str(float(lines_after_split[1][1])))
    print("Taps:" + str(taps))
    print("Drags:" + str(drags))
    print("Holds:" + str(holds))


ExtractNotes(file_path)
# print(lines_after_split)
# print(notes)
# print(note_checker)




