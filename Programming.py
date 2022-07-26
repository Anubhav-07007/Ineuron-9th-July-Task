"""We create a function to print the course available in Programming Tab"""

import logging

logging.basicConfig(filename='Programming.log',level=logging.DEBUG,format="%(asctime)s %(name)s %(levelname)s %(message)s  ")

class programming:
    Course=["C++","C","Java","Hive","Scala","SQL","Python","R"]

    try:
        logging.info("We create a function to print the course available in Programming Tab")

        def Course_details(self):
            list5=[]
            for i in self.Course:
                list5.append(i)
            logging.info(list5)
            return list5

    except Exception as e:
        logging.exception(e)

obj_programming=programming()

logging.info(obj_programming.Course_details())

