def findPies(pies, desired_sweetness):
    differences = {abs(sweetness - desired_sweetness): i for i, sweetness in enumerate(pies)}
    sorted_differences = sorted(differences.keys())
    result = []
    i = 0
    while sum(result) != desired_sweetness:
        curr_diff = sorted_differences[i]
        i += 1
        result.append(differences[curr_diff])
        if sum(result) > desired_sweetness:
            result.pop()
            break
    return result


if __name__ == '__main__':
    pies = [1, 2, 3, 2, 1]
    desired_sweetness = 6
    result = findPies(pies, desired_sweetness)
    print(f"Pies to consume: {result}")  # Pies to consume: [0, 1, 2]

    pies = [8, 4, 3, 2, 6, 5]
    desired_sweetness = 6
    result = findPies(pies, desired_sweetness)
    print(f"Pies to consume: {result}")  # Pies to consume: [1, 3]
