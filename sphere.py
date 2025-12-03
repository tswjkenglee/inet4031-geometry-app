import math


def surfaceArea(radius):
    area = 4 * math.pi * radius * radius
    return area


def volume(radius):
    vol = (4.0 / 3.0) * math.pi * radius * radius * radius
    return vol

# Function to prompt user for input and display the volume
def prompt():
    print()
    print("------------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND THE VOLUME OF A SPHERE")
    print("------------------------------------------------------------")
    radius = int(input("Please Enter the radius : "))
    print("\nThe Volume of a Sphere = ", volume(radius))

if __name__ == '__main__':
    prompt()
