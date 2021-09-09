from config import app
from views.home_controller import HomeController
from views.schedule_controller import ScheduleController
from views.teachers_controller import TeachersController

if __name__=='__main__':
    hc = HomeController()
    nc = TeachersController()
    uc = ScheduleController()
    app.run()