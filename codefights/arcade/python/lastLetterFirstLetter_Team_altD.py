# Python 2

class Team(object):
    def __init__(self, names):
        self.names = names

    def __bool__(self):
        nsolutions = 0
        def search(sequences, ord_minc, curr_word, current_path, current_path_len, longest_path):
            current_path[current_path_len] = curr_word
            current_path_len += 1
            if current_path_len == len(longest_path):
                nsolutions += 1
            elif current_path_len > len(longest_path):
                nsolutions = 1
                longest_path[:] = current_path[:current_path_len]

            last_char_index = ord(curr_word[-1]) - ord_minc
            if last_char_index >= 0 and last_char_index < len(sequences):
                for pair in sequences[last_char_index]:
                    if not pair[1]:
                        pair[1] = True
                        search(sequences, ord_minc, pair[0], current_path, current_path_len, longest_path)
                        pair[1] = False
        def find_longest_chain(words):
            ord_minc = ord(min(word[0] for word in words))
            ord_maxc = ord(max(word[0] for word in words))
            sequences = [[] for _ in xrange(ord_maxc - ord_minc + 1)]
            for word in words:
                sequences[ord(word[0]) - ord_minc].append([word, False])
            current_path = [None] * len(words)
            longest_path = []

            for seq in sequences:
                for pair in seq:
                    pair[1] = True
                    search(sequences, ord_minc, pair[0], current_path, 0, longest_path)
                    pair[1] = False
            return longest_path
        sol = find_longest_chain([name.lower() for name in self.names])
        return len(sol) == len(self.names)
        

def isCoolTeam(team):
    return bool(Team(team))
