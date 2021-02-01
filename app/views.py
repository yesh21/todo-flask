from flask import render_template, request, redirect, url_for 
from app import app 
from app.models import Todo 
from app import db 
  
  
@app.route("/")
def home():
    todo_list = Todo.query.all()
    return render_template("base.html", todo_list=todo_list)

@app.route("/complete")
def complete():
    todo_co = Todo.query.filter_by(complete=True).all()
    return render_template("complete.html", todo_list=todo_co)

@app.route("/incomplete")
def incomplete():
    todo_inco = Todo.query.filter_by(complete=False).all()
    return render_template("incomplete.html", todo_list=todo_inco)


@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    descript= request.form.get("descript")
    if Todo.query.filter_by(title=title).first() is None:
     new_todo = Todo(title=title, complete=False, descript=descript )
     db.session.add(new_todo)
     db.session.commit() 
     return redirect(url_for("home"))
    elif Todo.query.filter_by(title=title).first().title == title:
     return redirect(url_for("home"))
    else:
     new_todo = Todo(title=title, complete=False, descript=descript )
     db.session.add(new_todo)
     db.session.commit() 
     return redirect(url_for("home"))

@app.route("/updatecomp/<int:todo_id>")
def updateco(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("complete"))

@app.route("/updateinco/<int:todo_id>")
def updateinco(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("incomplete"))


@app.route("/update/<int:todo_id>")
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))