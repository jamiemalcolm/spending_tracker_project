from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.tag import Tag
import repositories.tag_repository as tag_repository


tags_blueprint = Blueprint("tags", __name__)

@tags_blueprint.route("/tags")
def tags():
    tags = tag_repository.select_all()
    return render_template("/tags/index.html", tags = tags)

@tags_blueprint.route("/tags/new")
def new_tag():
    return render_template("/tags/new.html", title="New spending category")

@tags_blueprint.route("/tags/new", methods=['POST'])
def create_new_tag():
    category = request.form['category']

    tag = Tag(category)
    tag_repository.save(tag)

    return redirect("/tags")

# add edit route and allow user to edit tag, make active false and/or delete

@tags_blueprint.route("/tags/<id>", methods=['GET'])
def show_this_tag(id):
    tag = tag_repository.select(id)
    return render_template("/tags/show.html", tag = tag)
