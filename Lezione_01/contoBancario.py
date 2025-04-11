
def contoBancario(m:float, mesi:int) -> None:
    if mesi>1:
        m=m*1.005
        mesi-=1
        contoBancario(m, mesi)
    else:
        print(f"Il valore dei soldi al termine del periodo è {m} euro")

contoBancario(1500, 12)