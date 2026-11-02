def simulate_guard_patrol(map_input):
    # Define movement directions and right turn mappings
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    right_turn = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    position = None
    direction = None
    visited = set()

    # Identify the guard's starting position and direction
    for r, row in enumerate(map_input):
        for c, char in enumerate(row):
            if char in directions:
                position = (r, c)
                direction = char
                visited.add(position)
                break
        if position:
            break

    # Ensure position and direction are found
    if position is None or direction is None:
        return 0

    rows = len(map_input)
    cols = len(map_input[0])

    while 0 <= position[0] < rows and 0 <= position[1] < cols:
        # Calculate the next position
        dr, dc = directions[direction]
        next_position = (position[0] + dr, position[1] + dc)

        if (0 <= next_position[0] < rows and 0 <= next_position[1] < cols and
                map_input[next_position[0]][next_position[1]] != '#'):
            # Move forward
            position = next_position
            visited.add(position)
        else:
            # Turn right and update direction
            direction = right_turn[direction]

    return len(visited)


with open ("input_4.txt", "r", encoding="utf-8") as file:
    data = [line.strip() for line in file]
distinct_positions = simulate_guard_patrol(data)
print(f"The guard will visit {distinct_positions} distinct positions.")
