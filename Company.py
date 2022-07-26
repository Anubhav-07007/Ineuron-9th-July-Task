""" Here i am  create a company Ineuron.

    Multiple course are available like : Data Science , Big Data , Data Analytics , Programming.

    We are offering to student  Job, Internship and Affiliate programm.

    We have also Tech Neuron and Kids Neuron course available on the website.

"""

import  logging

logging.basicConfig(filename="Company.log",level=logging.DEBUG,format="%(asctime)s %(name)s %(levelname)s %(message)s  ")

# Multilevel Inheritance : Class Company inherit all method from class Course. " However class Course have : # Multiple Inheritance : Class Course inherit all method from data_science, big_data,data_analytics, programming)"

from Company_course import  Course
from One_Neuron import  one_neuron
from Job_Portal import  job_portal
from Internship_Portal import  Internship
from Blog_Hall_of_Fame import blog_and_fame
from Affiliate import affiliate


"""Define Company Class as a blueprint. Inside a Company class inherit other classes: Like Course, one_neuron, job_portal,Internship,blog_and_fame
affiliate.
"""
class Company(Course,one_neuron,job_portal,Internship,blog_and_fame,affiliate):

    company="Ineuron"
    details=["17th floor Tower A, Brigade Signature Towers, Sannatammanahalli, Bengaluru, Karnataka 562129.","+91 87885-03778","contact@ineuron.ai"]
    about_us="iNeuron started as a product development company, then launched its ed-tech division. We provide 360 degree solutions from learning to internship to finding a job, and the first ever educational OTT platform to upgrade your skill set."

    def Name(self):
        logging.info("Create a function to print the company name.")
        return ("The company name is", self.company)

    def Contact_details(self):
        logging.info("Create a function to print the contact details of company.")
        return ("You can reach out to us",self.details)

    def About_company(self):
        logging.info("Create a function to read about the company.")
        return ("Read about us",self.about_us)

Company_obj=Company()

logging.info(Company_obj.Name())
logging.info(Company_obj.Contact_details())
logging.info(Company_obj.About_company())
logging.info(Company_obj.Data_Science_course())
logging.info(Company_obj.Big_Data_Course())
logging.info(Company_obj.Data_Analytics_Course())
logging.info(Company_obj.Course_details())
logging.info(Company_obj.Read_blog())
logging.info(Company_obj.Fame_story())
logging.info(Company_obj.Internship_course())
logging.info(Company_obj._affiliate__Affiliate_Programm())  # Private method : Data abstraction
logging.info(Company_obj._job_portal__Open_job())            # Private method : Data abstraction
logging.info(Company_obj._one_neuron__Tech())                # Private method : Data abstraction
