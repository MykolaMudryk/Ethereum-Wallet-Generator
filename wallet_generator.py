from web3 import Web3

def get_wallet_address(private_key):
    w3 = Web3()
    try:
        private_key = private_key[2:]  # Видаляємо "0x" з початку рядка
        if len(private_key) != 64:
            raise ValueError("Неправильна довжина приватного ключа")
        account = w3.eth.account.from_key(private_key)
        address = account.address
        return address
    except ValueError as e:
        return str(e)

def read_private_keys_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            private_keys = file.read().splitlines()
            return private_keys
    except Exception as e:
        return []

def write_addresses_to_file(file_path, private_keys, addresses):
    try:
        with open(file_path, 'w') as file:
            for private_key, address in zip(private_keys, addresses):
                file.write(f"{private_key} - {address}\n")
        return f"Приватні ключі та адреси гаманців були успішно записані у файл {file_path}"
    except Exception as e:
        return f"Помилка при записі у файл: {e}"

def main():
    file_path_input = "private_keys.txt"
    file_path_output = "EVM_addresses.txt"
    private_keys = read_private_keys_from_file(file_path_input)

    if not private_keys:
        result_message = f"Не вдалося отримати приватні ключі з файлу {file_path_input}"
    else:
        addresses = []
        for private_key in private_keys:
            wallet_address = get_wallet_address(private_key)
            addresses.append(wallet_address)

        result_message = write_addresses_to_file(file_path_output, private_keys, addresses)

    print(result_message)

if __name__ == "__main__":
    try:
        import web3
    except ImportError:
        print("Встановлюємо бібліотеку web3...")
        try:
            import subprocess

            subprocess.check_call(["python3", "-m", "pip", "install", "web3"])
        except Exception as e:
            print(f"Не вдалося встановити web3: {e}")
            exit(1)

    main()
