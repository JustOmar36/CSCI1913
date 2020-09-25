"""Omar Masri/Masri013"""
from math import sqrt
from image_utils import *

def modified_image(k_means_tuple):
    """
    Takes in our tuple that contains our assignments list and means list after going through our k_means function.
    creates a new image list with the width of our assignments list.
    appends to our new image list with values of our means list
    returns a new image.
    """
    new_image_list = []
    width, height = get_width_height(k_means_tuple[0])
    for x in range(width):
        new_image_list.append([])
        for y in range(height):
            new_image_list[x].append(k_means_tuple[1][k_means_tuple[0][x][y]])
    
    return new_image_list


def k_means(image, k):
    """
    Takes in an image and amount of clusters.
    creates a assigments list with our assignments function.
    Tests if our assignments list is equal to the previous version of itself and if so its returns the list.
    return a tuple of our assignments list and our means list
    """
    old_assignments = []
    new_assignments = assignments(initial_mean(k), image, k)
    while new_assignments != old_assignments:
        means = update_means(new_assignments, image, k)
        old_assignments = new_assignments
        new_assignments = assignments(means, image, k)
          
    return (new_assignments, means)#If the old list == new list we leave and return our new list

def assignments(means_list, image, k):
    """
    Takes in our means list, our image, and number of clusters.
    creates an empty list with the width of our image and fills it up with ones. This is to get the size of the image.
    we then use our distance function to test the distance between our colors and random colors.
    We append the distances to a new list
    using our min funtion we find our minimum value, then using our .index() function we are able to find the smallest index.
    We assign that index to our assignments list.
    return our assingment's list
    """
    assignment_list = [] #Empty list to populate with each pixel's cluster
    width, height = get_width_height(image)
    for x in range(width):
        assignment_list.append([])#Append the width with empty lists
        for y in range(height):
            assignment_list[x].append(1)#Append the height with "1" to get the size of the list.
    for y in range(height):
        for x in range(width):
            pixel = image[x][y]
            dist_list = []
            for i in range(len(means_list)):
                pixel2 = means_list[i]
                dist = distance(pixel, pixel2)
                dist_list.append(dist)

            minimum = min(dist_list)
            min_index = dist_list.index(minimum)
            assignment_list[x][y] = min_index
    return assignment_list


def update_means(assignment_list, image, k):
    """
    Our function takes in our assignment_list, image, and clusters.
    We iterate our loop depending on the number of clusters we have.
    We then get our width and height of image and check if the index equals to cluster.
    if true we increment a counter and find the sum each r, g , b value we iterated over.
    if our counter found an index but our count is 0 we append a tuple of zeroes, else we find the average of each value and append it to our means list
    return means list
    """
    new_means = []
    for i in range(k):
        count = 0
        r_sum = 0
        g_sum = 0
        b_sum = 0
        width, height = get_width_height(image)
        for x in range(width):
            for y in range(height):
                if assignment_list[x][y] == i:
                    count+= 1
                    r_sum+= image[x][y][0]
                    g_sum+= image[x][y][1]
                    b_sum+= image[x][y][2]
        if count == 0:
            new_means.append((0,0,0))
        else:
            new_means.append((r_sum//count, g_sum//count, b_sum//count))
    return new_means

def initial_mean(k):
    """
    Takes in number of clusters
    using our given random_color function we initalize a tuple full of random r, g, b values and append to our initial means list
    return initial means list
    """
    means_list = []
    for i in range(k):
        new_tuple = random_color()
        means_list.append(new_tuple)
    return means_list

def distance(pixel1, pixel2): #finds distance between our pixels and our mean pixel
    """
    Takes in 2 sets of colors/pixels
    finds distance between them
    returns distance
    """
    distance = sqrt(((pixel1[0]-pixel2[0])**2) + ((pixel1[1] - pixel2[1])**2) + ((pixel1[2] - pixel2[2])**2))
    return distance

