"""Create a function to print all the course avaiable in Data Analytics tab"""

import logging

logging.basicConfig(filename='Data_Analytics.log',level=logging.DEBUG,format="%(asctime)s %(name)s %(levelname)s %(message)s  ")

class data_analytics:

    Course=["Power Bi","Tableau","SQL","Excel"]

    try:
        logging.info("Create a function to print all the course avaiable in Data Analytics tab")

        def Data_Analytics_Course(self):
            list3=[]
            for i in self.Course:
                list3.append(i)
            logging.info(list3)
            return list3


    except Exception as e:
        logging.info(e)

Data_Analytics_obj=data_analytics()

logging.info(Data_Analytics_obj.Data_Analytics_Course())