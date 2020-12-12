from db.run_sql import run_sql

from models.tag import Tag
from models.merchant import Merchant
from models.transaction import Transaction

# write sql functions

# save 
def save(tag):
    sql = "INSERT INTO tags (category, active) VALUES (%s, %s) RETURNING *"
    values = [tag.category, tag.active]
    results = run_sql(sql, values)
    id = results[0]['id']
    tag.id = id
    return tag

# select all 
def select_all():
    tags = []

    sql = "SELECT * FROM tags"
    results = run_sql(sql)

    for row in results:
        tag = Tag(row['category'], row['active'], row['id'])
        tags.append(tag)
    return tags
# select by id 
def select(id):
    tag = None

    sql = "SELECT * FROM tags WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        tag = Tag(result['category'], result['active'], result['id'])
    return tag
# delete all 
def delete_all():
    sql = "DELETE FROM tags"
    run_sql(sql)
#delete by id 
def delete(id):
    sql = "DELETE FROM tags WHERE id = %s"
    values = [id]
    run_sql(sql, values)
# update 
def update(tag):
    sql = "UPDATE tags SET(category, active) = (%s, %s) WHERE id = %s"
    values = [tag.category, tag.active, tag.id]
    run_sql(sql, values)