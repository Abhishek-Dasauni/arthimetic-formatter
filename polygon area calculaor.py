def calculate_polygon_area(vertices):
    n = len(vertices)
    if n < 3:
        return "A polygon must have at least three vertices."

    
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += (vertices[i][0] * vertices[j][1]) - (vertices[j][0] * vertices[i][1])

    area = abs(area) / 2
    return area

# Example usage
vertices = [(0, 0), (0, 4), (3, 0)]
polygon_area = calculate_polygon_area(vertices)
print(f"The area of the polygon is: {polygon_area}")
