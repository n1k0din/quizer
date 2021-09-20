import argparse
import json

from bs4 import BeautifulSoup


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    args = parser.parse_args()

    html = ''
    with open(args.input_file) as f:
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

    output_file = args.input_file.replace('.html', '.json')
    with open(output_file, 'w') as f:
        json.dump(db, f)


if __name__ == '__main__':
    main()
