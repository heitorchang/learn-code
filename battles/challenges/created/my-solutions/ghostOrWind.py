def ghostOrWind(sounds):
    if sounds[0] == "O":
        return False
        
    while sounds:
        try:
            left_os = sounds.index('O')
        except ValueError:
            return False

        # consume left os
        sounds = sounds[left_os:]

        try:
            first_right_o = sounds.index('o')
        except ValueError:
            return False

        # consume Os
        sounds = sounds[first_right_o:]

        # consume right os
        if len(sounds) < left_os:
            # not enough right os
            return False

        sounds = sounds[left_os:]

    return True
