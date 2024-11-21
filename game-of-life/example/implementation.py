def evolve(grid, wrapping=False, custom_rules=None):
    birth = custom_rules.get("birth", [3]) if custom_rules else [3]
    survival = custom_rules.get("survival", [2, 3]) if custom_rules else [2, 3]
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    def count_neighbors(r, c):
        count = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if wrapping:
                    nr %= rows
                    nc %= cols
                elif not (0 <= nr < rows and 0 <= nc < cols):
                    continue
                count += grid[nr][nc]
        return count

    new_grid = [[0 for _ in range(cols)] for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            neighbors = count_neighbors(r, c)
            if grid[r][c] == 1 and neighbors in survival:
                new_grid[r][c] = 1
            elif grid[r][c] == 0 and neighbors in birth:
                new_grid[r][c] = 1
            # Else, leave cell as dead.
    return new_grid
