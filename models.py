import sys

def rf():
    print("Ejecutando Modelo")

def main():
    if sys.argv[1] == 'rf':
        rf()
    else:
        print("Sin modelo")

