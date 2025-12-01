from pathlib import Path
import csv
from datetime import datetime

class DadosGrafico:

    def __init__(self,path):
        self.path = path
        self.dates = []
        self.temperatures = []
        path_aux = Path(self.path)
        lines = path_aux.read_text().splitlines()
        reader = csv.reader(lines, delimiter=';')
        header_row = next(reader)
        temps_aux = []
        day = 0
        gravar = False

        for row in reader:

            try:
                current_date = datetime.strptime(row[0], '%d/%m/%Y')

                if current_date.day == day:
                    current_date_aux = current_date  
                    temp = float(row[2].replace(",", "."))
                    temps_aux.append(temp)

                if current_date.day != day:
                    if day != 0:
                        gravar = True
                    day = current_date.day
            except ValueError:
                pass
            else:
                if gravar:
                    self.dates.append(current_date_aux)
                    temp_grava = sum(temps_aux)/len(temps_aux)
                    self.temperatures.append(temp_grava)
                    gravar = False