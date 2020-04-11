import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def compression(data, width, height):
    result = np.array([])
    block_width = 3
    block_height = 3
    edge_width = width % block_width
    edge_height = height % block_height
    i = 0
    i0 = 0
    while(i < height - edge_height):
        j = 0
        while(j < width - edge_width):
            average = 0
            num = 0
            for b in range(block_width):
                for a in range(block_height):
                    average += data[i+a][j+b]
                    num += 1
            average = average / num
            result = np.append(result, average)
            j += block_width
        if(edge_width != 0):
            average = 0
            num = 0
            for b in range(edge_width):
                for a in range(block_height):
                    average += data[i+a][j+b]
                    num += 1
            average = average / num
            result = np.append(result, average)
        i += block_height
        i0 += 1
    if(edge_height != 0):
        i0 += 1
        j = 0
        while(j < width - edge_width):
            average = 0
            num = 0
            for b in range(block_width):
                for a in range(edge_height):
                    average += data[i+a][j+b]
                    num += 1
                average = average / num
            result = np.append(result, average)
            j += block_width
        if(edge_width != 0):
            average = 0
            num = 0
            for b in range(edge_width):
                for a in range(edge_height):
                    average += data[i+a][j+b]
                    num += 1
            average = average / num
            result = np.append(result, average)
    j0 = int(result.size / i0)
    result = result.reshape(i0, j0)
    return result

# Import a picture and create data
# return: data_mat, the amount of data, dimension of data
def pic():
    data = np.array([])
    img = Image.open('pictures/IMG_0016.jpg').convert('L')
    width = img.size[0]
    height = img.size[1]
    data = np.append(data, np.array(img))
    data = data.reshape(height, width)
    return (data, width, height)

if __name__ == "__main__":
    (data, width, height) = pic()
    result = compression(data, width, height)
    new_img = Image.fromarray(result)
    # new_img = Image.fromarray(data)
    new_img = new_img.convert('RGB')
    new_img.save('pictures/Miku2.jpg')
    new_img.show()