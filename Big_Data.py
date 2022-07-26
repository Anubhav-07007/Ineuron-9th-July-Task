"""Create a Function the course available in Big Data tab"""

import logging

logging.basicConfig(filename='Big_data.log',level=logging.DEBUG,format="%(asctime)s %(name)s %(levelname)s %(message)s  ")

class big_data:
    Course=["Big Data Master","Big Data on Cloud"]

    try:
        logging.info("create a function to print all the course available in Big Data")

        def Big_Data_Course(self):
            list2=[]
            for i in self.Course:
                list2.append(i)
            logging.info(list2)
            return  list2

    except Exception as e:
        logging.exception(e)

Big_data_obj=big_data()

logging.info(Big_data_obj.Big_Data_Course())



