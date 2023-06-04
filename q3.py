import math


city_bank_locations = [
    (1, 23.8728568, 90.3984184, "Uttara Branch"),
    (2, 23.8513998, 90.3944536, "City Bank Airport"),
    (3, 23.8330429, 90.4092871, "City Bank Nikunja"),
    (4, 23.8679743, 90.3840879, "City Bank Beside Uttara Diagnostic"),
    (5, 23.8248293, 90.3551134, "City Bank Mirpur 12"),
    (6, 23.827149, 90.4106238, "City Bank Le Meridien"),
    (7, 23.8629078, 90.3816318, "City Bank Shaheed Sarani"),
    (8, 23.8673789, 90.429412, "City Bank Narayanganj"),
    (9, 23.8248938, 90.3549467, "City Bank Pallabi"),
    (10, 23.813316, 90.4147498, "City Bank JFP")
]


def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371  
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = R * c
    return distance


def find_best_route(locations):
    num_locations = len(locations)
    unvisited = set(range(1, num_locations))  
    current_location = 0  
    best_route = [current_location]
    total_distance = 0

    while unvisited:
        nearest_location = min(unvisited, key=lambda x: calculate_distance(
            locations[current_location][1], locations[current_location][2],
            locations[x][1], locations[x][2]))
        unvisited.remove(nearest_location)
        best_route.append(nearest_location)
        total_distance += calculate_distance(
            locations[current_location][1], locations[current_location][2],
            locations[nearest_location][1], locations[nearest_location][2])
        current_location = nearest_location

   
    total_distance += calculate_distance(
        locations[current_location][1], locations[current_location][2],
        locations[0][1], locations[0][2])
    best_route.append(0)

    return best_route, total_distance


best_route, total_distance = find_best_route(city_bank_locations)


print("Best Route:")
for location_id in best_route:
    location = city_bank_locations[location_id]
    print(f"{location[0]}. {location[3]}")
print(f"\nTotal Distance: {total_distance} km")
