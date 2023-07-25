import json
from typing import Any
from typing import Union
import atexit
from logger import Logger

#OS Modul zum löschen von Dateien importieren
import os

Log = Logger("database")

DATA_PATH = "data/"
DATA_BACKUP_PATH = "data/backup/"

class Database:
    def __init__(self, database_name: str) -> None:
        
        
        self.db = DATA_PATH + database_name + ".json"
        self.db_clearname = database_name
        
        Log.log(f"Öffne Datenbank '{self.db_clearname}'... ({self.db})", "info")
        #Speichern der Datenbank beim Beenden des Programms
        atexit.register(self._write)
        
        #Initialisierung der Datenbank
        try:
            self.data = self._read()
            
            #Wenn die Datenbank leer ist, setze die Varaible auf ein leeres Dictionary
            if self.data == None:
                self.data = {}
                
            Log.log(f"Die Datenbank '{self.db_clearname}' wurde geöffnet!")
        
        except FileNotFoundError:
            #Wenn die Datei nicht existiert, wird sie erstellt
            self.data = {}
            self._write()
            Log.log(f"Die Datenbank '{self.db_clearname}' wurde erstellt!", "info")
    
    def _write(self) -> None:
        """Interne Funktion zum Schreiben in die Datei"""
        with open(self.db, "w") as file_data:
            json.dump(self.data, file_data)
    
    def _read(self) -> None:
        """Interne Funktion zum Lesen aus der Datei"""""
        with open(self.db) as file_data:
            self.data = json.load(file_data)
            
    def get_keys(self) -> list[str]:
        """Holt alle Schlüssel aus der Datenbank"""
        keys = self.data.keys()
        return keys
        
    def get_value(self, key: str) -> Union[str, int, float, bool, None, list, dict]:
        """Holt den Wert zu einem Schlüssel aus der Datenbank"""
        value = self.data[key]
        return value

    def set(self, key: str, value: Any) -> None:
        """Setzt den Wert des jeweiligen Schlüssels in der Datenbank"""
        self.data[key] = value
        Log.log(f"Der Schlüssel '{key}' in der Datenbank '{self.db_clearname}' wurde bearbeitet!")

    def rem_key(self, key: str) -> None:
        """Löscht den Schlüssel samt Wert aus der Datenbank"""
        del self.data[key]
          
    def save(self) -> None:
        """Manuelles Speichern der Datenbank"""
        self._write()
    
    def delete(self) -> None:
        """Löscht die gesamte Datenbank"""
        Log.log(f"Die Datenbank '{self.db_clearname}' wird gelöscht...", "warning")
        self.backup()
        
        #Löschen der Datei
        os.remove(self.db)
        
        Log.log(f"Die Datenbank '{self.db_clearname}' wurde gelöscht!", "warning")
        

        
    def backup(self) -> None:
        """Erstellt eine Sicherungskopie der Datenbank, wird automatisch beim löschen der Datenbank ausgeführt"""
        Log.log(f"Die Datenbank '{self.db_clearname}' wird gesichert...", "info")
        #Sicherung des Zwischenspeichers
        with open(f"{DATA_BACKUP_PATH}cached-{self.db}", "w") as file_data:
            json.dump(self.data, file_data)
            
        #Sicherung der bestehenden Datenbank-Datei
        with open(self.db) as file_data:
            data = json.load(file_data)
            
        with open(f"{DATA_BACKUP_PATH}file-{self.db}", "w") as file_data:
            json.dump(data, file_data)
            
        Log.log(f"Die Datenbank '{self.db_clearname}' wurde gesichert!", "info")
        
    def __del__(self):
        self._write()


if __name__ == "__main__":
    #Teste die Datenbank auf Funktion
    db = Database("test")
    db.set_value("testkey", "testvalue")
    db.get_value("testkey")
    db.delete()