def m_to_cm(n):
    return n*100

def cm_to_m(n):
    return n/100

def cm_to_inches(n): 
    return n/2.54

def feet_to_inches(n): 
    return n*12

def inches_to_cm(n): 
    return n*2.54


if __name__ == "__main__":
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')
    print(f'100cm = {cm_to_inches(100)}inches')
    print(f'10ft = {feet_to_inches(10)}inches')
    print(f'100inches = {inches_to_cm(100)}cm')
