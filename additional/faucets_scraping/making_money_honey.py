from grab.spider import Spider, Task
import xlsxwriter


class MakingMoneyHoneySpider(Spider):
    initial_urls = ['http://makingmoneyhoney.com/bitcoinfaucets.php']

    def task_initial(self, grab, task):
        workbook = xlsxwriter.Workbook('makingmoneyhoney.xlsx')
        worksheet = workbook.add_worksheet()

        faucets = grab.doc.select('//*[@id="faucet-list"]/tbody/tr')
        print(len(faucets))

        worksheet.write(0, 0, 'title')
        worksheet.write(0, 1, 'link')
        worksheet.write(0, 2, 'min payout')
        worksheet.write(0, 3, 'max payout')
        worksheet.write(0, 4, 'avg per hour')
        worksheet.write(0, 5, 'category')
        worksheet.write(0, 6, 'cooldown')
        worksheet.write(0, 7, 'min withdraw')

        for idx, faucet in enumerate(faucets):
            worksheet.write(idx + 1, 0, faucet.select('td[1]/center/a').text())
            worksheet.write(idx + 1, 1, faucet.select('td[1]/center/a/@href').text())
            worksheet.write(idx + 1, 2, faucet.select('td[2]/center').text())
            worksheet.write(idx + 1, 3, faucet.select('td[3]/center').text())
            worksheet.write(idx + 1, 4, faucet.select('td[4]/center').text())
            worksheet.write(idx + 1, 5, faucet.select('td[5]/center').text())
            worksheet.write(idx + 1, 6, faucet.select('td[6]/center').text())
            worksheet.write(idx + 1, 7, faucet.select('td[7]/center').text())

        workbook.close()


if __name__ == '__main__':
    bot = MakingMoneyHoneySpider(thread_number=4)
    bot.run()
