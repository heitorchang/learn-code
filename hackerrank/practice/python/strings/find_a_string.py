import re

def count_substring(string, sub_string):
    p = re.compile(sub_string)
    count = 0
    for i in range(len(string)):
        # match checks at the beginning of the string
        if p.match(string[i:]) is not None:
            count += 1
    return count

def alt_count(string, sub_string):
    # http://stackoverflow.com/questions/18933711/python-find-all-occurances-of-a-substring-including-overlap
    # [m.start() for m in re.finditer('(?={0})'.format(re.escape("cdc")), "abcdcdc")
    return len(re.findall(r'(?={0})'.format(sub_string), string))
