#Exercise 6.9 Compute the area of a triangle
#Andrew Turner

# area = .5 * (x2*y3 - x3*y2 -x1*y3 + x3*y1 + x1*y2 - x2*y1)

def area(v):
    area = 0.5 * abs(v[2][0]*v[3][1]-v[3][0]*v[2][1]-
                     v[1][0]*v[3][1]+v[3][0]*v[1][1]+
                     v[1][0]*v[2][1]-v[2][0]*v[1][1])
    return area

v1 = (0,0)
v2 = (1,0)
v3 = (0,2)

vertices = {1: v1, 2: v2, 3: v3}
area_triangle = area(vertices)

print 'Area of triangle is %.2f unit(s).' % area_triangle
