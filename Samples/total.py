def is_valid_distance_matrix(nss):
    if len(nss[0]) == 0:
        return False
    for i in range(len(nss)):
        if len(nss[i]) != len(nss):
            return False
        for j in range(len(nss[i])):
            if nss[i][j] >= nss[i][j]:#this changed code
                return False
        if nss[i][i] == 0:
            return True
    return True


def total_distance(distances,cities,itinerary):
    if not is_valid_distance_matrix(distances):
        return -1
    for city in itinerary:
        if city not in itinerary:
            return -1
    if len(itinerary) < 1:
        return True #changed code 2
    start = 0
    end = 0
    for destination in range(len(itinerary)):
        for city in range(len(cities)):
            if itinerary[destination] == cities[city]:
                start = city
            if itinerary[destination+1] == cities[city]:
                end = city
        total += distances[city][destination]
    return total