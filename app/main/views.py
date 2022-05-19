from flask import Flask,render_template,url_for,request, redirect
from datetime import datetime
from flask_migrate import Migrate,MigrateCommand

from ..models import Notes
from .. import db
from . import main

@main.route('/',methods=["POST","GET"])
def notes():
	if request.method == "POST":
		task_content = request.form['content']
		new_task=Notes(task=task_content)
		try:
			db.session.add(new_task)
			db.session.commit()
			return redirect('/')
		except:
			return "There was a problem adding your task"

	else:
		tasks = Notes.query.order_by(Notes.date_added).all() # fetchisng all data
		return render_template('notes.html',title="Notes App",tasks=tasks)


@main.route('/delete/<int:id>')
def delete(id):
	task_to_delete = Notes.query.get_or_404(id)
	try:
		db.session.delete(task_to_delete)
		db.session.commit()
		return redirect('/')
	except:
		return "There was a problem in deleting that task"


#add task
@main.route('/update/<int:id>',methods=["POST","GET"])
def update(id):
	#get the task first for updating
	task = Notes.query.get_or_404(id)
	if request.method == "POST":
		task.task = request.form['content']
		try:
			db.session.commit()
			return redirect('/')
		except:
			return "There was a problem updating your task"

	else:
		return render_template('/update.html',title="Update", task = task)

