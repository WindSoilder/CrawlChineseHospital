class Filter:
    def __call__(self, item):
        '''
        The filter should check if item should be filtered
        if specific item is not match for requirement, return True
        '''
        raise NotImplementedError()
