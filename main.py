import requests

# APIキーを設定
API_KEY = "YOUR_API_KEY"
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/"

def get_rate(base_currency, target_currency):
    url = BASE_URL + base_currency
    response = requests.get(url)
    data = response.json()
    return data['conversion_rates'][target_currency]

def convert_currency():
    print("通貨換算アプリ")
    print("モード選択:")
    print("1: 円 → ウォン")
    print("2: 円 → シンガポールドル")
    print("3: ウォン → 円")
    print("4: シンガポールドル → 円")

    mode = input("番号を入力してください（1-4）: ")
    amount = float(input("金額を入力してください: "))

    if mode == "1":
        rate = get_rate("JPY", "KRW")
        result = amount * rate
        print(f"{amount} 円 → {result:.2f} KRW")
    elif mode == "2":
        rate = get_rate("JPY", "SGD")
        result = amount * rate
        print(f"{amount} 円 → {result:.2f} SGD")
    elif mode == "3":
        rate = get_rate("KRW", "JPY")
        result = amount * rate
        print(f"{amount} KRW → {result:.2f} 円")
    elif mode == "4":
        rate = get_rate("SGD", "JPY")
        result = amount * rate
        print(f"{amount} SGD → {result:.2f} 円")
    else:
        print("無効な番号です")

if __name__ == "__main__":
    convert_currency()
