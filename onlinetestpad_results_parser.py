import json

from bs4 import BeautifulSoup


def main():

    html = ''
    with open('onlinetestpad1.html') as f:
        for row in f:
            html = f'{html}{row.rstrip()}'

    db = []

    soup = BeautifulSoup(html, 'lxml')
    question_cards = soup.find_all('div', class_='otp-item-view-question')

    for question_card in question_cards:
        question = question_card.find('span', class_='qtext').text
        answers = [answer.text.strip() for answer in
            question_card.find_all('div', class_='item otp-row-1')]

        db.append(
            {
                'question': question,
                'answers': answers,
            }
        )

    with open('onlinetestpad1.json', 'w') as f:
        json.dump(db, f)


if __name__ == '__main__':
    main()
