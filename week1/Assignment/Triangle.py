def can_form_triangle(side_a,side_b,side_c):
    sides = [side_a, side_b, side_c
]
    longest_side = max(sides)
    sum_of_other_sides = sum(sides) - longest_side

    if sum_of_other_sides > longest_side:
        print("It can form a triangle.")
    else:
        print("It cannot form a triangle.")
        
        
side_a = float(input('Enter length of side a: '))
side_b = float(input('Enter length of side b: '))
side_c = float(input('Enter length of side c: '))
        
can_form_triangle(side_a,side_b,side_c)
