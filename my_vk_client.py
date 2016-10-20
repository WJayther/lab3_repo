import VK_get_id
import VK_parser
from datetime import datetime
import matplotlib.pyplot as plt


class MatPlotParser(VK_parser.ParseFriends):
    #returns list of ages for matplotlib histogram
    def response_handler(self, response):
        friends = response.json()['response']
        hist_list = list()
        for friend in friends:
            if 'bdate' in friend and friend['bdate'].count('.')==2:
                bdate = datetime.strptime(friend['bdate'], "%d.%m.%Y")
                curdate = datetime.now()
                years = self.count_age(bdate, curdate)
                hist_list.append(years)
        return hist_list


if __name__ == '__main__':
    str_id = input('Type some ID: ')
    test = VK_get_id.GetIDFromUsername(str_id)
    uid = test.execute()
    test = VK_parser.ParseFriends(uid)
    print(test.execute())
    test = MatPlotParser(uid)
    ages = test.execute()
    #time to get rid of seniles
    ages = list(filter(lambda x: x > 0 and x < 100, ages))
    bins = max(ages)-min(ages)+1
    
    fig, ax0 = plt.subplots(ncols=1, figsize=(8, 4))

    ax0.hist(ages, bins, facecolor='#ff8000', alpha=0.75)
    ax0.set_title(str_id+'\'s friends ages')

    plt.tight_layout()
    plt.show()
