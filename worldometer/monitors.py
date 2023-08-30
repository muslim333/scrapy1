# scrapy_project/monitors.py

from spidermon import Monitor, monitors

class MyCustomMonitor(Monitor):
    @monitors.name("Check if items were scraped")
    def test_items_were_scraped(self):
        item_count = getattr(self.data.stats, 'item_scraped_count', 0)
        if item_count == 0:
            self.fail("No items were scraped.")
