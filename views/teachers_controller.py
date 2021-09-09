from flask import render_template
from config import app

class TeachersController(object):

    @staticmethod
    @app.route('/teachers/add')
    def create_t():
        return render_template('teachers/add.html')

    @staticmethod
    @app.route('/teachers/delete')
    def delete_t():
        return render_template('teachers/delete.html')

    @staticmethod
    @app.route('/teachers')
    def show_t():
        return render_template('teachers/teachers.html')

    @staticmethod
    @app.route('/teachers/update')
    def update_t():
        return render_template('teachers/update.html')
