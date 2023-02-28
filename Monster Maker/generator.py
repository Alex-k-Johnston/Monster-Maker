from PIL import Image, ImageOps
import numpy as np
import random, math, colorsys, copy
    
def generate(arr, width, height):
    map = base(arr, width, height)
    map = frame(map, width, height)
    map = color(map)
    #comment out this line if template doesn't need to be mirrored
    map, width, height = mirror(map)

    return map, width, height

def base(arr, width, height):
    # 0: no pixel, 1: body pixel, 2: core pixel, 3: frame pixel
    #if map at index is a 1, 50% chance to draw pixel
    #if map at index is a 2, 50% for regular pixel, 50% for core pixel 
    for h_index in range(height):
        for w_index in range(width):
            if arr[h_index][w_index] == 1:
                arr[h_index][w_index] = random.randint(0, 1)
            elif arr[h_index][w_index] == 2:
                arr[h_index][w_index] = random.randint(1, 2)
            #introduce a 3?
    
    return arr

def frame(map, width, height):
    #if 1 is adjacent to a 0, make it a 3 (skin) instead
    for h_index in range(height):
        for w_index in range(width):
            if map[h_index][w_index] == 0:
                if map[h_index][w_index - 1] == 0:
                    map[h_index][w_index] = 3
                #elif map[h_index][w_index] == 
                
            #elif map[h_index][w_index] == 0 and map[h_index][w_index - 1 ] == 1:
             #   map[h_index][w_index] = 3

    return map 
    

def color(map):
   
   #interior all one randomly generated color/ gradient? 
   #
   LUT=np.zeros(256, dtype=np.uint8)
   LUT[0] = 1
   LUT[1] = 0
   LUT[2] = 0
   LUT[3] = 0
   map = LUT[map]
   
   return map


def mirror(map):
    np_map = np.array(map)
    np_mirror = np.flip(np_map, axis = 1)
    map = np.concatenate((np_map, np_mirror), axis = 1)
    height, width = np.shape(map)

    return map, width, height

