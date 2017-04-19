import copy
import json

from .HospitalSpider import CommomHospitalSpider
from ..item import HospitalInforItem

class HospitalSpider3A(CommomHospitalSpider):
    '''
    A spider to crawl grade 3, class A hospital in Chinese
    '''
    query_dict = copy.deepcopy(CommomHospitalSpider.query_dict)
    query_dict['hgrade'] = '1'
