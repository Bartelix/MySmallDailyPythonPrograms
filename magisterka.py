import numpy as np
import math, datetime, re


def distance_between_points_on_a_circle(diameter, offset):
    return 2 * math.sqrt(diameter ** 2 / 4 - offset)


def optimization_b(thickness, diameter, multiplier, horizontal):
    #num_center = 1
    #num_not_center = 1
    results = { 'name_code': ( 'cell_diameter', 'thickness', 'number_of_layer', 'height' ) }
    for val_thickness in thickness:
        for val_diameter in diameter:
            for val_multiplier in multiplier:
                for val_horizontal in horizontal:
                    condition_height = 49.5 <= val_thickness + val_diameter * val_multiplier <= 50.1
                    offset = 0
                    condition_horizontal_center = False
                    for i in range(3):
                        if distance_between_points_on_a_circle(36, offset) - 0.5 <= val_thickness + val_diameter * val_horizontal <= distance_between_points_on_a_circle(36, offset):
                            condition_horizontal_center = True
                        else:
                            condition_horizontal_center = False
                        offset += val_diameter
                    if condition_height and condition_horizontal_center:
                        #with open('cell_b.txt', 'a+') as f:
                            #f.write(f'Start from center\ncombination {num_center}\nthickness = {val_thickness}\ndiameter = {val_diameter}\nrows = {val_multiplier}\nhorizontal = {val_horizontal}\n\n')
                        #print(f'Start from center\ncombination {num_center}\nthickness = {val_thickness}\ndiameter = {val_diameter}\nrows = {val_multiplier}\nhorizontal = {val_horizontal}\n')
                        results[ f'bfc__{val_diameter}__{val_thickness * 10}' ] = ( val_diameter, val_thickness, val_multiplier, val_thickness + val_diameter * val_multiplier )
                        #num_center += 1
                    condition_horizontal_oblique = distance_between_points_on_a_circle(36, offset + val_diameter / 2) - 1<= val_thickness + val_diameter * val_horizontal <= distance_between_points_on_a_circle(36, offset + val_diameter / 2)
                    if condition_height and condition_horizontal_oblique:
                        #with open('cell_b.txt', 'a') as f:
                            #f.write(f'Start next to center\ncombination {num_not_center}\nthickness = {val_thickness}\ndiameter = {val_diameter}\nrows = {val_multiplier}\nhorizontal = {val_horizontal}\n\n')
                        #print(f'Start next to center\ncombination {num_not_center}\nthickness = {val_thickness}\ndiameter = {val_diameter}\nrows = {val_multiplier}\nhorizontal = {val_horizontal}\n')
                        results[ f'bntc__{val_diameter}__{val_thickness * 10}' ] = ( val_diameter, val_thickness, val_multiplier, val_thickness + val_diameter * val_multiplier )
                        #num_not_center += 1
    return results

def optimization_cf(thickness, diameter, multiplier, horizontal):
    #num_center = 1
    #num_not_center = 1
    results = { 'name_code': ( 'cell_diameter', 'thickness', 'number_of_layer', 'height' ) }
    for val_thickness in thickness:
        for val_diameter in diameter:
            for val_multiplier in multiplier:
                for val_horizontal in horizontal:
                    condition_height = 50 <= val_diameter * val_multiplier <= 50.5
                    offset = 0
                    condition_horizontal_center = False
                    for i in range(3):
                        if distance_between_points_on_a_circle(36, offset) - 1 <= val_diameter / 2 ** 0.5 * val_horizontal + val_thickness <= distance_between_points_on_a_circle(36, offset):
                            condition_horizontal_center = True
                        else:
                            condition_horizontal_center = False
                        offset += val_diameter
                    if condition_height and condition_horizontal_center:
                        #with open('cell_cf.txt', 'a+') as f:
                            #f.write(f'Start from center\ncombination {num_center}\nthickness = {val_thickness}\ndiameter = {val_diameter}\nrows = {val_multiplier}\nhorizontal = {val_horizontal}\n\n')
                        #print(f'Start from center\ncombination {num_center}\nthickness = {val_thickness}\ndiameter = {val_diameter}\nrows = {val_multiplier}\nhorizontal = {val_horizontal}\n')
                        results[ f'cffc__{val_diameter}__{val_thickness * 10}' ] = ( val_diameter, val_thickness, val_multiplier, val_diameter * val_multiplier )
                        #num_center += 1
                    condition_horizontal_oblique = distance_between_points_on_a_circle(36, offset + val_diameter / 2) - 1 <= val_diameter / 2 ** 0.5 * val_horizontal + val_thickness <= distance_between_points_on_a_circle(36, offset + val_diameter / 2)
                    if condition_height and condition_horizontal_oblique:
                        #with open('cell_cf.txt', 'a') as f:
                            #f.write(f'Start next to center\ncombination {num_not_center}\nthickness = {val_thickness}\ndiameter = {val_diameter}\nrows = {val_multiplier}\nhorizontal = {val_horizontal}\n\n')
                        #print(f'Start next to center\ncombination {num_not_center}\nthickness = {val_thickness}\ndiameter = {val_diameter}\nrows = {val_multiplier}\nhorizontal = {val_horizontal}\n')
                        results[ f'cfntc__{val_diameter}__{val_thickness * 10}' ] = ( val_diameter, val_thickness, val_multiplier, val_diameter * val_multiplier )
                        #num_not_center += 1
    return results


def cell_b():
    optd_b = optimization_b(thickness, diameter, rows, horizontal)
    with open('cell_b.txt', 'a+') as f:
        for key, value in optd_b.items():
            f.write(f'{key}: {value}')
            f.write('\n')
        f.write(str(datetime.datetime.now()))
        f.write('\n')


def cell_cf():
    optd_cf = optimization_cf(thickness, diameter, rows, horizontal)
    with open('cell_cf.txt', 'a+') as f:
        for key, value in optd_cf.items():
            f.write(f'{key}: {value}')
            f.write('\n')
        f.write(str(datetime.datetime.now()))
        f.write('\n')


thickness = np.linspace(0.7, 1.5, int(0.8/0.1+1))
diameter = np.linspace(3, 8, int(5/0.1+1))
rows = np.linspace(4, 20, int(16/1+1))
horizontal = np.linspace(4, 20, int(16/1+1))


#cell_b()
cell_cf()