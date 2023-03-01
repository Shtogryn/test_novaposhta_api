# test_novaposhta_api
Python api test framework for [Nova Poshta](https://new.novaposhta.ua/) company's API.

Used technologies (Python, Pytest, requests library, tox, allure)

# Configuration
In order to use this library you need to generate an API key [here](https://new.novaposhta.ua/)

Login on web site -> Налаштування -> Безпека -> Створити ключ.
Create **'.env'** file and write 

**API_KEY="YOUR GENERATED API KEY"**


Install packages run **'tox.ini'** file with command **'tox'** 

Or in case you have not installed **TOX** use **pip: -r requirements.txt**


# Implementation of method support for 'Nova Poshta' API models


### Address

- **searchSettlements** - search for settlements
- **searchSettlementStreets** - search for streets in the settlement
- **getAreas** - get list of areas
- **getSettlements** - get list of settlements
- **getCities** - getting a directory of settlements in Ukraine, where there are branches of "Nova Poshta" and you can arrange delivery to the office, as well as delivery to the address
- **getStreet** - getting a directory of streets of a settlement in Ukraine
- **save** - saving the address of the counterparty of the recipient/sender
- **delete** - deleting the recipient/sender counterparty address

# How to use it

**Run all cases**

"pytest -v -s"
      or 
 "tox -e np"     
### Command samples for Address model


(Proceed to test_nova_poshta folder)

**Run all cases of Address model**

"pytest -v -m addresses"

**Run positive test cases**

"pytest -v -m  positive .\test_novaposhta_address.py"

**Run negative test cases**

"pytest -v -m  negative .\test_novaposhta_address.py"

**To generate and see report**

"pytest -v -m addresses --alluredir reports"

"allure serve reports"



"# test_novaposhta_api" 
