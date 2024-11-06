import tkinter as tk

class ModifyPopup(tk.Toplevel):
    def __init__(self, parent, record):
        super().__init__(parent)
        self.title("Modyfikacja rekordu")
        self.geometry("400x200")
        self.record = record

        # Zielona sekcja z polami tekstowymi
        self.create_fields()

        # Żółty przycisk "Zapisz" i brązowy przycisk "Anuluj"
        self.create_buttons()

    def create_fields(self):
        """Tworzy pola tekstowe dla edytowalnych wartości rekordu."""
        self.fields_frame = tk.Frame(self, bg="green")
        self.fields_frame.pack(fill="x", padx=10, pady=10)

        self.entries = []
        for i, value in enumerate(self.record):
            label = tk.Label(self.fields_frame, text=f"Pola {i+1}", bg="green")
            label.pack(anchor="w", padx=5, pady=2)

            entry = tk.Entry(self.fields_frame)
            entry.insert(0, value)
            entry.pack(fill="x", padx=5, pady=2)
            self.entries.append(entry)

    def create_buttons(self):
        """Tworzy przyciski 'Zapisz' i 'Anuluj'."""
        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        save_button = tk.Button(button_frame, text="Zapisz", bg="yellow", command=self.save_record)
        save_button.pack(side="left", padx=5)

        cancel_button = tk.Button(button_frame, text="Anuluj", bg="brown", command=self.destroy)
        cancel_button.pack(side="left", padx=5)

    def save_record(self):
        """Zapisuje zmiany rekordu i zamyka okno."""
        updated_values = [entry.get() for entry in self.entries]
        print("Zapisano nowe wartości:", updated_values)
        self.destroy()