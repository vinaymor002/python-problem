test_case_count = raw_input()

for i in range(int(test_case_count)):
    first_line = [int(x) for x in raw_input().split()]
    # vehicle_count = first_line[0]
    max_petrol = first_line[1]
    initial_petrol_cap_per_vehicle = []
    pakka = []
    i = 1
    for x in raw_input().split():
        int1 = int(x)
        if int1 >= i:
            pakka.append(i)
        else:
            initial_petrol_cap_per_vehicle.append(i-int1)
        i += 1

    load_cap_per_vehicle = []
    i = 1
    _pakka_load = 0

    for x in raw_input().split():
        int2 = int(x)
        if i not in pakka:
            load_cap_per_vehicle.append(int2)
        else:
            _pakka_load += int2
        i += 1

    def consume_petrol(index_p, petrol_left_p):
        if petrol_left_p <= 0:
            return 0

        _petrol_required = initial_petrol_cap_per_vehicle[index_p]
        _load = load_cap_per_vehicle[index_p]

        if index_p + 1 < initial_petrol_cap_per_vehicle.__len__():
            load1 = consume_petrol(index_p + 1, petrol_left_p)
            if _petrol_required <= petrol_left_p:
                load2 = consume_petrol(index_p + 1, petrol_left_p - _petrol_required)
                load2 += _load
                if load1 > load2:
                    return load1
                else:
                    return load2
            return load1

        if _petrol_required <= petrol_left_p:
            return _load
        else:
            return 0

    def consume_petrol_iter():

        pass

    if initial_petrol_cap_per_vehicle.__len__():
        load_sum = consume_petrol(0, max_petrol)
        print load_sum + _pakka_load
    else:
        print _pakka_load