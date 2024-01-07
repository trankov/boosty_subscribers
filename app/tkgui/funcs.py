from pathlib import Path
from tkinter import Text, INSERT
from tkinter.filedialog import askopenfilename

from core import text_report


class FileName:
    filename: str = ""
    text_field: Text

    def __init__(self, target):
        self.target = target

    def fill_output(self):
        self.set_file_name()
        self.text_field.insert(index=INSERT,
            chars=text_report(self.filename, sort_desc=True)
            if Path(self.filename).exists()
            else "File not found"
        )

    def set_file_name(self):
        self.filename = askopenfilename(defaultextension=".csv", filetypes=[("CSV", "*.csv")])
        self.target["text"] = self.filename
