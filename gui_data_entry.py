import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import db_handle as dbh

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Data Entry")
        self.resizable(False, False)
        self.create_frame()
        
    def create_frame(self):
        self.mainframe = ttk.Frame(self)
        self.mainframe.pack(fill="both", expand=True)
        
        self.key_label = ttk.Label(self.mainframe, text="Schlüssel:")
        self.key_label.grid(row=0, column=0, sticky="w")
        
        self.key_entry = ttk.Entry(self.mainframe)
        self.key_entry.grid(row=0, column=1, sticky="w")
        
        self.value_label = ttk.Label(self.mainframe, text="Wert:")
        self.value_label.grid(row=1, column=0, sticky="w")
        
        self.value_entry = ttk.Entry(self.mainframe)
        self.value_entry.grid(row=1, column=1, sticky="w")
        
        self.database_label = ttk.Label(self.mainframe, text="Datenbank:")
        self.database_label.grid(row=2, column=0, sticky="w")
        
        self.database_entry = ttk.Entry(self.mainframe)
        self.database_entry.grid(row=2, column=1, sticky="w")
        
        self.add_button = ttk.Button(self.mainframe, text="Hinzufügen", command=lambda: self.add_data())
        self.add_button.grid(row=3, column=0, columnspan=2, sticky="ew",)
        
        self.copyright = ttk.Label(self.mainframe, text="© 2023 Bjarne Matz", font=("Segoe UI", 10))
        self.copyright.grid(row=99, column=0, columnspan=2)
        
    def add_data(self):
        # Werte aus den Entry-Feldern holen
        key = self.key_entry.get()
        value = self.value_entry.get()
        db = self.database_entry.get()
        
        # Value und Key Felder löschen
        self.key_entry.delete(0, "end")
        self.value_entry.delete(0, "end")
        
        # Key und Value in die Datenbank schreiben
        if key != "" and db != "":
            db_access = dbh.Database(db)
            db_access.set(key, value)
            db_access.save()
            
        else:
            messagebox.showerror("Fehler", "Es muss eine Datenbank und ein Schlüssel angegeben werden!")
            
        
        
        
if __name__ == "__main__":
    app = App()
    app.mainloop()