import math

def giai_pt_bac2(a=1,b=2,c=3):
    """
    Day la ham giai pt bac hai
    """
    delta = b**2 - 4 * a * c
    if delta >= 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return x1, x2
    print('pt vo nghiem')
    return None, None


b1, b2 = giai_pt_bac2(3, 2, -1)

print(b1)
print(b2)

def khoang_cach(a,b):
    """
    Ham tinh khaong cach giua 2 diem
    """
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

a = (1, 2)
b = (3, 2)
print(khoang_cach(a, b))