from forex_python.converter import CurrencyRates
import json
from datetime import datetime

def convert_currency(amount, from_currency, to_currency):
    c = CurrencyRates()
    try:
        exchange_rate = c.get_rate(from_currency, to_currency)
        converted_amount = amount * exchange_rate
        return converted_amount, exchange_rate
    except:
        return None, None

def save_conversion_history(history):
    with open('conversion_history.json', 'w') as file:
        json.dump(history, file)

def load_conversion_history():
    try:
        with open('conversion_history.json', 'r') as file:
            history = json.load(file)
        return history
    except FileNotFoundError:
        return []

def main():
    conversion_history = load_conversion_history()

    amount = float(input("Entrez le montant à convertir : "))
    from_currency = input("Entrez la devise source (par ex. USD) : ").upper()
    to_currency = input("Entrez la devise cible (par ex. EUR) : ").upper()

    converted_amount, exchange_rate = convert_currency(amount, from_currency, to_currency)

    if converted_amount is not None:
        print(f"{amount} {from_currency} équivaut à {converted_amount:.2f} {to_currency} (Taux de change : {exchange_rate:.4f})")

        # Ajouter la conversion à l'historique
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        conversion_history.append({
            "timestamp": timestamp,
            "from_currency": from_currency,
            "to_currency": to_currency,
            "amount": amount,
            "converted_amount": converted_amount,
            "exchange_rate": exchange_rate
        })

        # Sauvegarder l'historique
        save_conversion_history(conversion_history)
    else:
        print("La conversion est impossible. Veuillez vérifier les devises saisies.")

if __name__ == "__main__":
    main()
