from bs4 import BeautifulSoup;
import requests

with open('home.html', 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    course_cards = soup.find_all('div', class_='card')
    for course in course_cards:
        course_name = course.h2.text
        course_price = course.button.text.split()[-1]
        print(f'{course_name}: {course_price}')