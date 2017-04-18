import logging

from .PipelineBase import Pipeline

class OutputToConsolePipeline(Pipeline):
    '''
    This pipeline will output the item information to console
    '''
    def __call__(self, item):
        print(item)
