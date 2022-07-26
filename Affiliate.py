"""Become a affiliate"""

import logging

logging.basicConfig(filename='Affiliate.log',level=logging.DEBUG,format="%(asctime)s %(name)s %(levelname)s %(message)s  ")

class affiliate:

    try:
        logging.info("Become a affiliate")

        def __Affiliate_Programm(self):     # data abstraction : private method )
            logging.info("Attain Financial freedom and joining the affiliate program.")

    except Exception as e:
        logging.exception(e)

Affiliate_obj=affiliate()

logging.info(Affiliate_obj._affiliate__Affiliate_Programm())  # We can't directly access the data : hiding the data behind the class.