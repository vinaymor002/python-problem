N = int(raw_input())


def find_level(i, level, immediate_superiors):
    if i == 0:
        return 0
    if level[i] != -1:
        return level[i]+1
    else:
        _level = find_level(immediate_superiors[i - 1], level, immediate_superiors)
        level[i] = _level
        return _level + 1


while N > 0:
    N -= 1
    number_of_soldiers = int(raw_input())
    immediate_superiors = [int(x) for x in raw_input().split()]
    hand_shake_count = 0
    level = [-1] * (number_of_soldiers + 1)

    for index, i in enumerate(immediate_superiors):
        if level[index + 1] == -1:
            _level = find_level(i, level, immediate_superiors)
            level[index + 1] = _level
        hand_shake_count += level[index + 1]

    total_possible_interactions = number_of_soldiers * (number_of_soldiers - 1) / 2

    fist_bumps_count = total_possible_interactions - hand_shake_count

    print hand_shake_count, fist_bumps_count



