class Pipeline:
    def __call__(self, item):
        '''
        pipeline will do something to the item, like output item to the console
        or save item to database, and these operation should be async..
        '''
        raise NotImplementedError()
