import pdb
from models.merchant import Merchant
from models.tag import Tag
from models.transaction import Transaction

import repositories.merchant_repository as merchant_repository

merchant_1 = Merchant("Sainsburys")
merchant_repository.save(merchant_1)

merchant_2 = Merchant("Tesco")
merchant_repository.save(merchant_2)


all_merchants = merchant_repository.select_all()

print(all_merchants)

sainsburys = merchant_repository.select(1)

print(sainsburys)

merchant_repository.delete_all()