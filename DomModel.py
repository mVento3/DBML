class Dom:
    # Zmienna klasowa zawierająca listę wszystkich właściwości jako stringi
    wszystkie_wlasciwosci = ["id", "adres", "liczba_pokoi", "powierzchnia", "kolor"]

    _id_counter = 1  # Zmienna klasowa do generowania unikalnych ID

    def __init__(self, adres, liczba_pokoi, powierzchnia, kolor):
        self.id = Dom._id_counter  # Przypisanie unikalnego ID z licznika
        self.adres = adres
        self.liczba_pokoi = liczba_pokoi
        self.powierzchnia = powierzchnia
        self.kolor = kolor
        Dom._id_counter += 1       # Zwiększenie licznika o 1

class DomContainer:
    wszystkie_wlasciwosci =  ["id", "adres", "liczba_pokoi", "powierzchnia", "kolor"]
    def __init__(self, objectList):
        self.itemList = objectList

    def getListToDisplay(self):
        result = []
        result.append(DomContainer.wszystkie_wlasciwosci)
        for element in self.itemList:
            result.append([
                element.id,
                element.adres, 
                element.liczba_pokoi,
                element.powierzchnia, 
                element.kolor
                ])
        return result
        

