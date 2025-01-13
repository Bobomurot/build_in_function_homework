def main(x, y):
    """Butun sonli o'zgaruvchilar 'x' va 'y' berilgan. README.md faylida berilgan ifodaning qiymatini qaytaring.
    https://github.com/codeschool43/Build_in_function_homework#build_func09

    Argümentlar:
        x (int): butun son
        y (int): butun son
        
    Qaytish:
        int: ifodaning qiymati
    """
    a = 2*((y ** 3) + (x ** 2)*y)
    
    return a

print(main(2, 4))  # Output: 126
