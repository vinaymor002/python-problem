first_line = [int(x) for x in raw_input().split()]
number_of_stones = first_line[0]
sayans_jump = first_line[1]
length_of_puddle = first_line[2]

p = [float(x) for x in raw_input().split()]
d = [int(x) for x in raw_input().split()]

repo = {}


def calculate_max(current_position, distance_covered):
    _current_position = current_position
    _p_max = -1

    if repo.get(current_position) is not None:
        return repo.get(current_position)

    if length_of_puddle - d[current_position] <= sayans_jump:
        return p[current_position]

    for current_distance in d[current_position + 1:]:
        if sayans_jump >= current_distance - distance_covered:
            _p = calculate_max(_current_position + 1, d[_current_position + 1])
            if _p > _p_max:
                _p_max = _p
        else:
            break
        _current_position += 1

    repo[current_position] = _p_max * p[current_position]
    return _p_max * p[current_position]


_local_max = -1
i = 0
initial_list = [k if sayans_jump >= k else None for k in d]
for j in d:
    if sayans_jump >= j:
        _p = calculate_max(i, d[i])
        if _p > _local_max:
            _local_max = _p
    else:
        break
    i += 1

if length_of_puddle - d[-1] > sayans_jump:
    print 'IMPOSSIBLE'
else:
    prop = _local_max
    if prop <= 0:
        print 'IMPOSSIBLE'
    else:
        print format(prop, '.6f')