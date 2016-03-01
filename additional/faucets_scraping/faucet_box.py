from grab import Grab
from grab.spider import Spider, Task
import csv
from urllib.parse import unquote


class FaucetBoxSpider(Spider):
    initial_urls = [
        'https://faucetbox.com/en/list/BTC',
        'https://faucetbox.com/en/list/LTC',
        'https://faucetbox.com/en/list/DOGE',
        'https://faucetbox.com/en/list/PPC',
        'https://faucetbox.com/en/list/XPM',
        'https://faucetbox.com/en/list/DASH',
    ]

    def prepare(self):
        self.counter = 0
        self.result_file = csv.writer(open('faucetbox.csv', 'w'), delimiter=';')

        self.result_file.writerow([
            'currency',
            'title',
            'link',
            'cooldown',
            'description',
            'max payout',
            'avg daily payout',
        ])

    def create_grab_instance(self, **kwargs):
        g = Grab(**kwargs)
        g.setup(follow_location=True)
        return g

    def task_initial(self, grab, task):
        faucets = grab.doc.select('//*[@id="faucets-list"]/tbody/tr')
        print(len(faucets))

        for faucet in faucets:
            data = (
                self.get_currency(grab),  # currency
                faucet.select('td[2]/a').text(),  # title
                faucet.select('td[3]').text(),  # cooldown
                faucet.select('td[4]').text(),  # description
                faucet.select('td[5]').text(),  # max pay
                faucet.select('td[6]').text()  # avg
            )

            yield Task('urls', url='https://faucetbox.com/en/' + unquote(faucet.select('td[2]/a/@href').text()),
                       faucet=data)

    def task_urls(self, grab, task):
        data = task.faucet + (grab.response.url,)
        self.result_file.writerow(list(data))

    def get_currency(self, grab):
        return grab.response.url.rsplit('/', 1)[-1]


if __name__ == '__main__':
    bot = FaucetBoxSpider(thread_number=4)
    bot.run()
