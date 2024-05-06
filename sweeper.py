#This program takes te grid and retrn a new grid with the numbers in the place of a "-".

"""Doc String
Define the pattern grid function
Create variable names for each avriable
"""
def pattern_grid (grid):
    rows= len(grid)
    columns= len(grid[0])
    grid_count= [[0 for _ in range (columns)]  for _ in range(rows)]
    
    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == "-":
                count = 0
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < rows and 0 <= nj < columns and grid[ni][nj] == "#":
                            count+=1
                grid_count[i][j] = count
    return grid_count
    
grid_1= [["-", "#", "-"], 
         ["-", "-", "#"], 
         ["#", "-", "-"], 
         ["-", "#", "-"],
           ["-", "#", "#"]]

print(f"This is the new grid:{pattern_grid(grid_1)}")
print()
print("---------New Grid---------")
grid_2 = pattern_grid(grid_1)
for rows in grid_2:
    #for column in rows:
        print(rows, end= "")
        print()

