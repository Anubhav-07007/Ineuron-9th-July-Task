"""Create a Class a methood for One Neuron"""

import logging

logging.basicConfig(filename='One_Neuron.log',level=logging.DEBUG,format="%(asctime)s %(name)s %(levelname)s %(message)s  ")

class one_neuron:
    Kids="Kids Neuron"

    Tech="Tech Neuron"

    try:
        logging.info("Print the course details in One Neuron")

        def Kids(self):
            course=self.Kids
            logging.info ("The couse is %s and price is 7080",course)
            return course

    except Exception as e:
        logging.info(e)

    try:
        logging.info("Print the course & Price Details in Tech Neuron")

        def __Tech(self):
            Tech_course=self.Tech
            logging.info("The Tech couse is %s and price is 25000",Tech_course)
            return Tech_course

    except Exception as e:
        logging.info(e)


One_Neuron_obj=one_neuron()

logging.info(One_Neuron_obj.Kids)

logging.info(One_Neuron_obj._one_neuron__Tech())