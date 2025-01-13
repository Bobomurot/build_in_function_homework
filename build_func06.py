def main(a):
    """Yuqori o'nlik sonli o'zgaruvchi 'a' berilgan. Natijani README.md faylida berilganidek 2 onlik raqamgacha yaxlitlang.
    https://github.com/codeschool43/Build_in_function_homework#build_func06

    Argümentlar:
        a (float): o'nlik son
        
    Qaytish:
        float: 2 onlik raqamgacha yaxlitlangan natija
    """
    x = round(a, 2)
    return x
b = main(3.456)

print(b) # Output: 3.46
