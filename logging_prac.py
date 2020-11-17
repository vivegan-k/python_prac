import logging
import os

#logging.basicConfig(filename='example.log',filemode='a',  level=logging.DEBUG)
#log1 =  logging.getLogger(os.getlogin())
#log = logging.getLogger('example.detail')

#log1.info('This is info message')
#log.debug('This is debug message')
#log.warn('Warning!!!')

# logging with different handler levels

logger = logging.getLogger(os.getlogin())
formatter = logging.Formatter(
    '%(asctime)s | %(name)s | %(levelname)s: %(message)s')
logger.setLevel(logging.DEBUG)


fh = logging.FileHandler(filename='output1.log',mode='a')
fh.setLevel(logging.WARNING)
fh.setFormatter(formatter)

sh = logging.StreamHandler()
sh.setLevel(logging.INFO)

logger.addHandler(fh)
logger.addHandler(sh)

logger.info('This is info message')
logger.debug('This is debug message')
logger.warning('Warning!!!')