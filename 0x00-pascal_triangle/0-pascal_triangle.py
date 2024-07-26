#!/usr/bin/python3

def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    Args:
        n (int): The number of rows of Pascal's Triangle to generate.

    Returns:
        list: A list of lists representing Pascal's Triangle.
    """
    if n <= 0:  # If n is less than or equal to 0, return an empty list.
        return []
    Triangle = []  # Initialize an empty list to hold the rows of Pascal's Triangle.
    for i in range(n):  # Iterate over the range from 0 to n-1.
        if i == 0:
            Triangle.append([1])  # The first row is always [1].
        elif i == 1:
            Triangle.append([1, 1])  # The second row is always [1, 1].
        else:
            row = [1]  # Start each new row with 1.
            for x in range(1, len(Triangle[i - 1])):  # Iterate over the indices of the previous row.
                # Append the sum of the two elements above the current position.
                row.append(Triangle[i - 1][x] + Triangle[i - 1][x - 1])
            row.append(1)  # End each row with 1.
            Triangle.append(row.copy())  # Append the complete row to the Triangle.
            row.clear()  # Clear the row list to prepare for the next iteration.

    return Triangle  # Return the complete Pascal's Triangle.

