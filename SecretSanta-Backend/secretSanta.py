import random

def shuffleNames(names: list):
    santas = names.copy()

    failed = True
    while failed:
        random.shuffle(santas)
        failed = False
        for i in range(len(names)):
            if santas[i] == names[i]:
                failed = True
                break 
    result_dict = {key: value for key, value in zip(names, santas)}
    return result_dict


start = ["ricky", "alexis", "bitmap", "miguel", "roxas", "axel", "franky"]
print(shuffleNames(start))


