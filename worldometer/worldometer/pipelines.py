import json

class CovidPipeline:
    def open_spider(self, spider):
        self.file = open('covid_data.json', 'w')
        self.file.write('[\n')
    
    def close_spider(self, spider):
        self.file.write('\n]')
        self.file.close()
    
    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + ",\n"
        self.file.write(line)
        return item
