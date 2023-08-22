
normal_usage = {    
    30 : {"usage per km": 0.14,"time" : 0,"final usage" : 0},
    50 : {"usage per km": 0.145,"time" : 0,"final usage" : 0},
    70 :{"usage per km": 0.15,"time" : 0,"final usage" : 0},
    90 : {"usage per km": 0.17,"time" : 0,"final usage" : 0},
    110 : {"usage per km": 0.195,"time" : 0,"final usage" : 0},
    130 : {"usage per km": 0.23,"time" : 0,"final usage" : 0}
}
list_of_speeds = [30,50,70,90,110,130]

def calculate_driving_times_for_each_speed(distance,list_of_speeds,normal_usage):
    for speed in list_of_speeds:
        hours = distance / speed
        normal_usage[speed]["time"] = hours
    

def calculate_multiplier_lower_temps(temperature):
    extra_usage = 1  
    if temperature < 10:
        extra_usage_multiplyer = abs(10 - temperature)
        extra_usage += (extra_usage_multiplyer * 0.1)
    return extra_usage

        
def optimal_speed(distance,temperature,list_of_speeds,normal_usage):
    
    calculate_driving_times_for_each_speed(distance,list_of_speeds,normal_usage)
    multiplier = calculate_multiplier_lower_temps(temperature)
    for speed in list_of_speeds:
        normal_usage[speed]["final usage"] = (normal_usage[speed]["usage per km"] * distance) + (normal_usage[speed]["time"] * multiplier)
    
    #flitrate under 0 and over 28 usage
    filtered_dict = {key: value for key, value in normal_usage.items() if 0 <= value["final usage"] <= 28}
    if not filtered_dict:
        return None
    
    if filtered_dict != None:
        min_key = min(filtered_dict, key=lambda key: filtered_dict[key]["final usage"])
    
    return min_key, filtered_dict[min_key]["final usage"]


if __name__ == "__main__":
    distance_to_go = 10
    temp = 20
    optimal_car_speed, usage = (optimal_speed(distance_to_go,temp,list_of_speeds,normal_usage))
    if optimal_car_speed != None:
        print(f"With a temperature of {temp} and a driving distance of {distance_to_go} the optimal speed would be {optimal_car_speed}")
        print(f"That trip would use about {usage:.2f} kWh")
    else:
        print("Distance is to far and/or the temperature is to low to go that distance")

