def auto_pilot_next_step(titanic_row, titanic_col, ocean_size):
    iceberg_positions = [
        [0, 3], [1, 3], [2, 3], [3, 3], [4, 3], [5, 3], [6, 3], [7, 3], [9, 3]
    ]

    # Get the current position of the Titanic
    row = titanic_row
    col = titanic_col

    # Check if the west is clear
    safe_path = True
    for i in range(col - 1, -1, -1):  # Iterate from the current column to the left boundary of the grid
        if [row, i] in iceberg_positions:  # Check if there is an iceberg in this position
            safe_path = False  # If there is an iceberg, it's not safe to go west
            break
    if safe_path:
        return 'WEST'

    # Find a safe path to the south
    for i in range(row + 1, ocean_size):  # Iterate from the current row to the bottom boundary of the grid
        if [i, col] not in iceberg_positions:  # Check if there is no iceberg in this position
            return 'SOUTH'

    # Find a safe path to the north
    for i in range(row - 1, -1, -1):  # Iterate from the current row to the top boundary of the grid
        if [i, col] not in iceberg_positions:  # Check if there is no iceberg in this position
            return 'NORTH'

    return 'WEST'
