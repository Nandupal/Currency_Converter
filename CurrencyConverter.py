import requests

# Real-time exchange rates function
def get_exchange_rate(api_key, base_currency, target_currency):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    if response.status_code != 200 or data['result'] != 'success':
        raise Exception(f"Error fetching exchange rates: {data.get('error-type', 'Unknown error')}")
    return data['conversion_rates'][target_currency]

# Conversion Fucntion 
def convert_currency(api_key, amount, base_currency, target_currency):
    exchange_rate = get_exchange_rate(api_key, base_currency, target_currency)
    converted_amount = amount * exchange_rate
    return converted_amount

# Main function 
def main():
    api_key = "0ad77f930b9f0b0f117f7738"  # Ne api key pettu ikkada, (This api key is mine)
    amount = float(input("Enter the amount to convert: "))
    base_currency = input("Enter the base currency (e.g., USD): ").upper()
    target_currency = input("Enter the target currency (e.g., EUR): ").upper()
    
    try:
        converted_amount = convert_currency(api_key, amount, base_currency, target_currency)
        print(f"{amount} {base_currency} is equal to {converted_amount:.2f} {target_currency}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
