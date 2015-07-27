# ~/.venvs/Grab

from grab.spider import Spider, Task

class MakejarSpider(Spider):
    initial_urls = ['http://bit.makejar.com/']

    def task_initial(self, grab, task):
        print('Hello!')

        for elem in grab.doc.select('//*[@id="id_list"]//div[starts-with(@id, "id_f")]'):
            print(elem)
            print(elem.select('a').text())


if __name__ == '__main__':
    bot = MakejarSpider(thread_number=4)
    bot.run()
