from photos.api import formatter, keys

class ImageResult(object):

    def __init__(self, item):
        self.data = item

    def get(self, attr, formatter=formatter.no_formatting):
        """
        Gets an attribute from the the result using the
        specified formatted function to process it
        """
        return formatter(self.data.get(attr))    

class ImageResults(object):

    def __init__(self, raw_results):
        self.results = raw_results[keys.RESULTS_KEY]
        self.total = self.results[keys.TOTAL_KEY]
        self.items = [r.pop() for r in self.results[keys.ITEMS_KEY]]

    def __iter__(self):
        for item in self.items:
            yield item

    def __len__(self):
        return len(self.items)
