# join all interview data js files into one (loads a lot faster in surge.sh)

import glob

DATA_FOLDER = "/home/heitor/pangloss/data/interview/"

OUTPUT = "/home/heitor/pangloss/only-interview/data/consolidated.js"

with open(OUTPUT, 'w') as out:
    print("var data = [];", file=out)
    for filename in glob.iglob(DATA_FOLDER + "*.js"):
        with open(filename) as current_file:
            print(current_file.read(), file=out)
    print("All done.")

def test():
    pass
