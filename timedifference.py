def get_minutes(time_str):
    # Convert time string to minutes
    hours, minutes = map(int, time_str.split(':'))
    return hours * 60 + minutes


def get_time_difference(time1, time2):
    # Calculate the time difference in minutes
    return (time2 - time1 + 24 * 60) % (24 * 60)


def find_minimum_time_difference(times):
    # Convert times to minutes
    minutes = [get_minutes(time) for time in times]

    # Sort the list of times in ascending order
    minutes.sort()

    # Initialize the minimum difference with a large value
    min_diff = float('inf')

    # Calculate the time difference between adjacent times
    for i in range(len(minutes) - 1):
        diff = get_time_difference(minutes[i], minutes[i + 1])
        min_diff = min(min_diff, diff)

    # Consider the circular nature of time
    circular_diff = get_time_difference(minutes[-1], minutes[0])
    min_diff = min(min_diff, circular_diff)

    return min_diff


# Example usage
times_list = list(map(str,input().split()))

result = find_minimum_time_difference(times_list)
print(f"Minimum time difference: {result} minutes")
