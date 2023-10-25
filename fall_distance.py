def falling_distance (fall_time):
    grav = 9.8
    distance_in_meters = (1/2 * grav * fall_time ** 2)
    return distance_in_meters

print(falling_distance(4.5))