def cube_volume(cube_side):
    
    cube_volume = int(cube_side)**3
    cube_surface_area = int(cube_side) * 6
    
    print(f'The volume of a cube with side {cube_side} is {cube_volume}')
    print(f'The surface area of a cube with side {cube_side} is {cube_surface_area}')

cube_volume(cube_side = 2)