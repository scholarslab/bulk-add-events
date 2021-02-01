import sys
import csv

IMAGE_FOLDER = 'workshops'

CSVFILE = sys.argv[1]

FILENAME_COL = 7
TITLE_COL = 8
CONTENT_COL = 9
IMAGE_COL = 10
REGISTER_COL = 11

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
            if row[IMAGE_COL]:
                fp.write(f'![{row[TITLE_COL]}](/assets/post-media/{IMAGE_FOLDER}/{row[IMAGE_COL]})\n')
                fp.write('\n')
            fp.write(f'{row[CONTENT_COL]}\n')
            if row[REGISTER_COL]:
                fp.write('\n')
                fp.write(f'Register here: [{row[REGISTER_COL]} ]({row[REGISTER_COL]})\n')
            fp.close()

        line_count += 1

