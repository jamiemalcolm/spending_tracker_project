from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.transaction import Transaction
from models.tag import Tag
from models.merchant import Merchant
import repositories.transaction_repository as transaction_repository
import repositories.tag_repository as tag_repository
import repositories.merchant_repository as merchant_repository
import datetime


transactions_blueprint = Blueprint("transactions", __name__)

@transactions_blueprint.route("/transactions")
def transactions():
    transactions = transaction_repository.select_all()
    all_amounts = transaction_repository.total()
    total = sum(all_amounts) / 100
    return render_template("transactions/index.html", transactions=transactions, total = total)

@transactions_blueprint.route("/transactions/new")
def new_transaction():
    merchants = merchant_repository.select_all()
    tags = tag_repository.select_all()
    return render_template("transactions/new.html", merchants = merchants, tags = tags)

@transactions_blueprint.route("/transactions/new", methods=['POST'])
def log_new_transaction():
    merchant_id = request.form['merchant-name']
    tag_id = request.form['tag-category']
    amount = request.form['amount']

    merchant = merchant_repository.select(merchant_id)
    tag = tag_repository.select(tag_id)
    transaction = Transaction(merchant, tag, amount)
    transaction_repository.save(transaction)
    
    return redirect("/transactions")

# might not need this route...
@transactions_blueprint.route("/total")
def total():
    transactions = transaction_repository.select_all()
    all_amounts = transaction_repository.total()
    total = sum(all_amounts) / 100
    return render_template("/transactions/total.html", transactions = transactions, total = total)

