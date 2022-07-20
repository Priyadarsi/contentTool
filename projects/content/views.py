from flask import render_template, url_for, flash, redirect, request, Blueprint
from projects.content.forms import ContentForm
from projects.content.search import searchbot

content_tool = Blueprint('content_tool', __name__)

@content_tool.route('/', methods=['GET', 'POST'])
def search():
    form = ContentForm()
    searchObj = searchbot()
    if form.validate_on_submit():

        title = form.title.data
        summary, description, length = searchObj.bot(title)
        return render_template('search_results.html', summary = summary, description = description, length = length, content_tool = content_tool)

    return render_template('search_page.html', form = form)
