class Kalkulacka:

    @classmethod
    def secti(cls, a:float, b:float) -> float:
	'''
	Tato funkce secte dve cisla
	input:
		a: float
		b: float
	returns:
		float
	'''
        return a + b

    @classmethod
    def odecti(cls, a:float, b:float) -> float:
        return a - b

    @classmethod
    def vynasob(cls, a:float, b:float) -> float:
        return a * b

    def vydel(cls, a, b):
	return a/b

def main():
    print(Kalkulacka.secti(5, 6))

if __name__ == "__main__":
    main()
