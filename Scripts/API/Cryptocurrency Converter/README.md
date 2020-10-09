# Cryptozor.py

**Author -> Abhinav Anand

## A Python Cryptocurrency converter.

## Run test.py (python test.py)
### Example:
``` python
from cryptozor import Cryptozor

# From USD to BTC
cryptozor = Cryptozor('usd', 'btc')

# Amount
value = cryptozor.convert(2500)

# Float value
print(value) 
```

### Currency support: 

Cryptocurrencies:
* Bitcoin (BTC)
* Ethereum (ETH)
* Ethereum Classic (ETC)
* Bitcoin Cash (BCH)
* Litecoin (LTC)
* ZCash (ZEC)
* 0x (ZRX)

