class Auto:
    # Zmienna klasowa zawierająca listę wszystkich właściwości jako stringi
    _id_counter = 1  # Zmienna klasowa do generowania unikalnych ID

    def __init__(self, marka, model, rok_produkcji, kolor):
        self.id = Auto._id_counter  # Przypisanie unikalnego ID z licznika
        Auto._id_counter += 1       # Zwiększenie licznika o 1
        self.marka = marka
        self.model = model
        self.rok_produkcji = rok_produkcji
        self.kolor = kolor
        self.przebieg = 0

class AutoContainer:
    wszystkie_wlasciwosci = ["id", "marka", "model", "rok_produkcji", "kolor", "przebieg"]
    def __init__(self, objectList):
        self.itemList = objectList

    def getListToDisplay(self):
        result = []
        result.append(AutoContainer.wszystkie_wlasciwosci)
        for element in self.itemList:
            result.append([element.id, element.marka, element.model, element.rok_produkcji, element.kolor, element.przebieg])
        return result
        

