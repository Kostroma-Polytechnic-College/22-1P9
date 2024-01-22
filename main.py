from logic.point3d import Point3D
from logic.line3d import Line3D


p1 = Point3D(0,1,2)
p2 = Point3D(3,4,5)
line = Line3D(p1, p2)

















# line.start_point = Point3D(6,7,8)
# line.end_point = Point3D(9,0,1)
# line.set_start_coordinates(2,3,4)
# line.set_end_coordinates(5,6,7)
# print(line.length())
# try:
#     line.start_point = Point3D(0,0,0)
#     line.end_point = Point3D(0,0,0)
# except ValueError as ex:
#     print(ex)

# for x1 in (0,1):
#     for y1 in (0,1):
#         for x2 in (0,1):
#             for y2 in (0,1):
#                 print(f'x1={x1}, y1={y1}, x2={x2}, y2={y2}')
#                 p1 = Point(x1, y1)
#                 p2 = Point(x2, y2)
#                 try:
#                     line = Line(p1, p2)
#                     line.start_point = p2
#                     print(line.length())
#                 except ValueError as ex:
#                     print(f'ValueError={ex}')