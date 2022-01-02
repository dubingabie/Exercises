
#################################################################
# FILE : cartoonify.py
# WRITER : Gaberiel Dubin , dubingabie , 209386481
# EXERCISE : intro2cse ex4 2021
# DESCRIPTION:
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES: ...
#################################################################

import ex5_helper as helper
import copy
import math
import sys


#######################################################################################################################


# question 1 - (i)


def separate_pixel_row(image: list, row: int, channel: int) -> list:
    """ a function that separates a pixel row from a color channel
        :param : a three dimensional list containing an image
                 an int number which states the channel which the row is in
                 an int number which states the row that is to be separated
        :returns : a list containing the mentioned pixel row"""
    pixel_row_list = list()
    for column in range(len(image[row])):
        pixel_row_list.append(image[row][column][channel])
    return pixel_row_list


def separate_channel(image: list, channel: int) -> list:
    """ a function that separates a single channel from an image
        :param : a three dimensional list containing an image
                 an int number which states the channel that is to be separated
        :returns : a two dimensional list containing the channel"""
    single_channel = list()
    for row in range(len(image)):
        single_channel.append(separate_pixel_row(image, row, channel))
    return single_channel


def separate_channels(image: list) -> list:
    """ a function that separates the three color channels of an image
        :param : a three dimensional list containing the entire images
        :returns : a three dimensional list containing three lists , one representing
                   each color channel"""
    channel_list = list()
    for i in range(len(image[0][0])):
        channel_list.append(separate_channel(image, i))
    return channel_list


# question 1 - (ii)


def combine_pixel_channels(channels: list, row: int, column: int) -> list:
    """a function that combines the color channels for a single pixel and returns the combined
       colors as a list
       :param : a list containing the separated color channels
                an int containing the row index of the pixel
                an int containing the column index of the pixel
       :returns : a list all of the color channels of one pixel"""
    pixel = list()
    for channel in range(len(channels)):
        pixel.append(channels[channel][row][column])
    return pixel


def combine_pixel_row(channels: list, row: int) -> list:
    """ a function that combines pixels into a row and returns it as a two dimensional list
        :param : a list containing the separated color channels
                 an int containing the column index of the pixel
        :returns : a two dimensional list containing a row of pixels with combined color channels"""
    pixel_row = list()
    for column in range(len(channels[0][row])):
        pixel_row.append(combine_pixel_channels(channels, row, column))
    return pixel_row


def combine_channels(channels: list) -> list:
    """ a function that receives a list of separated color channels of an image
        and returns that image
        :param : a list containing the separaed color channels of an image
        :returns : a list containing the image"""
    image = list()
    for row in range(len(channels[0])):
        image.append(combine_pixel_row(channels, row))
    return image


########################################################################################################################


# question 2


def get_grayscale_value(channels: list, row: int, column: int) -> int:
    """ a function that receives the separated RGB color channels
        and the coordinates of a pixel and returns its grayscale value
        :param : a list containing the separated color channels of an image
                 an int containing the row index of the pixel
                 an int containing the column index of the pixel
        :returns : an int containing the grayscale color value of the pixel"""
    grayscale_value = round((channels[0][row][column] * 0.299) \
                            + (channels[1][row][column] * 0.587) \
                                + (channels[2][row][column] * 0.114))
    return grayscale_value


def get_grayscale_row(channels: list, row: int) -> list:
    """ a function that receives the separated RGB color channels
        and the coordinates of a row and returns it in grayscale color
        :param : a list containing the separated color channels of an image
                 an int containing the row index
        :returns : a list contiang the row in graysacle color"""
    grayscale_row = list()
    for column in range(len(channels[0][row])):
        grayscale_row.append(get_grayscale_value(channels, row, column))
    return grayscale_row


def RGB2grayscale(colored_image: list) -> list:
    """ a function that receives an image and returns a grayscale version of it
        :param : a three dimensional list containing an RGB image
        :returns : a three dimensional list containing the original image in graysacle"""
    channel_list = separate_channels(colored_image)
    grayscale_image = list()
    for row in range(len(colored_image)):
        grayscale_image.append(get_grayscale_row(channel_list,row))
    return grayscale_image


########################################################################################################################


# question 3


def blur_kernel_row(size: int) -> list:
    """ a function that makes a row of a kernel and returns it
        :param : an int containing the size of the kernel
        :return : a list containing the row of the kernel"""
    blur_kernel_row_list = list()
    for column in range(size):
        blur_kernel_row_list.append(1 / (size ** 2))
    return blur_kernel_row_list


def blur_kernel(size: int) -> list:
    """ a function that makes a kernel that fits the size supplied to it
        :param : an int containing the size of the kernel
        :returns : a two dimensional list containing the kernel"""
    blur_kernel_list = list()
    for row in range(size):
        blur_kernel_list.append(blur_kernel_row(size))
    return blur_kernel_list

##########################################################################################################


# question 4


def check_out_of_range(image: list, row_range: int, column_range: int) -> bool:
    """ a function that checks if the indexes are not in the picture
        :param: a list that contains an image
                an int that contains an index of a row in the picture
                an int that contains an index of a column in the picture
        :returns: a bool that contains true if the indexes or in the picture and false if otherwise"""
    return row_range < 0 or row_range >= len(image) or column_range < 0 or column_range >= len(image[0])


def make_sum_kernel(image: list, kernel: list, row: int , column: int) -> list:
    """a function that makes a list the size of the blur kernel and multiplies the appropriate
       pixels of the image and stores it in the kernel
       :param : a list that contains the image
                a list the contains the blur kernel
                an int that contains the row index of the current pixel
                an int that contains the column index of the current pixel
       :return : a list that contains the values of each adjacent pixel with the value in the blur kernel"""
    kernel_center = len(kernel) // 2
    sum_kernel = copy.deepcopy(kernel)
    for kernel_row in range(len(sum_kernel)):
        for kernel_column in range(len(sum_kernel)):
            if check_out_of_range(image, row + kernel_row - kernel_center, column + kernel_column - kernel_center):
                sum_kernel[kernel_row][kernel_column] *= image[row][column]
            else:
                sum_kernel[kernel_row][kernel_column] *= \
                    image[row + kernel_row - kernel_center][column + kernel_column - kernel_center]
    return sum_kernel


def sum_kernel_into_pixel(image: list, kernel: list, row: int, column: int):
    """ a function that sums all of color values of the adjacent pixels multiplied by the
        blur value in the blur kernel and summed into the current pixel
        :param : a list containing an image
                 a list containing the blur kernel
                 an int containing the current row index of the pixel
                 an int containing the current column index of the pixel
         :returns : the color value of the pixel"""
    sum_kernel = make_sum_kernel(image, kernel, row, column)
    pixel_value = 0
    for kernel_row in range(len(sum_kernel)):
        for kernel_column in range(len(sum_kernel)):
            pixel_value += sum_kernel[kernel_row][kernel_column]
    if pixel_value > 255:
        pixel_value = 255
    elif pixel_value < 0:
        pixel_value = 0
    return round(pixel_value)


def apply_kernel(image: list, kernel: list) -> list:
    """ a function that applies a blur kernel on a single channel image and returns a
        blurred version of the picture
        :param : a list containing a single color channel image
                 a list containg a blur kernel
        :returns: a list containing a blurred single channel image"""
    new_image = copy.deepcopy(image)
    for row in range(len(image)):
        for column in range(len(image[0])):
            new_image[row][column] = sum_kernel_into_pixel(image, kernel, row, column)
    return new_image

#######################################################################################################################


# question 5


def get_bilinear_interpolation_operands(image: list, rounded_y: int, rounded_x: int) -> tuple:
    """ a function that returns the appropriate cells for the linear interpolation
        :param: a list containing a single color channel
                an int containg the rounded y coordinates of the pixel whose color vlaue is to be caluclated
                an int containg the rounded x coordinates of the pixel whose color vlaue is to be caluclated
        :return : a tuple containing the value of the appropriate cells in the right order """
    if rounded_y + 1 > len(image) - 1:
        rounded_y = len(image) - 2
    if rounded_x + 1 > len(image[0]) - 1:
        rounded_x = len(image) - 2
    a = image[rounded_y][rounded_x]
    b = image[rounded_y+1][rounded_x]
    c = image[rounded_y][rounded_x+1]
    d = image[rounded_y+1][rounded_x+1]
    return a, b, c, d


def calculate_pixel_color_value(a: int, b: int, c: int, d: int, y_distance: float, x_distance: float) -> float:
    """ a function that calculates the color value of a pixel according to the
        bilinear interpolation formula
        :param : an int containing the value of the a operand
                 an int containing the value of the b operand
                 an int containing the value of the c operand
                 an int containing the value of the d operand
                 a float containing the y distance according to the formula
        :return : a float containing the color value of the pixel
        """
    return (a * (1 - x_distance) * (1 - y_distance))\
                + (b * y_distance * (1 - x_distance)) \
                + (c * x_distance * (1 - y_distance )) \
                + (d * (x_distance * y_distance))


def get_distance(distance: float) -> float:
    """ a function that returns the appropriate axis distance according to the
        bilinear interpolation formula
        :param : a float containing the axis coordinate
        :return : a float containing the correct distance from the axis """
    return 1 if distance >= 1 else distance


def bilinear_interpolation(image: list, y: float, x: float) -> int:
    """ a function that calculates the color value of a pixel according to its location in the
        image and the bilinear interpolation formula
        :param : a list containing a single channel image
                a float containing the y axis distance
                a float containing the x axis distance
        :return : an int containing the color value as a result of a formula """
    rounded_x = int(x)
    rounded_y = int(y)
    y_distance, x_distance = get_distance(y), get_distance(x)
    a, b, c, d = get_bilinear_interpolation_operands(image, rounded_y, rounded_x)
    color_value = calculate_pixel_color_value(a, b, c, d, y_distance, x_distance)
    return round(color_value)

########################################################################################################################


# question 6


def make_new_size_image_row(new_width: int) -> list:
    """ a function that makes an empty list in the new width of an image
        :param : an int containing the length of the list that ist to be created
        :return : an empty list in state length"""
    new_image_row = list()
    for column in range(new_width):
        new_image_row.append([])
    return new_image_row


def make_new_size_image(new_height: int, new_width: int) -> list:
    """a function that makes an empty two dimensional list in the size of the image
       :param : an int containg the height of the list that is to be created
                an int containg the width of the last that is to be created
       :return : an empty list in the stated height and width"""
    new_image = list()
    for row in range(new_height):
        new_image.append(make_new_size_image_row(new_width))
    return new_image


def resize(image: list, new_height: int, new_width: int) -> list:
    """a function that resizes an image according to the new width and height
       :param : a list containg a single color channel image
                an int containg the new height of the image
                an int containg the new width of the image
       :returns : a list containing the resized single color channel image"""
    height_ratio = len(image) / new_height
    width_ratio = len(image[0]) / new_width
    new_image = make_new_size_image(new_height, new_width)
    for row in range(len(new_image)):
        for column in range(len(new_image[0])):
            y, x = row * height_ratio, column * width_ratio
            new_image[row][column] = bilinear_interpolation(image, y, x)
    return new_image

########################################################################################################################


# question 7


def rotate_90_column(image: list, direction: str, column: int) -> list:
    rotated_image_column = list()
    rotation_start = len(image) - 1 if direction == "R" else 0
    rotation_end = -1 if direction == "R" else len(image)
    rotation_index_change = -1 if direction == "R" else 1
    for row in range(rotation_start, rotation_end, rotation_index_change):
        rotated_image_column.append(image[row][column])
    return rotated_image_column


def rotate_90(image: list, direction: str) -> list:
    """ a function that rotates an image to the stated direction
        :param : a list containing a two dimensional image
                 a string containing the upper case first letter of the rotation direction
        :return : a list containg the rotated image"""
    rotated_image = list()
    rotation_start = 0 if direction == "R" else len(image[0]) - 1
    rotation_end = len(image[0]) if direction == "R" else -1
    rotation_index_change = 1 if direction == "R" else -1
    for column in range(rotation_start, rotation_end, rotation_index_change):
        rotated_image.append(rotate_90_column(image, direction, column))
    return rotated_image

############################################################################################

# question 8


def get_indexes(range: int, index: int, r: int) -> tuple:
    """ a function that returns the start and the end of the indexes
        :param : an int containing the highest possible value of the index
                 an int containing the current pixel index
                 an int containing the r parameter
        :return : a tuple containing the start and the end of the cell indexes for the calculation """
    index_start = 0 if index - r < 0 else index - r
    index_end = range if index + r + 1 > range else index + r + 1
    return index_start, index_end


def get_threshold_cell_value(blurred_image: list, i: int, j: int, r: int) -> float:
    """ a function that calculates the threshold cell value according to the formula
        :param: a list containing the image after blurring
                an int containg the i (row) index of the threshold calculation
                an int containing the j (column index of the threshold calalculation
                an int containg the r parameter for the calcualtion
        :returns: an int containg the threshold value for the current pixel"""
    cell_value = 0
    counter = 0
    for row in range(*get_indexes(len(blurred_image), i, r)):
        for column in range(*get_indexes(len(blurred_image[0]), j, r)):
            cell_value += blurred_image[row][column]
            counter += 1
    return cell_value / counter


def make_threshold(blurred_image: list, block_size: int) -> list:
    """a function that creates the threshold value for each pixel in the image
       :param : a list containing the original image after blurring
                an int containing the size of a threshold block
       :returns : a list containg the threshold value for each pixel"""
    r = block_size // 2
    threshold = copy.deepcopy(blurred_image)
    for row in range(len(threshold)):
        for column in range(len(threshold[0])):
            threshold[row][column] = get_threshold_cell_value(blurred_image, row, column, r)
    return threshold


def get_edges(image: list, blur_size: int, block_size:int, c: int) -> list:
    """ a function that returns an images that contains the edges of the objects in the image
        :param : a list containing an image with a single color channel
                 an int containing the blur size for the blurring before the calculation of edges
                 an int containing the block size for calculation of the threshold
        :returns : a list containing object edge image with a single color channel"""
    edge_image = copy.deepcopy(image)
    blurred_image = apply_kernel(image, blur_kernel(blur_size))
    threshold = make_threshold(blurred_image, block_size)
    for row in range(len(image)):
        for column in range(len(image[0])):
            edge_image[row][column] = 0 if blurred_image[row][column] < threshold[row][column] - c else 255
    return edge_image


########################################################################################################################

# question 9


def quantize(image: list, N: int) -> list:
    """ a function that quantizes the colors of an image into N colors
        :param : a list containing an image with a single color channel
                 an int containing the n parameter according the quantization index
        :return : a list containing the original image after quantization"""
    quantized_image = copy.deepcopy(image)
    for row in range(len(image)):
        for column in range(len(image[0])):
            quantized_image[row][column] = round(math.floor(image[row][column] * (N/255)) * (255/N))
    return quantized_image

#######################################################################################################################


# question 10


def quantize_colored_image(image: list, N: int) -> list:
    """ a function that quantizes the colors of an image into N colors
          :param : a list containing an image with multiple color channels
                   an int containing the n parameter according the quantization index
          :return : a list containing the original image after quantization"""
    seperated_color_channels = separate_channels(image)
    for channel in range(len(seperated_color_channels)):
        seperated_color_channels[channel] = quantize(seperated_color_channels[channel], N)
    return combine_channels(seperated_color_channels)

#######################################################################################################################


# question 11


def add_mask_single_channel(image1_channel: list, image2_channel: list, mask: list) -> list:
    """ a function that adds a mask from one single color channel image to another
        :param : a list containing a single color channel of the background image
                a list containing a single color channel of the mask image
                a list containing the mask template
        :return : a list containg a single channel image after the addition of the mask
                  from image1 to image2 according to the mask template"""
    new_image_channel = copy.deepcopy(image1_channel)
    for row in range(len(image1_channel)):
        for column in range(len(image1_channel[0])):
            new_image_channel[row][column] = \
                round(image1_channel[row][column] * mask[row][column] + \
                      image2_channel[row][column] * (1 - mask[row][column]))
    return new_image_channel


def make_image_channel_list(image: list) -> list:
    """ a function that switches the image channels to the appropriate format
        before adding a mask
        :param : a list containing an with an unkown amount of channels
        :return : a list of the channels of that image in the correct format for the masking"""
    image_channels = list()
    if type(image[0][0]) is int:
        image_channels.append(copy.deepcopy(image))
    else:
        image_channels = separate_channels(image)
    return image_channels


def add_mask(image1: list, image2: list, mask: list) -> list:
    """ a function that adds a mask from one multi color channel image to another
            :param : a list containing a multi color channel background image
                    a list containing a multi color channel mask image
                    a list containing the mask template
            :return : a list containing a single channel image after the addition of the mask
                      from image1 to image2 according to the mask template"""
    new_image = list()
    image1_channels, image2_channels = make_image_channel_list(image1), make_image_channel_list(image2)
    for channel in range(len(image1_channels)):
        new_image.append(add_mask_single_channel(image1_channels[channel], image2_channels[channel], mask))
    new_image = new_image[0] if len(new_image[0]) <= 1 else combine_channels(new_image)
    return new_image


########################################################################################################################


# question 12


def filter_mask(mask: list) -> list :
    """ a function that receives a list containing a black and white image
        and transforms it into a mask format image
        :param : a list containg a single color channel mask template
        :returns : a list comprised of ones and zeros according the add a mask function"""
    mask = copy.deepcopy(mask)
    for row in range(len(mask)):
        for column in range(len(mask[0])):
            mask[row][column] /= 255
    return mask


def cartoonify(image: list, blur_size: int, th_block_size: int, th_c: int, quant_num_shades: int) -> list:
    """ a function that cartoonifies a given image
        :parm: a list containing the original image
               an int containing the blur parameter for the blur kernel function
               an int contaning the block size for the threshold in the color quantification function
        :returns: a list containing a cartoonified version of the original image"""
    cartoon_image = quantize_colored_image(image, quant_num_shades)
    edges = get_edges(RGB2grayscale(image), blur_size, th_block_size, th_c)
    cartoon_image = separate_channels(cartoon_image)
    for channel in range(len(cartoon_image)):
        cartoon_image[channel] = add_mask_single_channel(cartoon_image[channel], edges, filter_mask(edges))
    cartoon_image = combine_channels(cartoon_image)
    return cartoon_image


#######################################################################################################################

if __name__ == "__main__":
    if len(sys.argv) == 8:
        image_source, cartoon_dest, max_im_size, blur_size, th_block_size, th_c, shades_num = sys.argv[1:]
        image = helper.load_image(image_source)
        if len(image[0]) >= int(max_im_size):
            resized_channels_list = list()
            resizing_ratio = int(max_im_size) / len(image[0])
            separated_channels_list = separate_channels(image)
            for i in range(len(separated_channels_list)):
                new_height = int(round(len(separated_channels_list[i]) * resizing_ratio))
                new_width = int(round(len(separated_channels_list[i][0]) * resizing_ratio))
                resized_channels_list.append(resize(separated_channels_list[i],  new_height, new_width))
                image = combine_channels(resized_channels_list)
            cartooned_image = cartoonify(image, int(blur_size), int(th_block_size), int(th_c), int(shades_num))
            helper.save_image(cartooned_image, cartoon_dest)
    else:
        print("ERROR: wrong number of parameters, program will now quit")
