"""We create a function to print the course available in Data Science Tab"""

import logging

logging.basicConfig(filename='Data.log',level=logging.DEBUG,format="%(asctime)s %(name)s %(levelname)s %(message)s  ")


class data_science:
    Course = ["Full Stack Data Science", "Python", "Machine Learning", "Deep Learning", "Computer Vision"]

    try:
        logging.info("Create a Function to print the Data Science Course")

        def Data_Science_course(self):
            list1=[]

            for i in self.Course:
                list1.append(i)
            logging.info(list1)
            return list1

    except Exception as e:
        logging.exception(e)


#Data_Science_obj=data_science()

#logging.info(Data_Science_obj.Data_Science_course())