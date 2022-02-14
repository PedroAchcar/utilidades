def primo(num):
    i = 1
    cont = 0
    while i <= num:
        x = num % i
        i += 1
        if x == 0:
            cont += 1
    if cont <= 2:
        return True
    else:
        return False
