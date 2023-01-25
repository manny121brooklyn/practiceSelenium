import logging

# create and configure logger
logging.basicConfig(filename="C:\dev\practiceSelenium\log_files\log_file1.log",
                    format= ('%(asctime)s:  %(levelname)s: %(message)s:')

                    )
# create logging object

logger = logging.getLogger()
# set the threshold of logger to debug
logger.setLevel(logging.DEBUG)

logging.debug('This is debug message')
logging.info("The application is running task number 5")
logging.warning('This is warning message')
logging.error('This is error message')
