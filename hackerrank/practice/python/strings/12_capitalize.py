def capitalize(string):
    # must keep whitespace intact
    # str.title() does not work because 12abc becomes 12Abc
    result = ""
    last_is_space = True
    
    for c in string:
        if last_is_space and c.isalpha():
            result += c.upper()
            last_is_space = False
        else:
            if c.isspace():
                last_is_space = True
            else:
                last_is_space = False
            result += c
    return result

if __name__ == "__main__":
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)
