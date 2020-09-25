"""
Omar Masri/Masri013
Run the k-means algorithm asking for input and output.
"""

from k_means import *
from image_utils import *

file_name_input = input('Please enter the ppm file you wish to convert\n>')
k_input = int(input('Now please enter the number of clusters you wish to convert to\n>'))
file_output_name = input('Now enter the name of the new file the picture will be converted to\n>')
print("Converting...")


user_file = read_ppm(file_name_input)
new_tuple = k_means(user_file, k_input)
image = modified_image(new_tuple)
user_output_file = save_ppm(file_output_name, image)
print("Your file has compiled!")
