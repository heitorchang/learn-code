final_draft = """
Ms. Andrews, a teacher at the "Cymbal University", is getting things ready for the end-of-year concert and needs your help in forming the rock 'n' roll act.

She will give you a list of students and whether they are able to perform in at least one of the four required roles of a rock band: **Bass, Drums, Guitar,** and **Vocals**.

Given this list, you should return the total number of possible permutations (assignments of students to one of the four roles so that a complete band is formed). Listing the names in every permutation will be too long, so here we will only report the total.

Note that it matters where each student will be assigned. If Dave and Lynn both play Bass and Guitar, swapping their roles will count as two different band permutations.

Each element of the student list is a string representing one student in the comma-separated format:

`studentName,skills`

`studentName` may have the student's ID number at the end to help us keep track of who they are.
 
`skills` is a string of up to 4 characters (for example, `BGV`) that represents all the roles the student is able to perform. The roles are abbreviated as their first letters:

(**B**)ass
(**D**)rums
(**G**)uitar
(**V**)ocals

There may be no possible permutation that forms a complete band for some lists. In these cases, output `0`.

__Examples__

For

```
students = ["Dave,BG", "Lynn,BG", "Andy,V", "Lucy,D"]
```

the output should be: `rockBandMembers(students) = 2`. Dave and Lynn can play either Bass and Guitar, and the other two students fill in the roles where they are comfortable performing.

For

```
students = ["Kim,GV",
            "Ben,BDG",
            "Edd,DGV", 
            "Lyn,BDG"]
```

the output should be: `rockBandMembers(students) = 6`.

We have 4 talented students and they can form the band in the ways shown below. The indices in each row correspond to the roles Bass, Drums, Guitar, and Vocals.

```
('Ben,BDG', 'Edd,DGV', 'Lyn,BDG', 'Kim,GV')
('Ben,BDG', 'Lyn,BDG', 'Kim,GV', 'Edd,DGV')
('Ben,BDG', 'Lyn,BDG', 'Edd,DGV', 'Kim,GV')
('Lyn,BDG', 'Ben,BDG', 'Kim,GV', 'Edd,DGV')
('Lyn,BDG', 'Ben,BDG', 'Edd,DGV', 'Kim,GV')
('Lyn,BDG', 'Edd,DGV', 'Ben,BDG', 'Kim,GV')
```

For

```
students = ["Jim,BD", "Ann,V", "Ken,G", "Joe,GV"]
```

the output should be: `rockBandMembers(students) = 0`. Unfortunately, no permutation of this group of students is able to fill every one of the four roles of a rock band. Jim can't be both playing Bass and Drums at the same time.

For

```
students = ["Sara,V", "Mark,BD", "Anna,GV", "Tina,G", "Tony,BDGV", "Neil,BG"]
```

the output should be: `rockBandMembers(students) = 20`. The possible permutations are:

```
('Mark,BD', 'Tony,BDGV', 'Anna,GV', 'Sara,V')
('Mark,BD', 'Tony,BDGV', 'Tina,G', 'Sara,V')
('Mark,BD', 'Tony,BDGV', 'Tina,G', 'Anna,GV')
('Mark,BD', 'Tony,BDGV', 'Neil,BG', 'Sara,V')
('Mark,BD', 'Tony,BDGV', 'Neil,BG', 'Anna,GV')
('Tony,BDGV', 'Mark,BD', 'Anna,GV', 'Sara,V')
('Tony,BDGV', 'Mark,BD', 'Tina,G', 'Sara,V')
('Tony,BDGV', 'Mark,BD', 'Tina,G', 'Anna,GV')
('Tony,BDGV', 'Mark,BD', 'Neil,BG', 'Sara,V')
('Tony,BDGV', 'Mark,BD', 'Neil,BG', 'Anna,GV')
('Neil,BG', 'Mark,BD', 'Anna,GV', 'Sara,V')
('Neil,BG', 'Mark,BD', 'Anna,GV', 'Tony,BDGV')
('Neil,BG', 'Mark,BD', 'Tina,G', 'Sara,V')
('Neil,BG', 'Mark,BD', 'Tina,G', 'Anna,GV')
('Neil,BG', 'Mark,BD', 'Tina,G', 'Tony,BDGV')
('Neil,BG', 'Mark,BD', 'Tony,BDGV', 'Sara,V')
('Neil,BG', 'Mark,BD', 'Tony,BDGV', 'Anna,GV')
('Neil,BG', 'Tony,BDGV', 'Anna,GV', 'Sara,V')
('Neil,BG', 'Tony,BDGV', 'Tina,G', 'Sara,V')
('Neil,BG', 'Tony,BDGV', 'Tina,G', 'Anna,GV')
```

"""

description = """

Ms. Andrews, a teacher at the "Cymbal University", is getting things ready for the end-of-year concert and needs your help in forming the rock 'n' roll act.

She will give you a list of students and whether they are able to perform in at least one of the four required roles of a rock band: **Bass, Drums, Guitar,** and **Vocals**.

Given this list, you should return the total number of possible permutations (assignments of students to one of the four roles that form a complete band). A complete list of names in each permutation will be too long, so we will only report the total.

Note that it is important where each student will be assigned. If Dave and Lynn both play Bass and Guitar, swapping their roles will count as two different band permutations.

Each element of the student list is a string representing a single student in the comma-separated format

`studentName,skills`

`studentName` may have the student's ID number at the end to help us keep track of who they are.

 
`skills` is a string of up to 4 characters such as `BGV` that represents all the roles the student is able to perform. The roles are abbreviated to their first letters:

(**B**)ass
(**D**)rums
(**G**)uitar
(**V**)ocals

There may be no possible permutation for some lists. In these cases, output `0`.

__Examples__

For

```
students = ["Dave,BG", "Lynn,BG", "Andy,V", "Lucy,D"]
```

the output should be: `rockBandMembers(students) = 2`. Dave and Lynn can play either Bass and Guitar, and the other two students fill in the roles where they are comfortable performing.

For

```
students = ["Kim,GV",
            "Ben,BDG",
            "Edd,DGV", 
            "Lyn,BDG"]
```

the output should be: `rockBandMembers(students) = 6`.

We have 4 talented students and they can form the band in the ways shown below. The indices in each row correspond to the roles Bass, Drums, Guitar, and Vocals.

```
('Ben,BDG', 'Edd,DGV', 'Lyn,BDG', 'Kim,GV')
('Ben,BDG', 'Lyn,BDG', 'Kim,GV', 'Edd,DGV')
('Ben,BDG', 'Lyn,BDG', 'Edd,DGV', 'Kim,GV')
('Lyn,BDG', 'Ben,BDG', 'Kim,GV', 'Edd,DGV')
('Lyn,BDG', 'Ben,BDG', 'Edd,DGV', 'Kim,GV')
('Lyn,BDG', 'Edd,DGV', 'Ben,BDG', 'Kim,GV')
```

For

```
students = ["Jim,BD", "Ann,V", "Ken,G", "Joe,GV"]
```

the output should be: `rockBandMembers(students) = 0`. Unfortunately, no permutation of this group of students is able to fill every one of the four roles of a rock band. Jim can't be both playing Bass and Drums at the same time.

For

```
students = ["Sara,V", "Mark,BD", "Anna,GV", "Tina,G", "Tony,BDGV", "Neil,BG"]
```

the output should be: `rockBandMembers(students) = 20`. The possible permutations are:

```
('Mark,BD', 'Tony,BDGV', 'Anna,GV', 'Sara,V')
('Mark,BD', 'Tony,BDGV', 'Tina,G', 'Sara,V')
('Mark,BD', 'Tony,BDGV', 'Tina,G', 'Anna,GV')
('Mark,BD', 'Tony,BDGV', 'Neil,BG', 'Sara,V')
('Mark,BD', 'Tony,BDGV', 'Neil,BG', 'Anna,GV')
('Tony,BDGV', 'Mark,BD', 'Anna,GV', 'Sara,V')
('Tony,BDGV', 'Mark,BD', 'Tina,G', 'Sara,V')
('Tony,BDGV', 'Mark,BD', 'Tina,G', 'Anna,GV')
('Tony,BDGV', 'Mark,BD', 'Neil,BG', 'Sara,V')
('Tony,BDGV', 'Mark,BD', 'Neil,BG', 'Anna,GV')
('Neil,BG', 'Mark,BD', 'Anna,GV', 'Sara,V')
('Neil,BG', 'Mark,BD', 'Anna,GV', 'Tony,BDGV')
('Neil,BG', 'Mark,BD', 'Tina,G', 'Sara,V')
('Neil,BG', 'Mark,BD', 'Tina,G', 'Anna,GV')
('Neil,BG', 'Mark,BD', 'Tina,G', 'Tony,BDGV')
('Neil,BG', 'Mark,BD', 'Tony,BDGV', 'Sara,V')
('Neil,BG', 'Mark,BD', 'Tony,BDGV', 'Anna,GV')
('Neil,BG', 'Tony,BDGV', 'Anna,GV', 'Sara,V')
('Neil,BG', 'Tony,BDGV', 'Tina,G', 'Sara,V')
('Neil,BG', 'Tony,BDGV', 'Tina,G', 'Anna,GV')
```

"""

from random import choice, randint
from string import ascii_uppercase
from itertools import combinations, permutations

def generateInitials():
    return "{}.{}.{}".format(choice(ascii_uppercase), choice(ascii_uppercase), str(randint(10000001, 99999999)))

def generateTestCase(students):
    roles = "BDGV"
    rolechoices = [[], list(combinations(roles, 1)),
                   list(combinations(roles, 2)),
                   list(combinations(roles, 3)),
                   ["BDGV"]]

    stulist = []
    for i in range(students):
        ableroles = randint(1, 4)
        stulist.append("{},{}".format(generateInitials(), ''.join(choice(rolechoices[ableroles]))))

    return stulist

def rockBandMembers(students):
    lens = len(students)
    names = set(s.split(',')[0] for s in students)
    if lens != len(names):
        raise ValueError("Name collision in student list")

    possibilities = permutations(students, 4)

    answer = 0

    rolesyms = "BDGV"
    
    for p in permutations(students, 4):
        # assume first slot is Bass, then Drums, Guitar and Vocals
        pWorks = True
        for i, slot in enumerate(p):
            name, stuRoles = slot.split(",")
            if rolesyms[i] not in stuRoles:
                pWorks = False
                break
        if pWorks:
            print(p)
            answer += 1
            
    return answer
