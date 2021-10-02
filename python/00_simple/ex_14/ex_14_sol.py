def Unmanned(distance, num_traffic_lights, track): # track [[light_location, time_red, time_green], [], ...]
    T = 0 # total time
    prev_light_location = 0
    for i in track:
        if i[0] > distance:
            continue
        else:
            curr_light_location = i[0]
            time_red = i[1]
            time_green = i[2]
            T += curr_light_location - prev_light_location 
            if (T % (time_red + time_green)) <= time_red: # В случае остановки
                T += time_red - (T % (time_red + time_green))
            prev_light_location = curr_light_location
    T += distance - prev_light_location 
    return T
