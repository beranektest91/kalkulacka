class Kalkulacka:

    @classmethod
    def secti(cls, a, b):
        return a + b

    @classmethod
    def odecti(cls, a, b):
        return a - b
    #baf
    @classmethod
    def vynasob(cls, a, b):
        return a * b 

def main():
    print(Kalkulacka.secti(5, 6))

if __name__ == "__main__":
    main()
