from logger import logger

class file_logger(logger):

    def __init__(self, log_level, file_name = "file_log.txt"):
        logger.__init__(self, log_level)
        self.file_name = file_name

    def log(self, log_level, message):
        if(log_level<=self.__log_level__):
    	    f= open(self.file_name,"a+")
            f.write("{}: {}\n".format(log_level, message))
    	    f.close()
        return
