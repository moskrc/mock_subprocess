import f1
import f2

def superfunction():
    return [x.action() for x in [f1, f2]]

if __name__ == '__main__':
    print superfunction()