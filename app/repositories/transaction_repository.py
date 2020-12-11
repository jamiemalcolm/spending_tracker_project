from db.run_sql import run_sql

from models.transaction import Transaction
from models.merchant import Merchant
from models.tag import Tag
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository
# write sql functions

# save 
def save(transaction):
    sql = "INSERT INTO transactions (merchant_id, tag_id, amount) VALUES (%s, %s, %s) RETURNING *"
    values = [transaction.merchant.id, transaction.tag.id, transaction.amount]
    results = run_sql(sql, values)
    id = results[0]['id']
    transaction.id = id
    return transaction
# select all 

# select by id 

# delete all 

#delete by id 

# update 