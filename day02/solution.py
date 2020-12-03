# PART 1
with open("./input.txt") as f:
    lines = f.read().splitlines()
    num_valid_pw = 0
    for line in lines:
        limits, kw, pw = line.split()
        min_match, max_match = [int(i) for i in limits.split("-")]
        kw = kw.removesuffix(":")
        # test lower bound
        min_pw = pw.replace(kw, "", min_match)
        if len(pw) - len(min_pw) < min_match:
            continue
        # print("lower bound checks out for: ", pw)
        # test higher bound
        max_pw = pw.replace(kw, "", max_match+1)
        if len(pw) - len(max_pw) > max_match:
            continue
        # print("higher bound checks out for ", pw)
        num_valid_pw += 1

    print("Number of valid passwords PT1: ", num_valid_pw)

# PART 2
with open("./input.txt") as f:
    lines = f.read().splitlines()
    num_valid_pw = 0
    for line in lines:
        limits, kw, pw = line.split()
        min_match, max_match = [int(i) for i in limits.split("-")]
        kw = kw.removesuffix(":")
        num_matches = 0
        if pw[min_match-1] == kw:
            num_matches += 1
        if pw[max_match-1] == kw:
            num_matches += 1
        if num_matches == 1:
            num_valid_pw += 1

    print("Number of valid passwords PT2: ", num_valid_pw)
