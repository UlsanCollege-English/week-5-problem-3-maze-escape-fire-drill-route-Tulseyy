
# src/maze.py

def find_path(grid, start, end):
    """
    Return a list of (r,c) from start to end inclusive, or None if no path.
    grid contains 0 (open) and 1 (wall). Moves: up/down/left/right.
    """
    rows, cols = len(grid), len(grid[0])
    visited = set()

    def backtrack(r, c):
        # If out of bounds or a wall or already visited, stop
        if not (0 <= r < rows and 0 <= c < cols):
            return None
        if grid[r][c] == 1 or (r, c) in visited:
            return None

        # Mark current cell as visited
        visited.add((r, c))

        # If we've reached the end, return this path
        if (r, c) == end:
            return [(r, c)]

        # Explore neighbors: up, down, left, right
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            path = backtrack(r + dr, c + dc)
            if path:
                return [(r, c)] + path

        # Backtrack (no valid path from here)
        return None

    return backtrack(*start)


# Example usage / test
if __name__ == "__main__":
    grid = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0],
    ]
    start = (0, 0)
    end = (3, 4)

    path = find_path(grid, start, end)
    print("Path found:" if path else "No path found")
    print(path)

