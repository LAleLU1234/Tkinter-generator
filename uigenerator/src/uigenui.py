import tkinter as tk
from tkinter import filedialog

# Funktion für den Button "Erstellen"
def single_button_action():
    try:
        # Werte aus entry2 abrufen
        geometry_value = entry2.get()

        # Überprüfen, ob die Eingabe das richtige Format hat (XXXxYYY)
        if "x" not in geometry_value or not all(part.isdigit() for part in geometry_value.split("x")):
            print("Ungültiges Format! Bitte XXXxYYY verwenden.")
            return

        # Dateiauswahl-Dialog öffnen
        file_path = filedialog.asksaveasfilename(
            defaultextension=".py",
            filetypes=[("Python Files", "*.py")],
            title="Speichern unter"
        )

        if not file_path:
            return  # Wenn der Nutzer den Dialog abbricht

        # Generiertes Script erstellen
        script_content = f"""import tkinter as tk
root = tk.Tk()
root.title(\"Mein Tkinter-Fenster\")  # Fenster-Titel setzen
root.geometry(\"{geometry_value}\")
root.mainloop()"""

        # Script in der ausgewählten Datei speichern
        with open(file_path, "w") as file:
            file.write(script_content)

        print(f"Script erfolgreich gespeichert unter: {file_path}")
    except Exception as e:
        print(f"Fehler: {e}")

# Erstelle das Hauptfenster
root = tk.Tk()
root.title("Mein Tkinter-Fenster")  # Fenster-Titel setzen

# Setze die Fenstergröße (Breite x Höhe)
root.geometry("600x800")

# Füge ein Beispiel-Label hinzu
label1 = tk.Label(root, text="Willkommen zu meinem Tkinter-Fenster!", font=("Arial", 16))
label1.pack(pady=20)  # Füge etwas Platz nach oben hinzu

# Erstelle die Toolbar
toolbar = tk.Frame(root, bg="lightgray")
toolbar.pack(side="top", fill="x", pady=10)

# Füge ein Label namens "Fenster" am Anfang der Toolbar hinzu
toolbar_label = tk.Label(toolbar, text="Fenster", bg="lightgray", font=("Arial", 14))
toolbar_label.pack(side="left", padx=10)

# Ersetze entry1 durch ein Label
entry1_label = tk.Label(toolbar, text="XXXxYYY", bg="lightgray", font=("Arial", 10))
entry1_label.pack(side="left", padx=5, pady=5)

# Füge eine Eingabezeile hinzu
entry2 = tk.Entry(toolbar, width=20)
entry2.pack(side="left", padx=5, pady=5)

# Füge einen einzelnen Button unterhalb der Toolbar hinzu
single_button = tk.Button(root, text="Erstellen", command=single_button_action)
single_button.pack(pady=20)

# Starte die Tkinter-Ereignisschleife
root.mainloop()
