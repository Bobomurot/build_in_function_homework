def main(x, y):
    """Butun sonli o'zgaruvchilar 'x' va 'y' berilgan. README.md faylida berilgan ifodaning qiymatini qaytaring.
    https://github.com/codeschool43/Build_in_function_homework#build_func07

    Argümentlar:
        x (int): butun son
        y (int): butun son
        
    Qaytish:
        int: ifodaning qiymati
    """
    a = ((x ** 2) + (6 * (x ** 3)) + 3 * x * y)
    return a
b = main(5, 2)
print(b)