from db.run_sql import run_sql

from models.merchant import Merchant
from models.tag import Tag
from models.transaction import Transaction

# write sql functions
# save 
def save(merchant):
    sql = "INSERT INTO merchants (name, active) VALUES (%s, %s) RETURNING *"
    values = [merchant.name, merchant.active]
    results = run_sql(sql, values)
    id = results[0]['id']
    merchant.id = id
    return merchant

# select all 
def select_all():
    merchants = []

    sql = "SELECT * FROM merchants"
    results = run_sql(sql)

    for row in results:
        merchant = Merchant(row['name'], row['active'], row['id'])
        merchants.append(merchant)
    return merchants
# select by id 
def select(id):
    merchant = None
    sql = "SELECT * FROM merchants WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        merchant = Merchant(result['name'], result['active'], result['id'])
    return merchant
# delete all 
def delete_all():
    sql = "DELETE FROM merchants"
    run_sql(sql)
#delete by id 
def delete(id):
    sql = "DELETE FROM merchants WHERE id = %s"
    values = [id]
    run_sql(sql, values)
# update 
def update(merchant):
    sql = "UPDATE merchants SET (name, active) = (%s, %s) WHERE id = %s"
    values = [merchant.name, merchant.active, merchant.id]
    run_sql(sql, values)
