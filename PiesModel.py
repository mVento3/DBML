class Dog:
    # Zmienna klasowa zawierająca listę wszystkich właściwości jako stringi
    all_properties = ["id", "imie", "rasa", "wiek", "kolor_siersci"]

    _id_counter = 1  # Zmienna klasowa do generowania unikalnych ID

    def __init__(self, imie, rasa, wiek, kolor_siersci):
        self.id = Dog._id_counter  # Przypisanie unikalnego ID z licznika
        self.imie = imie
        self.rasa = rasa
        self.wiek = wiek
        self.kolor_siersci = kolor_siersci
        Dog._id_counter += 1       # Zwiększenie licznika o 1

class DogContainer:
    all_properties = ["id", "imie", "rasa", "wiek", "kolor_siersci"]
    def __init__(self, objectList):
        self.itemList = objectList

    def getListToDisplay(self):
        result = []
        result.append(DogContainer.all_properties)
        for element in self.itemList:
            result.append([
                element.id,
                element.imie, 
                element.rasa,
                element.wiek, 
                element.kolor_siersci
                ])
        return result