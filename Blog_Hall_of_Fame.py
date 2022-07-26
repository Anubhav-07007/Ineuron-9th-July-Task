"""We create a function to print the course available in Data Science Tab"""

import logging

logging.basicConfig(filename='Blog_Fame.log',level=logging.DEBUG,format="%(asctime)s %(name)s %(levelname)s %(message)s  ")

class Hall_of_fame:

    try:
        logging.info("check the successfully story on hall of fame")

        def Fame_story(self):
            logging.info("You can read the sucessfully story on hall of fame and you can reachout to person over linkdin profile")

    except Exception as e:
        logging.exception(e)

class Blog:

    try:
        logging.info("Read the blog")

        def Read_blog(self):
            logging.info("Read the blog on our website")

    except Exception as e:
        logging.exception(e)

class blog_and_fame(Hall_of_fame,Blog):
    pass


blog_and_fame_obj=blog_and_fame()


Hall_of_fame_obj=Hall_of_fame()

logging.info(Hall_of_fame_obj.Fame_story())

Blog_obj=Blog()

logging.info(Blog_obj.Read_blog())



