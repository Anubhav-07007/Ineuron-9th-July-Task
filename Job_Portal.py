"""Create a class and method for job portal"""

import logging

logging.basicConfig(filename='Job.log',level=logging.DEBUG,format="%(asctime)s %(name)s %(levelname)s %(message)s  ")

class job_portal:

    try:
        logging.info("Print the avaiable job in job portal")

        def __Open_job(self):
            logging.info("Print the Job details ")

    except Exception as e:
        logging.exception(e)

Job_Portal_obj=job_portal()

logging.info(Job_Portal_obj._job_portal__Open_job())

