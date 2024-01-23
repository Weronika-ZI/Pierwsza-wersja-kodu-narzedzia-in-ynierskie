from datetime import datetime, timedelta
import time

dzisiaj = datetime.now()
print(f"Dzisiejsza data: {dzisiaj}")

print(f"Format daty 1: {dzisiaj.strftime('%Y/%m/%d %H:%M:%S')}")

print(f"Format daty 2: {dzisiaj.strftime('%y/%B/%d %I:%M:%S %p')}")

koniec_roku = datetime(dzisiaj.year, 12, 31)
dni_do_konca_roku = (koniec_roku - dzisiaj).days
print(f"Ilość dni do końca roku: {dni_do_konca_roku} dni")

dni_od_poczatku_roku = (dzisiaj - datetime(dzisiaj.year, 1, 1)).days + 1
print(f"Ilość dni od początku roku: {dni_od_poczatku_roku} dni")

print(f"Dzień tygodnia: {dzisiaj.strftime('%A')}")
print(f"Miesiąc: {dzisiaj.strftime('%B')}")
print(f"Rok: {dzisiaj.strftime('%Y')}")

nr_tygodnia = datetime.now().isocalendar()[1]
print(f"Który to tydzień roku: {nr_tygodnia}")