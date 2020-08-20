import sys
import csv

CSVFILE = sys.argv[1]

FILENAME_COL = 7
CONTENT_COL = 9

with open(CSVFILE) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            header = row[:] # make a copy of the list containing the first row
        else:
            print(f"Creating file events/{row[FILENAME_COL]}.md")
            fp = open(f'events/{row[FILENAME_COL]}.md', 'w')
            fp.write('---\n')
            for f in range(9):
                # if its the start or end time, the location or title, wrap in
                # quotes (columns start at 0)
                if f == 3 or f == 4 or f == 6 or f == 8: 
                    fp.write(f'{header[f]} "{row[f]}"\n')
                else:
                    fp.write(f'{header[f]} {row[f]}\n')
            fp.write('---\n')
            fp.write('\n')
            fp.write(f'{row[CONTENT_COL]}\n')
            fp.close()

        line_count += 1

