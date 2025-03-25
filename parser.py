import requests
import re

url = "https://tagildrama.ru"
url_afisha = "https://tagildrama.ru/afisha/"

html = requests.get(url_afisha).text

r_title = re.findall(r'<a href="/spektakli/[^"]+">([^<]+)</a>', html)
r_date_day = re.findall(r'<h2 class="font-title center">(\d+)</h2>', html)
r_date_month = re.findall(r'<p class="center">([^<]+)</p>', html)
r_weekday = re.findall(r'<div class="col s6 m6 xl2 day-time">\s*<p>([^<]+)</p>', html)
r_time = re.findall(
    r'<div class="col s6 m6 xl2 day-time">\s*<p>[^<]+</p>\s*<p>([^<]+)</p>', html
)
r_genre = re.findall(
    r'poster-info">\s*<h4[^>]+>\s*.*\s*.*h4>\s.*<p>([^<]+)</p>',
    html,
)
r_age = re.findall(r'<p class="bronze-color">([^<]+)</p>', html)
r_link = re.findall(r'<a href="(/spektakli/[^"]+)">', html)
r_ticket_link = re.findall(
    r'<a href="(/ticket/\d+)" class="waves-effect[^>]+>Купить билет</a>', html
)
r_price = re.findall(r"Купить билет</a>\s*<p>([^<]+)</p>", html)

with open("theater.txt", "w", encoding="utf-8") as f:
    for i in range(len(r_title)):
        f.write(
            f"{i+1}. Название: {r_title[i]}\n"
            f"Дата: {r_date_day[i]} {r_date_month[i]}\n"
            f"День недели: {r_weekday[i]}\n"
            f"Время: {r_time[i]}\n"
            f"Жанр: {r_genre[i]}\n"
            f"Возрастная категория: {r_age[i]}\n"
            f"Ссылка: {url + r_link[i]}\n"
            f"Цена: {r_price[i].strip()}\n"
            f"Купить: {url + r_ticket_link[i]}\n\n"
        )
