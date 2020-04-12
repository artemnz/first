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
	</body>"""

def save_page(title, header, paragraphs, output="index.html"):
	fp = open(output, "w", encoding="utf-8")
	today = dt.now().date()
	page = generate_page(
		head=generate_head(title),
		body=generate_body(header=header, paragraphs=paragraphs)
		)
	print(page, file=fp)
	fp.close()


today = dt.now().date()
save_page(
	title="Гороскоп на сегодня",
	header="Что день " + str(today) + " готовит",
	paragraphs=generate_prophecies(),
)

