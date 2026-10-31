def cuboid_calculation(a, b, c): 
    cuboid_volume = a * b * c
    cuboid_sufrace_area = ((a * b) * 2) + ((a *c) * 2) + ((b*c) * 2)
    print(f"For cuboid with sides {a} and {b} and {c} the volume is {cuboid_volume} and the surface area is {cuboid_sufrace_area}")
cuboid_calculation(a = 2, b = 3, c = 4)