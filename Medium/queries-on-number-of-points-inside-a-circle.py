# Solution author: Alexadre de Rosso Crestani
# Problem picked from Leet Code website: https://leetcode.com/

# You are given an array points where points[i] = [xi, yi] is the coordinates of the i-th point on a 2D plane.
# Multiple points can have the same coordinates.
# You are also given an array queries where queries[j] = [xj, yj, rj] describes a circle centered at (xj, yj) with a radius of rj.
# For each query queries[j], compute the number of points inside the j-th circle.
# Points on the border of the circle are considered inside.
# Return an array answer, where answer[j] is the answer to the j-th query.

# Exemple 1:
# Input:  points = [[1,3],[3,3],[5,3],[2,2]],
#         queries = [[2,3,1],[4,3,1],[1,1,2]]
# Output: [3,2,2]

# Exemple 2:
# Input:  points = [[1,1],[2,2],[3,3],[4,4],[5,5]],
#         queries = [[1,2,2],[2,2,2],[4,3,2],[4,3,3]]
# Output: [2,3,2,4]

# Complexity O(n x m)
# n = len(points)
# m = len(queries)

# Solution general idea:
# for each circle center, calculate all distances from circle center to a point from points
# if distance is grater than radius, then the point is outside the circle
#    distance from x0,y0 to x1,y1 = sqrt((x0-x1)^2 + (y0-y1)^2)
# otherwise the point is inside, in this case, keep it in an array

def foo(points: list, queries: list) -> list:
    
    # empty list to return the inside points
    output = []

    # for each circle, do
    for circle in queries:
        
        # varible to count how many points are inside
        inside = 0

        # for all points calculate the distance from circle to point
        for point in points:

            # calculate the distance
            distance = ((circle[0] - point[0])**2 + (circle[1] - point[1])**2)**(1/2)

            # if distance is grater than radius, then the point is outside the circle
            # otherwise the point is inside, in this case, keep it in an array
            if circle[2] >= distance:
                inside += 1
        
        # keeps the number of inside points
        output.append(inside)
    
    return output






# tests:
points = [[1,3],[3,3],[5,3],[2,2]]
queries = [[2,3,1],[4,3,1],[1,1,2]]

print(foo(points, queries))