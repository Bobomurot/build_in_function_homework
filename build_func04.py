def main(n):
    """Beriilgan butun sonli o'zgaruvchi 'n' ning qiymatini README.md faylida berilgan ifodaga asoslanib qaytaring.
    https://github.com/codeschool43/Build_in_function_homework#build_func04

    Argümentlar:
        n (int): butun son
        
    Qaytish:
        float: ifodaning qiymati
    """
    a = ((2+n)/3)**2
    return a
x = main(4)
print(x)