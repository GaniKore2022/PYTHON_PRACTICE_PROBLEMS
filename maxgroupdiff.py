def max_strength_difference(arr, m):
    arr.sort(reverse=True)

    def calculate_difference(group1, group2):
        return abs(sum(group1) - sum(group2))

    group1 = []
    group2 = []
    max_difference = float('-inf')

    for strength in arr:
        if strength >= 0 and len(group1) < m:
            group1.append(strength)
        else:
            group2.append(strength)

        if len(group1) <= m:
            max_difference = max(max_difference, calculate_difference(group1, group2))

    group1 = []
    group2 = []

    for strength in arr:
        if strength < 0 and len(group1) < m:
            group1.append(strength)
        else:
            group2.append(strength)

        if len(group1) <= m:
            max_difference = max(max_difference, calculate_difference(group1, group2))

    return max_difference

# Example usage
arr = list(map(int,input().split()))
m = int(input())
result = max_strength_difference(arr, m)
print("Maximum possible difference:", result)
