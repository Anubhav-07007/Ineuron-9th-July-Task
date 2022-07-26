"""We create a function to print the open Internship course available in Tab"""

import logging

logging.basicConfig(filename='Internship.log',level=logging.DEBUG,format="%(asctime)s %(name)s %(levelname)s %(message)s  ")

class Internship:

    project=["python","ML","DL","CV"]

    try:
        logging.info("Print the internship course")

        def Internship_course(self):
            list5=[]
            for i in self.project:
                list5.append(i)
            logging.info("list5")
            return list5


    except Exception as e:
        logging.info(e)

Internship_obj=Internship()

logging.info(Internship_obj.Internship_course())