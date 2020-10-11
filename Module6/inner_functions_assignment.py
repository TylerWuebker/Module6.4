def measurements(a_list):
    def area(a_list):
      area_of = a_list[0] * a_list[1]
    def perimeter(a_list):
      perimeter_of = 2*(a_list[0] + a_list[1])
    area_of = area(a_list)
    perimeter_of = perimeter(a_list)
    outer_string = "Perimeter = " + perimeter_of + " Area = " + area_of
    return outer_string
if __name__ == '__main__':
    '''Length, Width, Height'''
    a_list = {14, 10, 6}
    outer_string = measurements(a_list)
    print(outer_string)
