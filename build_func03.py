def main(n):
    """Beriilgan butun sonli o'zgaruvchi 'n' ning qiymatini README.md faylida berilgan ifodaga asoslanib qaytaring.
    https://github.com/codeschool43/Build_in_function_homework#build_func03

    Argümentlar:
        n (float): o'nlik son

    Qaytish:
        float: ifodaning qiymati
    """
    a = 3 * ((n + 1)**2)
    return a
x = main(3.5)
print(x)