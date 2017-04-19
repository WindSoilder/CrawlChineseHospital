from .HospitalSpider3A import HospitalSpider3A
from .HospitalSpider2A import HospitalSpider2A

class HospitalSpiderFactory:
    grade_to_spider = {
        '2': HospitalSpider2A,
        '3': HospitalSpider3A
    }

    @classmethod
    def create_hospital_spider(cls, grade_num, province_id):
        return cls.grade_to_spider.get(grade_num, HospitalSpider3A)(province_id)
        
