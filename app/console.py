import pdb
from models.merchant import Merchant
from models.tag import Tag
from models.transaction import Transaction

import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository
import repositories.transaction_repository as transaction_repository

merchant_1 = Merchant("Sainsburys")
merchant_repository.save(merchant_1)

merchant_2 = Merchant("Tesco")
merchant_repository.save(merchant_2)

merchant_3 = Merchant("EON")
merchant_repository.save(merchant_3)


tag_1 = Tag("Grocories")
tag_repository.save(tag_1)
tag_2 = Tag("Bills")
tag_repository.save(tag_2)


transaction_1 = Transaction(merchant_1, tag_1, 14.99)
transaction_repository.save(transaction_1)

transaction_2 = Transaction(merchant_3, tag_2, 50.51)
transaction_repository.save(transaction_2)

