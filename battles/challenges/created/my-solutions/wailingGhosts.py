def wailingGhosts(sounds):      
    while sounds:
        if sounds[0] == "u":
            return False
        try:
            left_os = sounds.index('u')
        except ValueError:
            return False

        # consume left os
        sounds = sounds[left_os:]

        try:
            first_right_o = sounds.index('o')
        except ValueError:
            return False

        # consume us
        sounds = sounds[first_right_o:]

        # consume right os
        if len(sounds) < left_os:
            # not enough right os
            return False

        sounds = sounds[left_os:]

    return True


tests = """
"""
