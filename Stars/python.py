# PART1

arr = [4, 6, 1, 3, 5, 7, 25]
def draw_stars(arr):
    for i in arr:
        print i * " *"
draw_stars(arr)


# PART2 

arr = [4, 'william', 1, 'jillllllllllll', 5, 'christopher', 25]
def draw_starswithstring(arr):
    for i in arr:
        if (type(i) == int):
            print i * " *"
        elif (type(i) == str):
            for letter in i:
                if (letter == 'i'):
                    print i[:1] * len(i)    
draw_starswithstring(arr)