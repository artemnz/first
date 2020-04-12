# -*- coding: utf-8 -*-
from horoscope import generate_prophecies
from datetime import datetime as dt

## получает Head и Body и оборачивает в тег HTML создавая тема самым страницу
def generate_page(head, body):
	page = f"""<html>
	{head}
	{body}
</html>"""
	return page

## Генерация тайтла. Где на вход получаем название, все это оборачиваем в тайтл, добавляем utf-8 и оборачиваем все в head
def generate_head(title):
	head = f"""<head>
	<meta charset='utf-8'>
		<title>
			{title}
		</title>
	</head>"""
	return head

## Генерация Боди. На вход получаем, заголовки и параграфы. И через цикл заводи все в боди.
def generate_body(header, paragraphs):
	body = f"""<h1>
			{header}
		</h1>"""
	for p in paragraphs:
		body = body + f"""
		<p>{p}</p>"""
	return f"""<body>
		{body}
		<hr>
		<a href="about.html"> О нас</a>
		&nbsp
		<a href="reliz.html"> О реализации </a>
	</body>"""

def generate_body_about(time, verbs):
	time = time.split(",")
	verbs = verbs.split(",")
	list_time = ""
	list_verbs = ""
	for t in time:
		list_time = list_time + f"<li>{t}</li>"
	
	for v in verbs:
		list_verbs = list_verbs + f"<li>{v}</li>"

	return f"""
	<body>
	<h1>О чем все это</h1>
	<img src = "2.png" width= 25%>
	<ul>Времена<ol>{list_time}</ol></ul>
	<ul>Глаголы<ol>{list_verbs}</ol></ul>
	</body>
	<hr>
	<a href="index.html"> Главная </a>"""

def save_page(title, header, paragraphs, output="index.html"):
	fp = open(output, "w", encoding="utf-8")
	today = dt.now().date()
	page = generate_page(
		head=generate_head(title),
		body=generate_body(header=header, paragraphs=paragraphs)
		)
	print(page, file=fp)
	fp.close()

def save_page_about(title, header, time, verbs, main, output="about.html"):
	fp = open(output, "w", encoding="utf-8")
	today = dt.now().date()
	page = generate_page(
		head = f"<head><meta charset='utf-8'><title>{title}</title></head>",
		body = generate_body_about(time = "Утром, Вечером, После обеда", verbs = "Остерегайтесь, Ожидайте")
		)
	print(page, file=fp)
	fp.close()	


today = dt.now().date()
save_page(
	title="Гороскоп на сегодня",
	header="Ваши предсказания на " + str(today),
	paragraphs=generate_prophecies(),
)

save_page_about(
	header = "Ваши предсказания на " + str(today),
	title = "О чем все это",
	time = "Утром, Вечером, После обеда",
	verbs = "Остерегайтесь, Ожидайте",
	main = 'index.html'
)