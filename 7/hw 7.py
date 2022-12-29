# потенциальные источники ошибок (2, 7, 4, 9 - нет сведений о родительском классе, 15, 36, 54, 60)
class NoMoneyToWithdrawError(Exception):
   def __init__(self, message):
       super().__init__(message)


class PaymentError(Exception):
   def __init__(self, message):
       super().__init__(message)


def print_accounts(accounts):
   """Печать аккаунтов."""
   print("Список клиентов ({}): ".format(len(accounts)))
   for i, (name, value) in enumerate(accounts.items(), start=1):
       print("{}. {} {}".format(i, name, value))


def transfer_money(accounts, account_from, account_to, value):
    if __name__ == "__main__":
       accounts = {
           "Василий Иванов": 100,
           "Екатерина Белых": 1500,
           "Михаил Лермонтов": 400
       }
       print_accounts(accounts)

       payment_info = {
           "account_from": "Екатерина Белых",
           "account_to": "Василий Иванов"
       }

       print("Перевод от {account_from} для {account_to}...".
             format(**payment_info))

       payment_info["value"] = int(input("Сумма = "))

    try:
        payment_info["value"] <= 0
        raise PaymentError("ошибка при переводе")
    except PaymentError as err:
        print(err)

    if payment_info["value"] > 0:
        try:
            payment_info["value"] <= accounts["Екатерина Белых"]
            transfer_money(accounts, **payment_info)
            print("OK!")
            accounts["Екатерина Белых"] = accounts["Екатерина Белых"] - payment_info["value"]
            accounts["Василий Иванов"] = accounts["Василий Иванов"] + payment_info["value"]
            print_accounts(accounts)

            if payment_info["value"] > accounts["Екатерина Белых"]:
            raise NoMoneyToWithdrawError("на счету {account_from} не хватает денег для перевода".format(**payment_info))
            except NoMoneyToWithdrawError as err:
            print('Будьте внимательны', err)









