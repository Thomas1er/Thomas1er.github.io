import numpy as np 
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

def image2format(image):
    noir = (0, 0, 0)
    blanc1 = (255, 255, 255)
    gris = (170, 170, 170)
    rose = (240,18,190)
    rouge = (255, 0, 0)
    jaune = (255,220,0)
    blanc2 = (221, 221, 221)
    orange = (255,133,27)
    lime = (1,255,12)
    vert1 = (46,204,64)
    cyan = (127,219,255)
    dark_blue = (0,116,217)
    light_blue = (57,204,204)
    violet = (177,13,201)
    dark_green = (61,153,112)

    couleur = np.array([noir, blanc1, gris, rose, rouge, jaune, blanc2, orange, lime, vert1, cyan, dark_blue, light_blue, violet, dark_green])

    new_image= -np.ones((image.shape[:-1]))
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i,j,0] != 140:
                new_image[i,j]=np.argmin(np.linalg.norm(couleur-image[i,j],axis=1))
            else :
                new_image[i,j]=-1
    
    return new_image

def format2image(format):
    noir = (0, 0, 0)
    blanc1 = (255, 255, 255)
    gris = (170, 170, 170)
    rose = (240,18,190)
    rouge = (255, 0, 0)
    jaune = (255,220,0)
    blanc2 = (221, 221, 221)
    orange = (255,133,27)
    lime = (1,255,12)
    vert1 = (46,204,64)
    cyan = (127,219,255)
    dark_blue = (0,116,217)
    light_blue = (57,204,204)
    violet = (177,13,201)
    dark_green = (61,153,112)

    couleur = np.array([noir, blanc1, gris, rose, rouge, jaune, blanc2, orange, lime, vert1, cyan, dark_blue, light_blue, violet, dark_green])

    new_image = np.zeros((*format.shape,3))
    new_image[:,:,0] = 140

    for i in range(format.shape[0]):
        for j in range(format.shape[1]):
            if format[i,j] != -1:
                new_image[i,j] = couleur[int(format[i,j])]
    
    return new_image


image = plt.imread("alliance.png")
image = image[:,:,:3]*255
format = image2format(image)
format = format.tolist()
text = "["
for i in format:
    text += str(i) + "\n"
text += "]"
with open("format.txt", "w") as f:
    f.write(text)

    with open("index.html", "r") as file:
        soup = BeautifulSoup(file, "html.parser")

    text_to_copy_div = soup.find("div", {"id": "textToCopy"})
    if text_to_copy_div:
        text_to_copy_div.string = text

    with open("index.html", "w") as file:
        file.write(str(soup))

if False:
    np.savetxt("format.txt", format, fmt='%d')
    new_image = format2image(format)
    new_image = new_image.astype(np.uint8)
    plt.imsave("new_image.png", new_image)
    plt.imshow(new_image)
    plt.show()


