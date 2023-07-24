#linear interpolation code
time1 = float(input("Enter time 1:"))
x1 = float(input("Enter the x position of the object at time 1:"))
y1 = float(input("Enter the y position of the object at time 1:"))
z1 = float(input("Enter the z position of the object at time 1:"))
time2 = float(input("Enter time 2:"))
x2 = float(input("Enter the x position of the object at time 2:"))
y2 = float(input("Enter the y position of the object at time 2:"))
z2 = float(input("Enter the z position of the object at time 2:"))
# finds at what intervals should the code be found at
time_points = (time2 - time1) * .25
time_input = time1
# makes the code output at all the positions
while time_input <= time2:
    x3 = ((time_input - time1) * (x2 - x1) / (time2 - time1)) + x1
    z3 = ((time_input - time1) * (z2 - z1) / (time2 - time1)) + z1
    y3 = ((time_input - time1) * (y2 - y1) / (time2 - time1)) + y1
    print("at time", '{:.1f}'.format(time_input), "seconds the object is at (", '{:.2f}'.format(x3), ",",
          '{:.2f}'.format(y3), ",", '{:.2f}'.format(z3), ")")
    # makes while loop not run forever
    time_input += time_points
