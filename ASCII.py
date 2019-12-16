from PIL import Image
import numpy as np

gscale1 = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$" 

i = Image.open(r"C:\Users\nweinstein\Desktop\MAC_Portable.JPG")
(width, height) =  (800, 600)
i_resize = i.resize((width,height))
iar = np.asarray(i_resize, dtype = 'int64')
pxrows = len(iar)
pxcols = len(iar[0])
f = open(r"C:\Users\nweinstein\Desktop\ASCII_ART.txt", 'w')

def get_Avg_Intensity(iar):
	bright_matrix = []
	for x in iar:
		bright_matrix_row=[]
		for y in x:
			bright = (y[0] + y[1] + y[2])/3
			bright_matrix_row.append(bright)
		bright_matrix.append(bright_matrix_row)
	return(bright_matrix)

def get_invert_bright(bright_matrix):
	invert_matrix = []
	for x in bright_matrix:
		invert_matrix_row = []
		for y in x:
			invert_matrix_row.append(255 - y)
		invert_matrix.append(invert_matrix_row)
	return(invert_matrix)

def convert_to_ascii(bright_matrix):
		ascii_matrix = []
		for x in bright_matrix:
			ascii_matrix_row = []
			for y in x:
				ascii_char = gscale1[int(y/255 * len(gscale1)) - 1]
				ascii_matrix_row.append(ascii_char)
			ascii_matrix.append(ascii_matrix_row)
		return(ascii_matrix)

def print_ascii_matrix(ascii_matrix):
    for row in ascii_matrix:
        line = [p+p+p for p in row]
        f.write("".join(line) + "\n")

im_bright_matrix = get_Avg_Intensity(iar)
im_invert_matrix = get_invert_bright(im_bright_matrix)
im_ascii_matrix = convert_to_ascii(im_invert_matrix)
print_ascii_matrix(im_ascii_matrix)
print(width, height)