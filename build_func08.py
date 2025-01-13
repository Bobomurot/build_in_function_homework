def main(x, y):
    """Butun sonli o'zgaruvchilar 'x' va 'y' berilgan. README.md faylida berilgan ifodaning qiymatini qaytaring.
    https://github.com/codeschool43/Build_in_function_homework#build_func08

    Argümentlar:
        x (int): butun son
        y (int): butun son
        
    Qaytish:
        int: ifodaning qiymati
    """
    a = 5 * (x ** 2) * (y ** 3) + x * (y ** 2)
    return a
b = main(7, 1)
print(b)