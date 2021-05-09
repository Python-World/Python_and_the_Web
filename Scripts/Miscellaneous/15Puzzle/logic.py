def is_solvable(puzzle):
    parity = 0
    grid_width = int(len(puzzle) ** 0.5)
    row = 0  # the current row we are on
    blank_row = 0  # the row with the blank tile
    for i, num in enumerate(puzzle):
        if i % grid_width == 0:  # advance to the next row
            row += 1
        if num == 0:  # the blank tile
            blank_row = row
            continue
        for j in range(i + 1, len(puzzle)):
            if puzzle[i] > puzzle[j] and puzzle[j] != 0:
                parity += 1

    if grid_width % 2 == 0:  # grid is even
        if blank_row % 2 == 0:  # blank on odd row; counting from bottom
            return parity % 2 == 0
        # blank on even row; counting from bottom
        return parity % 2 != 0
    # odd grid
    return parity % 2 == 0


def is_solved(puzzle):
    for i, e in enumerate(puzzle[:-1], 1):
        if i != e:
            return False
    return True


def convert_time(seconds):
    """convert seconds into natural time. i.e, 122 seconds => 2 minutes 32 seconds
    note: does not go beyond minutes
    """
    seconds = round(seconds)
    minutes, seconds = divmod(seconds, 60)
    x, y = "minute", "second"
    if minutes > 1:
        x += "s"
    if seconds > 1:
        y += "s"
    if minutes:
        return f"{minutes} {x} {seconds} {y}"
    return f"{seconds} {y}"
