import copy
from .HospitalSpider import CommomHospitalSpider

class HospitalSpider2A(CommomHospitalSpider):
    '''
    A spider to crawl grade 2, class A hospital in Chinese
    '''
    query_dict = copy.deepcopy(CommomHospitalSpider.query_dict)
    query_dict['hgrade'] = '2'
