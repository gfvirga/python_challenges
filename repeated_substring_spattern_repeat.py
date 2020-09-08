def get_duplicates(s):
    substring=""

    # Identify sub string
    for letter in s:
        if letter in substring:
            break
        else:
            substring += letter

    substring_helper = substring[0]
    substring_max = len(substring)
    substring_counter = 0
    substring_last = substring[substring_max -1 ]
    string_last = s[len(s) -1 ]
    
    for letter in s:
        if letter == substring_helper:
            #print(letter + "-" + str(substring_counter) + "-" + substring_helper)
            substring_counter += 1
            if substring_counter < substring_max:
                substring_helper = substring[substring_counter]
            if letter == substring_last:
                substring_counter = 0
                substring_helper = substring[substring_counter]
        else:
            return False
            print("ught")

    print string_last
    print substring_last
    if string_last == substring_last:
        print("true")
        return True
    else:
        print("ught")
        return False

string = "abaababaab"
get_duplicates(string)