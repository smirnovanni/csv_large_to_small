import sys
import os

def main(argv):
    file_name = argv[0]
    count_lines = int(argv[1])

    file = open(file_name, "r")
    first_line = file.readline()

    counter = 0
    all_counter = 0
    new_file = open('{}/{}_{}-{}'.format('small_files', os.path.splitext(file_name)[0], 1, count_lines), "w")
    new_file.write('{}{}'.format(first_line, ''))
    for f in file.readlines():
        new_file.write(f)
        counter = counter + 1
        all_counter = all_counter + 1
        if counter == count_lines:
            new_file.close()
            new_file = open('{}/{}_{}-{}'.format('small_files', os.path.splitext(file_name)[0], all_counter - count_lines, all_counter), "w")
            new_file.write('{}{}'.format(first_line, ''))
            counter = 0


if __name__ == '__main__':
    main(sys.argv[1:])
