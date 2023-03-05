import tkinter as tk
import requests


def get_json(a):
    response = requests.get(f'https://api.nbp.pl/api/exchangerates/rates/a/{a}')
    if response.status_code != requests.codes.ok:
        return 0
    else:
        return response.json()['rates'][0]['mid']


def count_value(currency):
    value_pln = ent_value.get()
    counted = float(value_pln) * get_json(currency)
    lbl_result["text"] = f"{round(counted, 2)} PLN"


def count_pln(currency):
    value_currency = ent_value.get()
    counted_pln = float(value_currency) / get_json(currency)
    lbl_result["text"] = f"{round(counted_pln, 2)} {currency}"


root = tk.Tk()
root.title("Kalkulator walut")
root.resizable(False, False)

frm_entry = tk.Frame(master=root)
ent_value = tk.Entry(master=frm_entry, width=10)
lbl_pln = tk.Label(master=frm_entry, text="Podaj wartość: ")

ent_value.grid(row=0, column=1, sticky="e")
lbl_pln.grid(row=0, column=0, sticky="w")

btn_convert_usd = tk.Button(
    master=root,
    text="USD na PLN",
    command=lambda: count_value("USD")
)
btn_convert_eur = tk.Button(
    master=root,
    text="EUR na PLN",
    command=lambda: count_value("EUR")
)

btn_convert_usd_pln = tk.Button(
    master=root,
    text="PLN na USD",
    command=lambda: count_pln("USD")
)
btn_convert_eur_pln = tk.Button(
    master=root,
    text="PLN na EUR",
    command=lambda: count_pln("EUR")
)

lbl_result = tk.Label(master=root, text="", width=20)

frm_entry.grid(row=0, rowspan=4, column=0, padx=10)
btn_convert_usd.grid(row=0, column=1, pady=10)
btn_convert_eur.grid(row=1, column=1, pady=10)
btn_convert_usd_pln.grid(row=2, column=1, pady=10)
btn_convert_eur_pln.grid(row=3, column=1, pady=10)
lbl_result.grid(row=0, rowspan=4, column=2, padx=10)

root.mainloop()
