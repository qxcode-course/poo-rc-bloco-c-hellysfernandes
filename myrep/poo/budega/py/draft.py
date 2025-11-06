class Cliente:
    def __init__(self):
        self.__name: str = ""
    
    def getName(self) -> str:
        return self.__name
    
    def __str__(self) -> str:
        return f"nome: {self.__name()}"
    
class Market:
    def __init__(self):
            self.counters: list[Cliente | None] = []
            self.queue: list[Cliente] = []

    def __str__(self) -> str:
         
         return f"Caixas: {self.counters} \nEspera: {self.queue}"
    
def main():
     mercado = Market()
     print(mercado)
main()