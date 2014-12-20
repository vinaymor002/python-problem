T = int(raw_input())


def calculate_water(building_heights, starting_index, largest_ending_index):
    height = 0
    if building_heights[starting_index] < building_heights[largest_ending_index]:
        height = building_heights[starting_index]
    else:
        height = building_heights[largest_ending_index]

    total = 0
    for index in range(starting_index + 1, largest_ending_index):
        total += height - building_heights[index]
    return total


while T > 0:
    T -= 1
    N = int(raw_input())
    building_heights = [int(x) for x in raw_input().split()]

    total_water_stored = 0
    starting_building_height = -1
    ending_building_height = -1
    starting_index = 0
    largest_ending_index = -1
    i = 1
    while i < N:
        sumed = False
        if building_heights[i] < building_heights[starting_index]:
            if building_heights[i] > building_heights[largest_ending_index] or largest_ending_index == -1:
                largest_ending_index = i
        elif building_heights[i] >= building_heights[starting_index]:
            largest_ending_index = i
            total_water_stored += calculate_water(building_heights, starting_index, largest_ending_index)
            starting_index = largest_ending_index
            largest_ending_index = -1
            sumed = True
        i += 1
        if i == N and sumed is False:
            total_water_stored += calculate_water(building_heights, starting_index, largest_ending_index)
            starting_index = largest_ending_index
            i = largest_ending_index + 1
            largest_ending_index = -1
    print total_water_stored % 1000000007