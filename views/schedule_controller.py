from flask import render_template
from config import app

class ScheduleController(object):

    @staticmethod
    @app.route('/subjects/create')
    def create_subj():
        return render_template('subjects/create.html')

    @staticmethod
    @app.route('/subjects/delete')
    def delete_subj():
        return render_template('subjects/delete.html')

    @staticmethod
    @app.route('/subjects/details')
    def details_subj():
        return render_template('subjects/details.html')

    @staticmethod
    @app.route('/subjects')
    def list_subj():
        return render_template('subjects/list.html')

    @staticmethod
    @app.route('/subjects/update')
    def update_subj():
        return render_template('subjects/update.html')
