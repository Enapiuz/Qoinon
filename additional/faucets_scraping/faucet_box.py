from grab import Grab
from grab.spider import Spider, Task
import xlsxwriter
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

    def create_grab_instance(self, **kwargs):
        g = Grab(**kwargs)
        g.setup(follow_location=True)
        return g

    def task_initial(self, grab, task):
        self.workbook = xlsxwriter.Workbook('faucetbox.xlsx')
        self.worksheet = self.workbook.add_worksheet()

        faucets = grab.doc.select('//*[@id="faucets-list"]/tbody/tr')
        print(len(faucets))

        self.worksheet.write(0, 0, 'currency')
        self.worksheet.write(0, 1, 'title')
        self.worksheet.write(0, 2, 'link')
        self.worksheet.write(0, 3, 'cooldown')
        self.worksheet.write(0, 4, 'description')
        self.worksheet.write(0, 5, 'max payout')
        self.worksheet.write(0, 6, 'avg daily payout')

        for idx, faucet in enumerate(faucets):
            self.worksheet.write(idx+1, 0, self.get_currency(grab))  # currency
            self.worksheet.write(idx+1, 1, faucet.select('td[2]/a').text())  # title
            self.worksheet.write(idx+1, 3, faucet.select('td[3]').text())  # cooldown
            self.worksheet.write(idx+1, 4, faucet.select('td[4]').text())  # description
            self.worksheet.write(idx+1, 5, faucet.select('td[5]').text())  # max pay
            self.worksheet.write(idx+1, 6, faucet.select('td[6]').text())  # avg
            yield Task('urls', url='https://faucetbox.com/en/' + unquote(faucet.select('td[2]/a/@href').text()), idx=idx)

    def task_urls(self, grab, task):
        self.worksheet.write(task.idx+1, 2, grab.response.url)

    def get_currency(self, grab):
        return grab.response.url.rsplit('/', 1)[-1]


if __name__ == '__main__':
    bot = FaucetBoxSpider(thread_number=2)
    bot.run()
    bot.workbook.close()
