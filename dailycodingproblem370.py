# The “active time” of a courier is the time between the pickup and dropoff of a delivery. Given a set of data formatted like the following:

# (delivery id, timestamp, pickup/dropoff)
# Calculate the total active time in seconds. A courier can pick up multiple orders before dropping them off. The timestamp is in unix epoch seconds.

# For example, if the input is the following:

# (1, 1573280047, 'pickup')
# (1, 1570320725, 'dropoff')
# (2, 1570321092, 'pickup')
# (3, 1570321212, 'pickup')
# (3, 1570322352, 'dropoff')
# (2, 1570323012, 'dropoff')

def calculate_time(arr):

    time_map = {}
    total_time = 0

    i = 0
    while (i < len(arr)):

        temp = arr[i]
        package = temp[0]
        time = temp[1]
        type = temp[2]
        if (package not in time_map):

            time_map[package] = time

        else:

            total_time = total_time + time_map[package]
            del time_map[package]

    return total_time