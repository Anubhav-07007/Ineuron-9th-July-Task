import logging

logging.basicConfig(filename="course.log",level=logging.DEBUG,format="%(asctime)s %(name)s %(levelname)s %(message)s")

from  Data_Science import  data_science
#obj1=data_science()

from Big_Data import  big_data
#obj2=big_data()

from Data_Analytics import  data_analytics

from Programming import programming


# Multiple Inheritance : Class Course inherit all method from data_science, big_data,data_analytics, programming)

class Course(data_science,big_data,data_analytics,programming):
    pass

obj_course=Course()

logging.info(obj_course.Data_Science_course())
logging.info(obj_course.Big_Data_Course())
logging.info(obj_course.Data_Analytics_Course())
logging.info(obj_course.Course_details())