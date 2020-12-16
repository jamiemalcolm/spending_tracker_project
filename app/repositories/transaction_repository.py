from db.run_sql import run_sql

from models.transaction import *
from models.merchant import Merchant
from models.tag import Tag
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository

# save 
def save(transaction):
    sql = "INSERT INTO transactions (merchant_id, tag_id, amount) VALUES (%s, %s, %s) RETURNING *"
    values = [transaction.merchant.id, transaction.tag.id, transaction.amount]
    results = run_sql(sql, values)
    id = results[0]['id']
    transaction.id = id
    time_stamp = results[0]['time_stamp']
    transaction.time_stamp = time_stamp
    return transaction
# select all 
def select_all():
    transactions = []

    sql = "SELECT * FROM transactions"
    results = run_sql(sql)

    for row in results:
        merchant = merchant_repository.select(row['merchant_id'])
        tag = tag_repository.select(row['tag_id'])
        transaction = Transaction(merchant, tag, row['amount'], row['id'], row['time_stamp'])
        transactions.append(transaction)
    return transactions

# select by id 
def select(id):
    transaction = None
    sql = "SELECT * FROM transactions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)

    if result is not None:
        merchant = merchant_repository.select(result['merchant_id'])
        tag = tag_repository.select(result['tag_id'])
        transaction = Transaction(merchant, tag, result['amount'], result['id'], result['time_stamp'])
    return transaction
# delete all 
def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)
#delete by id 
def delete(id):
    sql = "DELETE FROM transactions WHERE id = %s"
    values = [id]
    run_sql(sql, values)
# update 
def update(transaction):
    sql = "UPDATE transactions SET (merchant_id, tag_id, amount) = (%s, %s, %s) WHERE id = %s"
    values = [transaction.merchant.id, transaction.tag.id, transaction.amount, transaction.id, transaction.time_stamp]
    run_sql(sql, values) 
# get total of all transactions 
def total():
    transactions = []

    sql = "SELECT * FROM transactions"
    results = run_sql(sql)

    for row in results:
        merchant = merchant_repository.select(row['merchant_id'])
        tag = tag_repository.select(row['tag_id'])
        transaction = Transaction(merchant, tag, row['amount'], row['id'], row['time_stamp'])
        pennies = int(transaction.amount * 100)
        transactions.append(pennies)
    return transactions

