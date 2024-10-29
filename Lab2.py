print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def display_main_menu():
    print("Enter temperatures separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    number = input("Enter temperatures: ")
    number_split = number.split(",")
    number_floats = [float(num) for num in number_split]
    return number_floats

def sort_temperature(temperatures):
    print("sort_temperature")
    return sorted(temperatures)

def calc_median_temperature(temperatures):
    print("calc_median_temperature")
    
    # Sort temperatures before calculating the median
    sorted_temperatures = sort_temperature(temperatures)
    n = len(sorted_temperatures)
    
    if n == 0:
        return 0.0
    
    # If odd, return the middle element
    if n % 2 == 1:
        median = sorted_temperatures[n // 2]
    else:
        # If even, return the average of the two middle elements
        mid1 = sorted_temperatures[n // 2 - 1]
        mid2 = sorted_temperatures[n // 2]
        median = (mid1 + mid2) / 2
    
    return median

def calc_average_temperature(temperatures):
    print("calc_average_temperature")
    if len(temperatures) == 0:
        return 0.0
    return sum(temperatures) / len(temperatures)

def calc_min_max_temperature(temperatures):
    print("calc_min_max_temperature")
    if len(temperatures) == 0:
        return [0.0, 0.0]
    min_temp = min(temperatures)
    max_temp = max(temperatures)
    return [min_temp, max_temp]

# Example usage:
display_main_menu()
temperatures = get_user_input()

average = calc_average_temperature(temperatures)
min_max = calc_min_max_temperature(temperatures)
sorted_temps = sort_temperature(temperatures)
median = calc_median_temperature(temperatures)

print(f"Average temperature: {average}")
print(f"Min temperature: {min_max[0]}, Max temperature: {min_max[1]}")
print(f"Sorted temperatures: {sorted_temps}")
print(f"Median temperature: {median}")




