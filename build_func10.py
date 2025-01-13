from math import pow

def main(x, y):
    """Butun sonli o'zgaruvchilar 'x' va 'y' berilgan. README.md faylida berilgan ifodaning qiymatini qaytaring.
    https://github.com/codeschool43/Build_in_function_homework#build_func10

    Argümentlar:
        x (int): butun son
        y (int): butun son
        
    Qaytish:
        int: ifodaning qiymati
    """
    a = (3 * pow(y, 1/2)) + pow(x, 2/3)
    return a
print(round(main(2, 4)))
