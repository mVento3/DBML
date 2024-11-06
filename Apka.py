import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from AutoModel import *
from DomModel import *
from PiesModel import *
from PopupView import *

auta = AutoContainer([
    Auto("Toyota", "Corolla", 2015, "niebieski"),
    Auto("Honda", "Civic", 2018, "czarny"),
    Auto("Ford", "Focus", 2020, "biały"),
    Auto("Mazda", "3", 2019, "czerwony"),
    Auto("Volkswagen", "Golf", 2017, "szary"),
    Auto("Audi", "A4", 2021, "czarny"),
    Auto("BMW", "3", 2016, "niebieski"),
    Auto("Mercedes", "C", 2018, "srebrny"),
    Auto("Kia", "Ceed", 2019, "zielony"),
    Auto("Hyundai", "Elantra", 2020, "granatowy"),
    Auto("Toyota", "Corolla", 2015, "niebieski"),
    Auto("Honda", "Civic", 2018, "czarny"),
    Auto("Ford", "Focus", 2020, "biały"),
    Auto("Mazda", "3", 2019, "czerwony"),
    Auto("Volkswagen", "Golf", 2017, "szary"),
    Auto("Audi", "A4", 2021, "czarny"),
    Auto("BMW", "3", 2016, "niebieski"),
    Auto("Mercedes", "C", 2018, "srebrny"),
    Auto("Kia", "Ceed", 2019, "zielony"),
    Auto("Hyundai", "Elantra", 2020, "granatowy")
]).getListToDisplay()

domy = DomContainer([
    Dom("Ul. Kwiatowa 10", 4, 120, "biały"),
    Dom("Ul. Ogrodowa 5", 3, 85, "szary"),
    Dom("Ul. Zielona 3", 5, 140, "żółty"),
    Dom("Ul. Lipowa 7", 2, 60, "niebieski"),
    Dom("Ul. Długa 15", 6, 200, "beżowy"),
    Dom("Ul. Krótka 2", 3, 90, "zielony"),
    Dom("Ul. Wąska 8", 4, 110, "brązowy"),
    Dom("Ul. Parkowa 12", 5, 150, "czerwony"),
    Dom("Ul. Słoneczna 1", 4, 125, "biały"),
     Dom("Ul. Kwiatowa 10", 4, 120, "biały"),
    Dom("Ul. Ogrodowa 5", 3, 85, "szary"),
    Dom("Ul. Zielona 3", 5, 140, "żółty"),
    Dom("Ul. Lipowa 7", 2, 60, "niebieski"),
    Dom("Ul. Długa 15", 6, 200, "beżowy"),
    Dom("Ul. Krótka 2", 3, 90, "zielony"),
    Dom("Ul. Wąska 8", 4, 110, "brązowy"),
    Dom("Ul. Parkowa 12", 5, 150, "czerwony"),
    Dom("Ul. Słoneczna 1", 4, 125, "biały"),
    Dom("Ul. Kwiatowa 10", 4, 120, "biały"),
    Dom("Ul. Ogrodowa 5", 3, 85, "szary"),
    Dom("Ul. Zielona 3", 5, 140, "żółty"),
    Dom("Ul. Lipowa 7", 2, 60, "niebieski"),
    Dom("Ul. Długa 15", 6, 200, "beżowy"),
    Dom("Ul. Krótka 2", 3, 90, "zielony"),
    Dom("Ul. Wąska 8", 4, 110, "brązowy"),
    Dom("Ul. Parkowa 12", 5, 150, "czerwony"),
    Dom("Ul. Słoneczna 1", 4, 125, "biały"),
    Dom("Ul. Zaciszna 6", 3, 100, "szary")
]).getListToDisplay()

psy = DogContainer([
    Dog("Burek", "Owczarek Niemiecki", 3, "czarny"),
    Dog("Reksio", "Labrador", 5, "złoty"),
    Dog("Azor", "Buldog", 2, "biały"),
    Dog("Tobi", "Pudel", 4, "brązowy"),
    Dog("Maks", "Beagle", 3, "biało-brązowy"),
    Dog("Nero", "Rottweiler", 6, "czarny"),
    Dog("Bono", "Border Collie", 7, "czarno-biały"),
    Dog("Lucky", "Golden Retriever", 5, "złoty"),
    Dog("Diesel", "Pitbull", 4, "szary"),
    Dog("Zygi", "Dachshund", 2, "rudy"),
    Dog("Kora", "Shih Tzu", 1, "biały"),
    Dog("Nina", "Chihuahua", 3, "czarny"),
    Dog("Gaja", "Siberian Husky", 5, "szary"),
    Dog("Rocky", "Doberman", 6, "czarny"),
    Dog("Luna", "Akita Inu", 3, "biało-czarny"),
    Dog("Roxy", "Yorkshire Terrier", 4, "złoty"),
    Dog("Spike", "Mastiff", 5, "brązowy"),
    Dog("Mila", "Maltańczyk", 1, "biały"),
    Dog("Leo", "Samoyed", 4, "biały"),
    Dog("Dino", "Chow Chow", 2, "rudy"),
    Dog("Bella", "Cocker Spaniel", 3, "brązowy"),
    Dog("Max", "Dalmatyńczyk", 6, "biało-czarny"),
    Dog("Czaki", "Cane Corso", 5, "czarny"),
    Dog("Fibi", "Jack Russell Terrier", 2, "biało-brązowy"),
    Dog("Loki", "Shiba Inu", 4, "rudy"),
    Dog("Aron", "Hound", 5, "czarno-brązowy"),
    Dog("Lara", "Whippet", 2, "szary"),
    Dog("Maja", "Papillon", 3, "biało-czarny"),
    Dog("Miki", "Pomeranian", 1, "rudy"),
    Dog("Kika", "Basset Hound", 6, "brązowo-biały"),
]).getListToDisplay()
class CustomLayoutApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Konfiguracja okna
        self.title("Custom Layout Application")
        self.geometry("800x400")  # Początkowy rozmiar okna

        # Inicjalizacja sekcji
        self.create_top_frame()
        self.create_middle_frame()
        self.create_side_frame()

        # Konfiguracja kolumn i wierszy dla dynamicznego rozciągania
        self.grid_columnconfigure(0, weight=1)  # Główna kolumna jest rozciągliwa
        self.grid_columnconfigure(1, weight=0)  # Boczne okno stałej szerokości
        self.grid_rowconfigure(1, weight=1)     # Dolny wiersz (środkowa i boczna sekcja) jest rozciągliwy

        # Event na dynamiczną zmianę rozmiaru okna
        self.bind('<Configure>', self.adjust_window_size)

        # Zmienna do przechowywania zaznaczonego wiersza
        self.selected_row = None
        self.current_data = []  # Zmienna do przechowywania aktualnych danych

    def create_top_frame(self):
        """Tworzy górną sekcję (czarną) i dodaje 3 przyciski."""
        self.top_frame = tk.Frame(self, bg="black", height=50)
        self.top_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")

        # Przygotowanie różnych zestawów danych do wyświetlenia
        data1 = domy
        data2 = auta
        data3 = psy

        # Dodanie trzech przycisków, każdy z innym zestawem danych
        buttons_data = [("Domy", data1), ("Auta", data2), ("Psy", data3)]
        for i, (text, data) in enumerate(buttons_data):
            button = tk.Button(self.top_frame, text=text, command=lambda d=data: self.display_table(d))
            button.grid(row=0, column=i, padx=5, pady=10)

    def create_middle_frame(self):
        """Tworzy środkową sekcję z możliwością przewijania."""
        self.middle_frame = tk.Frame(self, bg="#2d6a8c")
        self.middle_frame.grid(row=1, column=0, sticky="nsew")

        # Utworzenie Canvas dla przewijanej treści
        self.canvas = tk.Canvas(self.middle_frame, bg="#2d6a8c")
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Dodanie pionowego paska przewijania do Canvas
        self.scrollbar = tk.Scrollbar(self.middle_frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill="y")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Utworzenie ramki wewnątrz Canvas, która będzie przewijana
        self.scrollable_frame = tk.Frame(self.canvas, bg="#2d6a8c")
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        # Dodanie ramki do Canvas
        self.canvas_frame = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

    def create_side_frame(self):
        """Tworzy boczną sekcję (pomarańczową) i dodaje przyciski na dole."""
        self.side_frame = tk.Frame(self, bg="#e67e22", width=100)
        self.side_frame.grid(row=1, column=1, sticky="nsew")
        
        # Dodanie przycisków na dole pomarańczowej sekcji
        button_names = ["Dodaj", "Usuń", "Zmień", "Pokaż analizę"]
        for i, name in enumerate(button_names):
            button = tk.Button(self.side_frame, text=name, command=lambda n=name: self.handle_button_click(n))
            button.pack(side="bottom", fill="x", padx=5, pady=5)

    def adjust_window_size(self, event):
        """Aktualizuje układ podczas zmiany rozmiaru okna."""
        self.update_idletasks()

    def display_table(self, data):
        """Wyświetla stylizowaną tabelę wewnątrz przewijanego obszaru."""
        # Usuwanie istniejących widżetów z przewijanej ramki
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        # Przechowujemy aktualne dane, aby móc do nich odnosić się później
        self.current_data = data

        # Stylizacja tabeli
        header_bg = "#4a90e2"  # Kolor nagłówka
        header_fg = "white"    # Kolor tekstu nagłówka
        row_bg_odd = "#d9edf7" # Kolor tła dla nieparzystych wierszy
        row_bg_even = "white"  # Kolor tła dla parzystych wierszy
        selected_bg = "#b3e5fc"  # Kolor tła dla wybranego wiersza
        font_style = ("Arial", 12)

        # Tworzenie nowej tabeli
        for row_index, row in enumerate(data):
            for col_index, cell in enumerate(row):
                # Nagłówek
                if row_index == 0:
                    cell_label = tk.Label(
                        self.scrollable_frame,
                        text=cell,
                        bg=header_bg,
                        fg=header_fg,
                        font=("Arial", 12, "bold"),
                        borderwidth=1,
                        relief="solid",
                        padx=10,
                        pady=5
                    )
                # Wiersze tabeli
                else:
                    cell_bg = row_bg_odd if row_index % 2 == 1 else row_bg_even
                    cell_label = tk.Label(
                        self.scrollable_frame,
                        text=cell,
                        bg=cell_bg,
                        fg="black",
                        font=font_style,
                        borderwidth=1,
                        relief="solid",
                        padx=10,
                        pady=5
                    )
                    
                    # Dodanie zdarzenia kliknięcia dla wyboru wiersza
                    cell_label.bind("<Button-1>", lambda e, idx=row_index: self.select_row(idx, data))

                cell_label.grid(row=row_index, column=col_index, sticky="nsew")

        # Konfiguracja, aby każda kolumna była rozciągliwa, wypełniając dostępną szerokość
        for col_index in range(len(data[0])):
            self.scrollable_frame.grid_columnconfigure(col_index, weight=1)

    def select_row(self, row_index, data):
        """Wybiera wiersz i podświetla go."""
        # Odznaczenie poprzednio wybranego wiersza
        if self.selected_row is not None:
            for col_index in range(len(self.current_data[0])):
                cell_bg = "#d9edf7" if self.selected_row % 2 == 1 else "white"
                self.scrollable_frame.grid_slaves(row=self.selected_row, column=col_index)[0].config(bg=cell_bg)

        # Ustawienie nowego wybranego wiersza
        self.selected_row = row_index
        for col_index in range(len(self.current_data[0])):
            self.scrollable_frame.grid_slaves(row=row_index, column=col_index)[0].config(bg="#b3e5fc")

    def handle_button_click(self, button_name):
        """Obsługuje kliknięcia przycisków w pomarańczowej sekcji."""
        if button_name == "Dodaj":
            self.add_record()
        elif button_name == "Usuń":
            self.delete_record()
        elif button_name == "Zmień":
            self.edit_record()
        elif button_name == "Pokaż analizę":
            self.show_analysis()

    def show_analysis(self):
        """Wyświetla wykres Gaussa wewnątrz niebieskiej sekcji."""
        # Czyszczenie istniejących widżetów w `scrollable_frame`
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        # Generowanie danych dla krzywej Gaussa
        x = np.linspace(-5, 5, 100)
        y = (1 / (np.sqrt(2 * np.pi))) * np.exp(-0.5 * x**2)

        # Tworzenie wykresu
        fig, ax = plt.subplots(figsize=(6, 4), dpi=100)
        ax.plot(x, y, label="Krzywa Gaussa", color="blue")
        ax.set_title("Analiza Danych - Krzywa Gaussa")
        ax.set_xlabel("Wartość")
        ax.set_ylabel("Prawdopodobieństwo")
        ax.legend()
        ax.grid()

        # Osadzenie wykresu w `scrollable_frame`
        canvas = FigureCanvasTkAgg(fig, master=self.scrollable_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    def add_record(self):
        """Funkcja do obsługi dodawania nowego rekordu."""
        self.open_add_popup()

    def delete_record(self):
        """Funkcja do obsługi usuwania zaznaczonego rekordu."""
        if self.selected_row is not None:
            confirm = messagebox.askyesno("Potwierdzenie usunięcia", "Czy na pewno chcesz usunąć wybrany rekord?")
            if confirm:
                del self.current_data[self.selected_row]
                self.selected_row = None
                self.display_table(self.current_data)
        else:
            messagebox.showwarning("Brak wyboru", "Proszę wybrać rekord do usunięcia.")

    def edit_record(self):
        """Funkcja do obsługi edycji zaznaczonego rekordu."""
        if self.selected_row is not None:
            self.open_edit_popup(self.current_data[self.selected_row])
        else:
            messagebox.showwarning("Brak wyboru", "Proszę wybrać rekord do edycji.")

    def open_add_popup(self):
        """Otwiera okno popup do dodawania nowego rekordu."""
        popup = tk.Toplevel(self)
        popup.title("Dodaj nowy rekord")
        
        labels = self.current_data[0]  # Nagłówki kolumn
        entries = []

        for i, label_text in enumerate(labels):
            label = tk.Label(popup, text=label_text)
            label.grid(row=i, column=0, padx=10, pady=5)

            entry = tk.Entry(popup)
            entry.grid(row=i, column=1, padx=10, pady=5)
            entries.append(entry)

        # Przycisk "Dodaj rekord"
        add_button = tk.Button(popup, text="Dodaj", command=lambda: self.save_new_record(entries, popup))
        add_button.grid(row=len(labels), column=0, columnspan=2, pady=10)

    def save_new_record(self, entries, popup):
        """Zapisuje nowy rekord na podstawie danych z popup i dodaje go do tabeli."""
        new_record = [entry.get() for entry in entries]
        
        # Dodaj nowy rekord do danych
        self.current_data.append(new_record)
        
        popup.destroy()  # Zamknięcie popupu po dodaniu rekordu
        self.display_table(self.current_data)  # Odświeżenie tabeli

    def open_edit_popup(self, record):
        """Otwiera okno popup do edycji wybranego rekordu."""
        popup = tk.Toplevel(self)
        popup.title("Edycja rekordu")
        
        labels = self.current_data[0]  # Nagłówki kolumn
        entries = []

        for i, (label_text, value) in enumerate(zip(labels, record)):
            label = tk.Label(popup, text=label_text)
            label.grid(row=i, column=0, padx=10, pady=5)

            entry = tk.Entry(popup)
            entry.insert(0, value)  # Wstawienie aktualnej wartości rekordu
            entry.grid(row=i, column=1, padx=10, pady=5)
            entries.append(entry)

        # Przycisk "Zapisz zmiany"
        save_button = tk.Button(popup, text="Zapisz", command=lambda: self.save_changes(record, entries, popup))
        save_button.grid(row=len(labels), column=0, columnspan=2, pady=10)

    def save_changes(self, record, entries, popup):
        """Zapisuje zmiany w rekordzie na podstawie danych z popup."""
        for i, entry in enumerate(entries):
            record[i] = entry.get()  # Aktualizacja rekordu w oryginalnych danych

        popup.destroy()  # Zamknięcie popupu po zapisaniu zmian
        self.display_table(self.current_data)  # Odświeżenie tabeli


# Uruchom aplikację
if __name__ == "__main__":
    app = CustomLayoutApp()
    app.mainloop()
