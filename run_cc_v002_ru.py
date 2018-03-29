# -*- coding: utf-8 -*-

#import'ы, которые гарантированно сработают
import os
import time
import json
import random
import smtplib
import datetime

#жизненно важная информация
__author__ = 'Elisey Sharov aka ZerZ™(or ZerZru)'
version = '0.0.2'
program_language = 'python'
game_language = 'russian'
country = 'Russian Federation'
license = 'GNU GPL 3.0'
path_version = '0.3'

#try:
	#проверка наличия DLC у пользователя
#	import DLC
#	import DLC_Lada
#	import DLC_Audi
#	import DLC_Skoda
#	import DLC_BMW
#	import DLC_Nissan
#	import DLC_Toyota
#	import DLC_F1
#	print('Обнаружены DLC')
#except:
#	print('DLC не обнаружены. Вы можете приоберсти их на официальном сайте.')

global money
global count_cars
count_cars = int('0')
money = int('1000')

try:
	with open('save.json', 'r') as fh:
		data = json.load(fh)
		nickname = data['nickname']
		company = data['company']
		workshop = data['workshop']
		money = data['money']
	print('Обнаружен файл сохранения. Ник(имя): {}, название компании: {}, название мастерской: {}, капитал: {}$'.format(nickname, company, workshop, money))
except:
	nickname = input('Введите имя(или ник): ')
	company = input('Введите название компании: ')

try:
	#проверка запуска игры для дальнейшео написания в лог
	now = datetime.datetime.now()
	def logs(filename, content, mode='a'):
			#print('New log has been added!')
			with open(filename, mode=mode) as f:
				f.write(content)
	logs('log.txt', now.strftime("[%d-%m-%Y %H:%M] Game has been run. Nickname: {}, company: {}, money: {}. \n".format(nickname, company, money)))

	def details():
		print('Список доступных деталей для версии 0.0.1: ')
		print('Двигатели: \n 1) Мотор 2101 "Копейка" \n 2) Мотор ВАЗ 2103 \n 3) Мотор ВАЗ 2106 \n 4) Мотор ВАЗ 21083 \n 5) Мотор ВАЗ 2111 \n 6) Двигатель КАМАЗ 43101 \n 7) Двигатель КАМАЗ 55111 \n 8) Двигатель КАМАЗ 55111 \n 9) Двигатель КАМАЗ 43114 \n 10) Двигатель КАМАЗ 4925 \n 11) Двигатель КАМАЗ 6520 \n 12) 4A-FE \n 13) 4E-GE 16V \n 14) 8A-FE \n 15) 7A-FE LB \n 16) Alfa Romeo V6 Busso')
		print('Салоны: \n 1) Кожанный \n 2) Советский классический \n 3) Деревянный')
		print('Колёса: \n 1) Стальные \n 2) Michelin \n 3) Золотые GTA')
		return None

	def ghelp():
		print('1) Вызвать help: ghelp() \n 2) Узнать, как зарабатывать: how_get_a_money() \n 3) Создать новую машину: new_car() \n 4) Узнать названия деталей, доступных на данный момент: details() \n 5) Найти работу: works() \n 6) Выйти из игры с сохранением всех данных: gquit() \n 7) Узнать, как создавать автомобиль: how_create_a_auto() \n 8) Почта для ваших сообщений: mail() \n 9) Узнать про конкурентов: competitors() \n 10) Взлом серверов: virus() \n 11) Тех.поддержка: support() \n 12) Сохраненить прогресс: save() \n 13) Сбросить прогресс: clear() \n 14) Помочь материально: money_help() \n')
		return None

	def money_help():
		print('Вы хотите материально помочь? Огромное спасибо хотя бы за то, что посетили эту страницу! Материальная поддержка даёт мотивацию работать над программой, а значит, обновления и патчи будут выходить гораздо быстрее!')
		print('Яндекс.Денги: 410013018225939 \n Qiwi: +79889413270')
		print('Ещё раз огромное спасибо!')
		return None

	def save():
		print('Идёт сохранение данных, пожалуйста, подождите...')
		dict = {}
		dict['nickname'] = nickname
		dict['company'] = company
		dict['money'] = money
		with open('save.json', mode='w') as f:
			json.dump(dict, f)
		time.sleep(5)
		print('Данные сохранены.')
		return None

	def gquit():
		print('Вы собираетесь выйти из игры. Идёт сохранение данных. Пожалуйста, подождите...')
		dict = {}
		dict['nickname'] = nickname
		dict['company'] = company
		dict['workshop'] = workshop
		dict['money'] = money
		with open('save.json', mode='w') as f:
			json.dump(dict, f)
		time.sleep(5)
		quit()
		return None

	def how_get_a_money():
		print('1) Продавать автомобили: самый дорогостоящий способ, но очень прибыльный. \n 2) Быть на работе: самый долгий способ: чтобы накопить 1000$, потребуется около 20 минут(если вы на самой престижной работе). На работе средне-низкого уровня понадобится от часа и более.')
		# 3) Оставить игру в фоне. За каждый час, проведённый в игре, даётся 100$
		return None

	def competitors():
		print('Мы решили усложнить игру, потому что иначе она была бы слишком лёгкая и быстро потеряет интерес. Конкуренты - ваши враги. Они могут влиять на продажи ваших автомобилей, влиять на ценообразование и популярность вашей компании. Единственный способ их победить - это взломать их сервера. Более подробно можно узнать, написав virus(). Удачи с захватом рынка!')
		pass

	def virus():
		global servers_hacked
		servers_hacked = int('0')
		print('Вы хотите достать данные из базы данных ваших конкурентов? Довольно смелый шаг. Выберите из списка ниже конкурента, которого вы хотите взломать. Взлом может обойтись вам очень дорого, так что сначала всё обдумайте, прежде чем приступать.')
		print('1) BMW \n 2) Audi \n 3) Lada \n 4) Skoda \n 5) Nissan \n 6) Toyota \n 7) Subaru')
		a_v = input('Введите название компании: ')
		c_1 = 'BMW'
		c_2 = 'Audi'
		c_3 = 'Lada'
		c_4 = 'Skoda'
		c_5 = 'Nissan'
		c_6 = 'Toyota'
		c_7 = 'Subaru'

		if a_v == c_1:
			a_v_c = input('Вы решили взломать базу данных BMW. Так как это крупная немецкая компания, взлом может обойтись вам штрафом в 5000$. Вы уверены? (Да/Нет): ')
			yes = 'Да'
			no = 'Нет'
			if a_v_c == yes:
				print('Вы подтвердили свой выбор. Если вашу попытку взлома заметят, с вашего счёта будет списано 5000$. Если у вас не будет такой суммы, вы проиграете.')
				print('Подождите, идёт попытка взлома...') #15 секунд
				time.sleep(15)
				res = int(random.randint(0, 1))
				if res == int('0'):
					print('Попытка взлома не удалась. Обнаружили ли вашу попытку? Реакцию узнаем через 10 секунд...')
					time.sleep(10)
					reaction = int(random.randint(2, 3))
					if reaction == int('2'):
						print('Вашу попытку обнаружили. С вашего счёта было списано 5000$')
						count = int('5000')
						if money > count:
							count_res = money - count
							print('У вас осталось {} долларов.'.format(count_res))
						elif money < count:
							print('Штраф оказался выше вашего капитала. Вы - банкрот. Сейчас мы сохраним ваши данные в файл result.txt и вы сможете посмотреть свою статистику. После сохранения игра закроется. Пожалуйста, подождите...')
							a1 = 'Причина проигрыша: попытка взлома. Статистика: ник(имя): {}, название компании: {}, капитал: {}. Удачи в следующий раз!'.format(nickname, company, money)
							time.sleep(10)
							quit()
						elif money == count:
							print('У вас закончились деньги. Вы можете пойти на работу и наверстать упущенное.')
							pass
					elif reaction == int('3'):
						print('Вам повезло. Вашу попытку не обнаружили. Можете спокойно дальше жить.')
						pass
				elif res == int('1'):
					print('Ваша попытка взлома удалась! \n...')
					time.sleep(2)
					try:
						from DLC_HackServer import server_hack
						print('DLC на автоматический взлом сервера обнаружен. Сейчас программа будет подбирать пароли.')
						server_hack()
					except:
						print('У вас отсутствует DLC на автоматический взлом сервера. Вам придётся найти пароль, а потом переписать его вручную. Приобрести DLC можно на сайте https://www.github.com/ZerZru/DLC/CarCreator/')
						from alternate_hack import server_hack
						server_hack()
					time.sleep(10)
					reaction = int(random.randint(2, 3))
					if reaction == int('2'):
						print('Вашу попытку обнаружили. С вашего счёта было списано 5000$')
						count = int('5000')
						if money > count:
							count_res = money - count
							print('У вас осталось {} долларов.'.format(count_res))
						elif money < count:
							print('Штраф оказался выше вашего капитала. Вы - банкрот. Сейчас мы сохраним ваши данные в файл result.txt и вы сможете посмотреть свою статистику. После сохранения игра закроется. Пожалуйста, подождите...')
							#сохранение результата в файл
							a1 = 'Причина проигрыша: штраф при взломе. Статистика: имя(ник): {}, название компании: {}, капитал: {}$. Удачи в следующий раз! \n'.format(nickname, company, money)
							f = open('result.txt', 'a')
							f.write(a1)
							f.close()
							path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'save.json')
							os.remove(path)
							time.sleep(10)
							quit()
						elif money == count:
							print('У вас закончились деньги. Вы можете пойти на работу и наверстать упущенное.')
							pass
					elif reaction == int('3'):
						print('Вам повезло. Вашу попытку не обнаружили. Можете спокойно дальше жить.')
						pass
			elif a_v_c == 'Нет':
				print('Вы решили не взламывать базу данных компании. Ваша совесть чиста.')
				pass

		if a_v == c_2:
			a_v_c = input('Вы решили взломать базу данных Audi. Так как это крупная немецкая компания, взлом может обойтись вам штрафом в 5000$. Вы уверены? (Да/Нет): ')
			yes = 'Да'
			no = 'Нет'
			if a_v_c == yes:
				print('Вы подтвердили свой выбор. Если вашу попытку взлома заметят, с вашего счёта будет списано 5000$. Если у вас не будет такой суммы, вы проиграете.')
				print('Подождите, идёт попытка взлома...') #15 секунд
				time.sleep(15)
				res = int(random.randint(0, 1))
				if res == int('0'):
					print('Попытка взлома не удалась. Обнаружили ли вашу попытку? Реакцию узнаем через 10 секунд...')
					time.sleep(10)
					reaction = int(random.randint(2, 3))
					if reaction == int('2'):
						print('Вашу попытку обнаружили. С вашего счёта было списано 5000$')
						count = int('5000')
						if money > count:
							count_res = money - count
							print('У вас осталось {} долларов.'.format(count_res))
						elif money < count:
							print('Штраф оказался выше вашего капитала. Вы - банкрот. Сейчас мы сохраним ваши данные в файл result.txt и вы сможете посмотреть свою статистику. После сохранения игра закроется. Пожалуйста, подождите...')
							a1 = 'Причина проигрыша: попытка взлома. Статистика: ник(имя): {}, название компании: {}, капитал: {}. Удачи в следующий раз!'.format(nickname, company, money)
							time.sleep(10)
							quit()
						elif money == count:
							print('У вас закончились деньги. Вы можете пойти на работу и наверстать упущенное.')
							pass
					elif reaction == int('3'):
						print('Вам повезло. Вашу попытку не обнаружили. Можете спокойно дальше жить.')
						pass
				elif res == int('1'):
					print('Ваша попытка взлома удалась! \n...')
					time.sleep(2)
					try:
						from DLC_HackServer import server_hack
						print('DLC на автоматический взлом сервера обнаружен. Сейчас программа будет подбирать пароли.')
						server_hack()
					except:
						print('У вас отсутствует DLC на автоматический взлом сервера. Вам придётся найти пароль, а потом переписать его вручную. Приобрести DLC можно на сайте https://www.github.com/ZerZru/DLC/CarCreator/')
						from alternate_hack import server_hack
						server_hack()
					time.sleep(10)
					reaction = int(random.randint(2, 3))
					if reaction == int('2'):
						print('Вашу попытку обнаружили. С вашего счёта было списано 5000$')
						count = int('5000')
						if money > count:
							count_res = money - count
							print('У вас осталось {} долларов.'.format(count_res))
						elif money < count:
							print('Штраф оказался выше вашего капитала. Вы - банкрот. Сейчас мы сохраним ваши данные в файл result.txt и вы сможете посмотреть свою статистику. После сохранения игра закроется. Пожалуйста, подождите...')
							#сохранение результата в файл
							a1 = 'Причина проигрыша: штраф при взломе. Статистика: имя(ник): {}, название компании: {}, капитал: {}$. Удачи в следующий раз! \n'.format(nickname, company, money)
							f = open('result.txt', 'a')
							f.write(a1)
							f.close()
							path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'save.json')
							os.remove(path)
							time.sleep(10)
							quit()
						elif money == count:
							print('У вас закончились деньги. Вы можете пойти на работу и наверстать упущенное.')
							pass
					elif reaction == int('3'):
						print('Вам повезло. Вашу попытку не обнаружили. Можете спокойно дальше жить.')
						pass
			elif a_v_c == 'Нет':
				print('Вы решили не взламывать базу данных компании. Ваша совесть чиста.')
				pass

		if a_v == c_3:
			a_v_c = input('Вы решили взломать базу данных Lada. Так как эта компания нужна только в России, взлом может обойтись вам штрафом всего лишь в 100$. Вы уверены? (Да/Нет): ')
			yes = 'Да'
			no = 'Нет'
			if a_v_c == yes:
				print('Вы подтвердили свой выбор. Если вашу попытку взлома заметят, с вашего счёта будет списано 100$. Если у вас не будет такой суммы, вы проиграете.')
				print('Подождите, идёт попытка взлома...') #15 секунд
				time.sleep(15)
				res = int(random.randint(0, 1))
				if res == int('0'):
					print('Попытка взлома не удалась. Обнаружили ли вашу попытку? Реакцию узнаем через 10 секунд...')
					time.sleep(10)
					reaction = int(random.randint(2, 3))
					if reaction == int('2'):
						print('Вашу попытку обнаружили. С вашего счёта было списано 100$')
						count = int('100')
						if money > count:
							count_res = money - count
							print('У вас осталось {} долларов.'.format(count_res))
						elif money < count:
							print('Штраф оказался выше вашего капитала. Вы - банкрот. Сейчас мы сохраним ваши данные в файл result.txt и вы сможете посмотреть свою статистику. После сохранения игра закроется. Пожалуйста, подождите...')
							a1 = 'Причина проигрыша: попытка взлома. Статистика: ник(имя): {}, название компании: {}, капитал: {}. Удачи в следующий раз!'.format(nickname, company, money)
							time.sleep(10)
							quit()
						elif money == count:
							print('У вас закончились деньги. Вы можете пойти на работу и наверстать упущенное.')
							pass
					elif reaction == int('3'):
						print('Вам повезло. Вашу попытку не обнаружили. Можете спокойно дальше жить.')
						pass
				elif res == int('1'):
					print('Ваша попытка взлома удалась! \n...')
					time.sleep(2)
					try:
						from DLC_HackServer import server_hack
						print('DLC на автоматический взлом сервера обнаружен. Сейчас программа будет подбирать пароли.')
						server_hack()
					except:
						print('У вас отсутствует DLC на автоматический взлом сервера. Вам придётся найти пароль, а потом переписать его вручную. Приобрести DLC можно на сайте https://www.github.com/ZerZru/DLC/CarCreator/')
						from alternate_hack import server_hack
						server_hack()
					time.sleep(10)
					reaction = int(random.randint(2, 3))
					if reaction == int('2'):
						print('Вашу попытку обнаружили. С вашего счёта было списано 100$')
						count = int('100')
						if money > count:
							count_res = money - count
							print('У вас осталось {} долларов.'.format(count_res))
						elif money < count:
							print('Штраф оказался выше вашего капитала. Вы - банкрот. Сейчас мы сохраним ваши данные в файл result.txt и вы сможете посмотреть свою статистику. После сохранения игра закроется. Пожалуйста, подождите...')
							#сохранение результата в файл
							a1 = 'Причина проигрыша: штраф при взломе. Статистика: имя(ник): {}, название компании: {}, капитал: {}$. Удачи в следующий раз! \n'.format(nickname, company, money)
							f = open('result.txt', 'a')
							f.write(a1)
							f.close()
							path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'save.json')
							os.remove(path)
							time.sleep(10)
							quit()
						elif money == count:
							print('У вас закончились деньги. Вы можете пойти на работу и наверстать упущенное.')
							pass
					elif reaction == int('3'):
						print('Вам повезло. Вашу попытку не обнаружили. Можете спокойно дальше жить.')
						pass
			elif a_v_c == 'Нет':
				print('Вы решили не взламывать базу данных компании. Ваша совесть чиста.')
				pass

		if a_v == c_4:
			a_v_c = input('Вы решили взломать базу данных Skoda. Так как это чешская компания, взлом может обойтись вам штрафом в 2500$. Вы уверены? (Да/Нет): ')
			yes = 'Да'
			no = 'Нет'
			if a_v_c == yes:
				print('Вы подтвердили свой выбор. Если вашу попытку взлома заметят, с вашего счёта будет списано 2500$. Если у вас не будет такой суммы, вы проиграете.')
				print('Подождите, идёт попытка взлома...') #15 секунд
				time.sleep(15)
				res = int(random.randint(0, 1))
				if res == int('0'):
					print('Попытка взлома не удалась. Обнаружили ли вашу попытку? Реакцию узнаем через 10 секунд...')
					time.sleep(10)
					reaction = int(random.randint(2, 3))
					if reaction == int('2'):
						print('Вашу попытку обнаружили. С вашего счёта было списано 2500$')
						count = int('2500')
						if money > count:
							count_res = money - count
							print('У вас осталось {} долларов.'.format(count_res))
						elif money < count:
							print('Штраф оказался выше вашего капитала. Вы - банкрот. Сейчас мы сохраним ваши данные в файл result.txt и вы сможете посмотреть свою статистику. После сохранения игра закроется. Пожалуйста, подождите...')
							a1 = 'Причина проигрыша: попытка взлома. Статистика: ник(имя): {}, название компании: {}, капитал: {}. Удачи в следующий раз!'.format(nickname, company, money)
							time.sleep(10)
							quit()
						elif money == count:
							print('У вас закончились деньги. Вы можете пойти на работу и наверстать упущенное.')
							pass
					elif reaction == int('3'):
						print('Вам повезло. Вашу попытку не обнаружили. Можете спокойно дальше жить.')
						pass
				elif res == int('1'):
					print('Ваша попытка взлома удалась! \n...')
					time.sleep(2)
					try:
						from DLC_HackServer import server_hack
						print('DLC на автоматический взлом сервера обнаружен. Сейчас программа будет подбирать пароли.')
						server_hack()
					except:
						print('У вас отсутствует DLC на автоматический взлом сервера. Вам придётся найти пароль, а потом переписать его вручную. Приобрести DLC можно на сайте https://www.github.com/ZerZru/DLC/CarCreator/')
						from alternate_hack import server_hack
						server_hack()
					time.sleep(10)
					reaction = int(random.randint(2, 3))
					if reaction == int('2'):
						print('Вашу попытку обнаружили. С вашего счёта было списано 5000$')
						count = int('2500')
						if money > count:
							count_res = money - count
							print('У вас осталось {} долларов.'.format(count_res))
						elif money < count:
							print('Штраф оказался выше вашего капитала. Вы - банкрот. Сейчас мы сохраним ваши данные в файл result.txt и вы сможете посмотреть свою статистику. После сохранения игра закроется. Пожалуйста, подождите...')
							#сохранение результата в файл
							a1 = 'Причина проигрыша: штраф при взломе. Статистика: имя(ник): {}, название компании: {}, капитал: {}$. Удачи в следующий раз! \n'.format(nickname, company, money)
							f = open('result.txt', 'a')
							f.write(a1)
							f.close()
							path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'save.json')
							os.remove(path)
							time.sleep(10)
							quit()
						elif money == count:
							print('У вас закончились деньги. Вы можете пойти на работу и наверстать упущенное.')
							pass
					elif reaction == int('3'):
						print('Вам повезло. Вашу попытку не обнаружили. Можете спокойно дальше жить.')
						pass
			elif a_v_c == 'Нет':
				print('Вы решили не взламывать базу данных компании. Ваша совесть чиста.')
				pass
		if a_v == c_5:
			a_v_c = input('Вы решили взломать базу данных Nissan. Так как это крупная японская компания, взлом может обойтись вам штрафом в 5700$. Вы уверены? (Да/Нет): ')
			yes = 'Да'
			no = 'Нет'
			if a_v_c == yes:
				print('Вы подтвердили свой выбор. Если вашу попытку взлома заметят, с вашего счёта будет списано 5700$. Если у вас не будет такой суммы, вы проиграете.')
				print('Подождите, идёт попытка взлома...') #15 секунд
				time.sleep(15)
				res = int(random.randint(0, 1))
				if res == int('0'):
					print('Попытка взлома не удалась. Обнаружили ли вашу попытку? Реакцию узнаем через 10 секунд...')
					time.sleep(10)
					reaction = int(random.randint(2, 3))
					if reaction == int('2'):
						print('Вашу попытку обнаружили. С вашего счёта было списано 5700$')
						count = int('5700')
						if money > count:
							count_res = money - count
							print('У вас осталось {} долларов.'.format(count_res))
						elif money < count:
							print('Штраф оказался выше вашего капитала. Вы - банкрот. Сейчас мы сохраним ваши данные в файл result.txt и вы сможете посмотреть свою статистику. После сохранения игра закроется. Пожалуйста, подождите...')
							a1 = 'Причина проигрыша: попытка взлома. Статистика: ник(имя): {}, название компании: {}, капитал: {}. Удачи в следующий раз!'.format(nickname, company, money)
							time.sleep(10)
							quit()
						elif money == count:
							print('У вас закончились деньги. Вы можете пойти на работу и наверстать упущенное.')
							pass
					elif reaction == int('3'):
						print('Вам повезло. Вашу попытку не обнаружили. Можете спокойно дальше жить.')
						pass
				elif res == int('1'):
					print('Ваша попытка взлома удалась! \n...')
					time.sleep(2)
					try:
						from DLC_HackServer import server_hack
						print('DLC на автоматический взлом сервера обнаружен. Сейчас программа будет подбирать пароли.')
						server_hack()
					except:
						print('У вас отсутствует DLC на автоматический взлом сервера. Вам придётся найти пароль, а потом переписать его вручную. Приобрести DLC можно на сайте https://www.github.com/ZerZru/DLC/CarCreator/')
						from alternate_hack import server_hack
						server_hack()
					time.sleep(10)
					reaction = int(random.randint(2, 3))
					if reaction == int('2'):
						print('Вашу попытку обнаружили. С вашего счёта было списано 5700$')
						count = int('5700')
						if money > count:
							count_res = money - count
							print('У вас осталось {} долларов.'.format(count_res))
						elif money < count:
							print('Штраф оказался выше вашего капитала. Вы - банкрот. Сейчас мы сохраним ваши данные в файл result.txt и вы сможете посмотреть свою статистику. После сохранения игра закроется. Пожалуйста, подождите...')
							#сохранение результата в файл
							a1 = 'Причина проигрыша: штраф при взломе. Статистика: имя(ник): {}, название компании: {}, капитал: {}$. Удачи в следующий раз! \n'.format(nickname, company, money)
							f = open('result.txt', 'a')
							f.write(a1)
							f.close()
							path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'save.json')
							os.remove(path)
							time.sleep(10)
							quit()
						elif money == count:
							print('У вас закончились деньги. Вы можете пойти на работу и наверстать упущенное.')
							pass
					elif reaction == int('3'):
						print('Вам повезло. Вашу попытку не обнаружили. Можете спокойно дальше жить.')
						pass
			elif a_v_c == 'Нет':
				print('Вы решили не взламывать базу данных компании. Ваша совесть чиста.')
				pass
		if a_v == c_7:
			a_v_c = input('Вы решили взломать базу данных Toyota. Так как это крупная японская компания, взлом может обойтись вам штрафом в 4900$. Вы уверены? (Да/Нет): ')
			yes = 'Да'
			no = 'Нет'
			if a_v_c == yes:
				print('Вы подтвердили свой выбор. Если вашу попытку взлома заметят, с вашего счёта будет списано 4900$. Если у вас не будет такой суммы, вы проиграете.')
				print('Подождите, идёт попытка взлома...') #15 секунд
				time.sleep(15)
				res = int(random.randint(0, 1))
				if res == int('0'):
					print('Попытка взлома не удалась. Обнаружили ли вашу попытку? Реакцию узнаем через 10 секунд...')
					time.sleep(10)
					reaction = int(random.randint(2, 3))
					if reaction == int('2'):
						print('Вашу попытку обнаружили. С вашего счёта было списано 4900$')
						count = int('4900')
						if money > count:
							count_res = money - count
							print('У вас осталось {} долларов.'.format(count_res))
						elif money < count:
							print('Штраф оказался выше вашего капитала. Вы - банкрот. Сейчас мы сохраним ваши данные в файл result.txt и вы сможете посмотреть свою статистику. После сохранения игра закроется. Пожалуйста, подождите...')
							a1 = 'Причина проигрыша: попытка взлома. Статистика: ник(имя): {}, название компании: {}, капитал: {}. Удачи в следующий раз!'.format(nickname, company, money)
							time.sleep(10)
							quit()
						elif money == count:
							print('У вас закончились деньги. Вы можете пойти на работу и наверстать упущенное.')
							pass
					elif reaction == int('3'):
						print('Вам повезло. Вашу попытку не обнаружили. Можете спокойно дальше жить.')
						pass
				elif res == int('1'):
					print('Ваша попытка взлома удалась! \n...')
					time.sleep(2)
					try:
						from DLC_HackServer import server_hack
						print('DLC на автоматический взлом сервера обнаружен. Сейчас программа будет подбирать пароли.')
						server_hack()
					except:
						print('У вас отсутствует DLC на автоматический взлом сервера. Вам придётся найти пароль, а потом переписать его вручную. Приобрести DLC можно на сайте https://www.github.com/ZerZru/DLC/CarCreator/')
						from alternate_hack import server_hack
						server_hack()
					time.sleep(10)
					reaction = int(random.randint(2, 3))
					if reaction == int('2'):
						print('Вашу попытку обнаружили. С вашего счёта было списано 4900$')
						count = int('4900')
						if money > count:
							count_res = money - count
							print('У вас осталось {} долларов.'.format(count_res))
						elif money < count:
							print('Штраф оказался выше вашего капитала. Вы - банкрот. Сейчас мы сохраним ваши данные в файл result.txt и вы сможете посмотреть свою статистику. После сохранения игра закроется. Пожалуйста, подождите...')
							#сохранение результата в файл
							a1 = 'Причина проигрыша: штраф при взломе. Статистика: имя(ник): {}, название компании: {}, капитал: {}$. Удачи в следующий раз! \n'.format(nickname, company, money)
							f = open('result.txt', 'a')
							f.write(a1)
							f.close()
							path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'save.json')
							os.remove(path)
							time.sleep(10)
							quit()
						elif money == count:
							print('У вас закончились деньги. Вы можете пойти на работу и наверстать упущенное.')
							pass
					elif reaction == int('3'):
						print('Вам повезло. Вашу попытку не обнаружили. Можете спокойно дальше жить.')
						pass
			elif a_v_c == 'Нет':
				print('Вы решили не взламывать базу данных компании. Ваша совесть чиста.')
				pass
		if a_v == c_6:
			a_v_c = input('Вы решили взломать базу данных Toyota. Так как это крупная немецкая компания, взлом может обойтись вам штрафом в 5900$. Вы уверены? (Да/Нет): ')
			yes = 'Да'
			no = 'Нет'
			if a_v_c == yes:
				print('Вы подтвердили свой выбор. Если вашу попытку взлома заметят, с вашего счёта будет списано 5900$. Если у вас не будет такой суммы, вы проиграете.')
				print('Подождите, идёт попытка взлома...') #15 секунд
				time.sleep(15)
				res = int(random.randint(0, 1))
				if res == int('0'):
					print('Попытка взлома не удалась. Обнаружили ли вашу попытку? Реакцию узнаем через 10 секунд...')
					time.sleep(10)
					reaction = int(random.randint(2, 3))
					if reaction == int('2'):
						print('Вашу попытку обнаружили. С вашего счёта было списано 5900$')
						count = int('5900')
						if money > count:
							count_res = money - count
							print('У вас осталось {} долларов.'.format(count_res))
						elif money < count:
							print('Штраф оказался выше вашего капитала. Вы - банкрот. Сейчас мы сохраним ваши данные в файл result.txt и вы сможете посмотреть свою статистику. После сохранения игра закроется. Пожалуйста, подождите...')
							a1 = 'Причина проигрыша: попытка взлома. Статистика: ник(имя): {}, название компании: {}, капитал: {}. Удачи в следующий раз!'.format(nickname, company, money)
							time.sleep(10)
							quit()
						elif money == count:
							print('У вас закончились деньги. Вы можете пойти на работу и наверстать упущенное.')
							pass
					elif reaction == int('3'):
						print('Вам повезло. Вашу попытку не обнаружили. Можете спокойно дальше жить.')
						pass
				elif res == int('1'):
					print('Ваша попытка взлома удалась! \n...')
					time.sleep(2)
					try:
						from DLC_HackServer import server_hack
						print('DLC на автоматический взлом сервера обнаружен. Сейчас программа будет подбирать пароли.')
						server_hack()
					except:
						print('У вас отсутствует DLC на автоматический взлом сервера. Вам придётся найти пароль, а потом переписать его вручную. Приобрести DLC можно на сайте https://www.github.com/ZerZru/DLC/CarCreator/')
						from alternate_hack import server_hack
						server_hack()
					time.sleep(10)
					reaction = int(random.randint(2, 3))
					if reaction == int('2'):
						print('Вашу попытку обнаружили. С вашего счёта было списано 5900$')
						count = int('5900')
						if money > count:
							count_res = money - count
							print('У вас осталось {} долларов.'.format(count_res))
						elif money < count:
							print('Штраф оказался выше вашего капитала. Вы - банкрот. Сейчас мы сохраним ваши данные в файл result.txt и вы сможете посмотреть свою статистику. После сохранения игра закроется. Пожалуйста, подождите...')
							#сохранение результата в файл
							a1 = 'Причина проигрыша: штраф при взломе. Статистика: имя(ник): {}, название компании: {}, капитал: {}$. Удачи в следующий раз! \n'.format(nickname, company, money)
							f = open('result.txt', 'a')
							f.write(a1)
							f.close()
							path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'save.json')
							os.remove(path)
							time.sleep(10)
							quit()
						elif money == count:
							print('У вас закончились деньги. Вы можете пойти на работу и наверстать упущенное.')
							pass
					elif reaction == int('3'):
						print('Вам повезло. Вашу попытку не обнаружили. Можете спокойно дальше жить.')
						pass
			elif a_v_c == 'Нет':
				print('Вы решили не взламывать базу данных компании. Ваша совесть чиста.')
				pass
				
	def works():
		print('Выберете интересующую вас работу: \n 1) Подметать дворы \n 2) Мыть автомобили \n 3) "Свободная касса" \n 4) Получить образование(недоступно)')
		class work:
			w1 = int('1') #10$
			w2 = int('2') #15$
			w3 = int('3') #30$
			#w4 = print('Чтобы получить образование, введите ptu()') #поняли, типо функция ПТУ называется
			a = int(input('Введите номер: '))
			if a == w1:
				print('Вы захотели подметать дворы. За эту работу вам заплатят 10$ по истечении 5 минут')
				time.sleep(10)
				print('Вы закончили работу.') #в тестовой версии время снижено до 10 секунд 
				global money
				money = money + int('10')
				print('Вы заработали 10 доллара(ов)! Состояние вашего счёта: {} долларов'.format(money))
			elif a == w2:
				print('Вы захотели мыть автомобили. За эту работу вам заплатят 15$ по истечении 10 минут') #в тестовой версии время снижено до 15 секунд
				time.sleep(15)
				print('Вы закончили работу.')
				money = money + int('15')
				print('Вы заработали 15 доллара(ов)! Состояние вашего счёта: {} долларов'.format(money))
			elif a ==w3:
				print('Вы захотели быть кассиром. За эту работу вам заплатят 30$ по истечении 20 минут')  #в тестовой версии время снижено до 20 секунд
				time.sleep(20)
				print('Вы закончили работу.')
				money = money + int('30')
				print('Вы заработали 30 доллара(ов)! Состояние вашего счёта: {} долларов'.format(money))
			else:
				print('Вы ввели неправильный номер. Попробуйте снова или напишите мне, если у вас есть идея для моего проекта.')
				work()
		return None

#	def ptu():
#		print('Вы решили получить о образование.')

	def clear():
		a = input('Вы действительно хотите удалить файл сохранения? (Да/Нет): ')
		path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'save.json')
		yes = 'Да'
		no = 'Нет'
		if a == yes:
			try:
				os.remove(path)
				print('Ваш файл сохранения был удалён')
			except:
				print('Файл сохранения не был удалён. Возможно, его уже нет.')
		elif a == no:
			print('Вы решили не удалять файл сохранения.')		
		return None

	def how_create_a_auto():
		print('Добро пожаловать в мануал по созданию автомобиля!')
		print('Начало работы: \n При запуске функции new_car(), вам предложат дать название для вашей мастерской. Если название будет занято, вам придётся ввести другое значение. После создания мастерской вам предложат дать название, номер и ID автомобилю. Это делается для создания коллекции и истории ваших автомобилей: ваш игровой путь наверх. После создания паспорта автомобиля, вы перейдёте к технической части. \n Техническая часть \n В версии 0.0.2 доступны 3 типа деталей: двигатель, салон и колёса. К двигателю представлено 16 деталей, к салону и колёсам - 3. Узнать список и названия деталей можно, введя details(). Итак: вам предложат ввести названия для 3 типов деталей. После обработки паспорт автомобиля обновится: в нём будут указаны ID, номер, название модели и комплектующие. Вы можете выкинуть паспорт и создать новую машину, либо принять изменения и выпустить автомобиль. После подтверждения вам предложать написать чисто автомобилей, которое вы хотите выпустить. После выпуска вам на счёт будут поступать деньги. И на этом пока что всё закончится, поэтому вы должны ждать обновлений. Вы можете помочь выпуску обновлений, если будете поддеживать меня материально. Подробнее: money_help(). Спасибо, что играете в CarCreator!')
		return None

	def mail():
		print('Почта для ваших предложений: scg-publicmail@yandex.ru')
		pass

	def support():
		print('Если у вас техническая проблема, какая-то функция не работает или у вас есть другой вопрос или предложение, вы можете написать нам на почту(введите функцию mail()) или используйте данную форму. Если у эта форма вам не подходит, посетите scgofficial.esy.es/GitHub/#support.')
		a1 = input('Введите ваш вопрос. Пожалуйста, указывайте любую информацию, которая нам поможет решить вашу проблему. На почту желательно отправлять файл log.txt и скриншоты ошибки. Итак: ')
		f = open('question.txt', 'w')
		f.write(a1)
		f.close()
		print('Ваш вопрос записан в файл question.txt. Пожалуйста, отправьте его на нашу почту. Узнать её можно, написав mail()')
		pass
		
	def new_car():
		global workshop
		global count_cars
		count_cars = int('0')
		try:
			with open('save.json', 'r') as fh:
				data = json.load(fh)
				workshop = data['workshop']
		except:
			workshop = input('Введите название для мастерской: ')
		w1 = 'Steam'
		while workshop == w1:
			print('Это название уже занято или является зарегистрированным товарным знаком')
			workshop = input('Введите название для мастерской: ')
		print('Добро пожаловать в мастерскую {}! Прочитайте мануал по созданию автомобилей, если вы этого ещё не сделали.'.format(workshop))
		car_name = input('Введите название модели: ')
		car_name_ver = int(input('Введите номер автомобиля: '))
		car_id = int(input('Введите ID автомобиля: '))
		print('Вы создали автомобиль с ID: {}, названием {} и номером {}. Теперь давайте начнём собирать автомобиль!'.format(car_id, car_name, car_name_ver))
		engine = input('Введите двигатель: ')
		salon = input('Введите салон: ')
		wheel = input('Введите колёса: ')
		e1 = 'Мотор 2101 "Копейка"'
		e2 = 'Мотор ВАЗ 2103'
		e3 = 'Мотор ВАЗ 2106'
		e4 = 'Мотор ВАЗ 21083'
		e5 = 'Мотор ВАЗ 2111'
		e6 = 'Двигатель КАМАЗ 43101'
		e7 = 'Двигатель КАМАЗ 55111'
		e8 = 'Двигатель КАМАЗ 43114'
		e9 = 'Двигатель КАМАЗ 4925'
		e10 = 'Двигатель КАМАЗ 6520'
		e11 = '4A-FE'
		e12 = '4E-GE 16V'
		e13 = '8A-FE'
		e14 = '7A-FE LB'
		e15 = 'Alfa Romeo V6 Busso'
		e16 = 'Alfa Romeo V6 Busso'
		s1 = 'Кожанный'
		s2 = 'Советский классический'
		s3 = 'Деревянный'
		w1 = 'Стальные'
		w2 = 'Michelin'
		w3 = 'Золотые GTA'
		if engine == e1:
			e_input = 'Мотор ВАЗ 2101 "Копейка"'
		elif engine == e2:
			e_input = 'Мотор ВАЗ 2103'
		elif engine == e3:
			e_input = 'Мотор ВАЗ 2106'
		elif engine == e4:
			e_input = 'Мотор ВАЗ 21083'
		elif engine == e5:
			e_input = 'Мотор ВАЗ 2111'
		elif engine == e6:
			e_input = 'Двигатель КАМАЗ 43101'
		elif engine == e7:
			e_input = 'Двигатель КАМАЗ 55111'
		elif engine == e8:
			e_input = 'Двигатель КАМАЗ 43114'
		elif engine == e9:
			e_input = 'Двигатель КАМАЗ 4925'
		elif engine == e10:
			e_input = 'Двигатель КАМАЗ 6520'
		elif engine == e11:
			e_input = '4A-FE'
		elif engine == e12:
			e_input = '4E-GE 16V'
		elif engine == e13:
			e_input = '8A-FE'
		elif engine == e14:
			e_input = '7A-FE LB'
		elif engine == e15:
			e_input = 'Alfa Romeo V6 Busso'
		elif engine == e16:
			e_input = 'Alfa Rome v6 Busso'
		else:
			print('В базе данных не найдены совпадения с вашей деталью. Проверьте правильность введения детали или предлоэите её добавить. Узнать почту для предложений можно, введя mail()')
			engine = input('Введите двигатель: ')
			pass
		if salon == s1:
			s_input = 'Кожанный'
		elif salon == s2:
			s_input = 'Советский классический'
		elif salon == s3:
			s_input = 'Деревянный'
		else:
			print('В базе данных не найдены совпадения с вашей деталью. Проверьте правильность введения детали или предлоэите её добавить. Узнать почту для предложений можно, введя mail()')
			salon = input('Введите салон: ')
			pass
		if wheel == w1:
			w_input = 'Стальные'
		elif wheel == w2:
			w_input = 'Michelin'
		elif wheel == w3:
			w_input = 'Золотые GTA'
		else:
			print('В базе данных не найдены совпадения с вашей деталью. Проверьте правильность введения детали или предлоэите её добавить. Узнать почту для предложений можно, введя mail()')
			wheel = input('Введите колёса: ')
			pass
		global money
		car_points = int('0')
		car_points_engine = int('0')
		car_points_salon = int('0')
		car_points_wheels = int('0')
		if e_input == e1:
			car_points_engine = car_points + int('1')
		elif e_input == e2:
			car_points_engine = car_points + int('1')
		elif e_input == e3:
			car_points_engine = car_points + int('2')
		elif e_input == e4:
			car_points_engine = car_points + int('2')
		elif e_input == e5:
			car_points_engine = car_points + int('3')
		elif e_input == e6:
			car_points_engine = car_points + int('3')
		elif e_input == e7:
			car_points_engine = car_points + int('4')
		elif e_input == e8:
			car_points_engine = car_points + int('4')
		elif e_input == e9:
			car_points_engine = car_points + int('5')
		elif e_input == e10:
			car_points_engine = car_points + int('5')
		elif e_input == e11:
			car_points_engine = car_points + int('6')
		elif e_input == e12:
			car_points_engine = car_points + int('6')
		elif e_input == e13:
			car_points_engine = car_points + int('10')
		elif e_input == e14:
			car_points_engine = car_points + int('10')
		elif e_input == e15:
			car_points_engine = car_points + int('12')
		elif e_input == e16:
			car_points_engine = car_points + int('15')

		if s_input == s1:
			car_points_salon = car_points + int('10')
		elif s_input == s2:
			car_points_salon = car_points + int('3')
		elif e_input == s3:
			car_points_salon = car_points + int('15')
		if w_input == w1:
			car_points_wheels = car_points + int('3')
		elif w_input == w2:
			car_points_wheels = car_points + int('5')
		elif e_input == w3:
			car_points_wheels = car_points + int('20')
		global result_car_points
		result_car_points = car_points_engine + car_points_salon + car_points_wheels
		print('Ваш автомобиль набрал {} очков!'.format(result_car_points))

		if e_input == e1:
			detail_engine_count = int('100')
		elif e_input == e2:
			detail_engine_count = int('100')
		elif e_input == e3:
			detail_engine_count = int('200')
		elif e_input == e4:
			detail_engine_count = int('200')
		elif e_input == e5:
			detail_engine_count = int('300')
		elif e_input == e6:
			detail_engine_count = int('300')
		elif e_input == e7:
			detail_engine_count = int('400')
		elif e_input == e8:
			detail_engine_count = int('400')
		elif e_input == e9:
			detail_engine_count = int('500')
		elif e_input == e10:
			detail_engine_count = int('500')
		elif e_input == e11:
			detail_engine_count = int('600')
		elif e_input == e12:
			detail_engine_count = int('600')
		elif e_input == e13:
			detail_engine_count = int('1000')
		elif e_input == e14:
			detail_engine_count = int('1000')
		elif e_input == e15:
			detail_engine_count = int('1200')
		elif e_input == e16:
			detail_engine_count = int('1500')

		if s_input == s1:
			detail_salon_count = int('1000')
		elif s_input == s2:
			detail_salon_count = int('300')
		if w_input == w1:
			detail_wheel_count = int('300')
		elif w_input == w2:
			detail_wheel_count = int('500')
		elif w_input == w3:
			detail_wheel_count = int('2000')
		end_count_car = detail_engine_count + detail_salon_count + detail_wheel_count
		number_car = int(input('Цена вашего автомобиля {}$. Состояние вашего счёта: {}$. Какое количество автомобилей вы хотите выпустить?: '.format(end_count_car, money)))
		count_car_of_number_car = end_count_car * number_car
		global budjet
		budjet = money - count_car_of_number_car
		print('Вы выпустили {} автомобилей общей стоимостью {}$. Остаток вашего бюджета: {}$'.format(number_car, count_car_of_number_car, budjet))

		def compilar_car():
			global money
			car_answer = input('Вы создали автомобиль с номером {}, ID {}, названием {}, двигателем {}, {} салоном и {} колёсами. Вы подтверждаете свой выбор? (Да/Нет): '.format(car_name_ver, car_id, car_name, e_input, s_input, w_input))
			yes = 'Да'
			no = 'Нет'
			if car_answer == yes:
				print('Ваша машина была выпущена. Ждём реакцию на неё 10 секунд...')
				rp_real = int(random.randint(0, 1000))
				time.sleep(10)
				global budjet
				earnings = rp_real - count_car_of_number_car
				money = budjet + rp_real
				if earnings == int('0'):
					print('Вы ведёте бизнес в 0. Прибыль равна затратам.')
				elif earnings < int('0'):
					print('Убыль: {}$'.format(earnings))
				elif earnings > int('0'):
					print('Прибыль: {}$'.format(earnings))
				print('Вы заработали {} доллара(ов)! Состояние вашего счёта: {} долларов.'.format(rp_real, money))
				a1 = 'Модель: {}, номер: {}, ID: {}. Заработано: {}$. Детали: колёса: {}, двигатель: {}, салон: {} \n'.format(car_name, car_name_ver, car_id, rp_real, w_input, e_input, s_input)
				f = open('cars.txt', 'a')
				f.write(a1)
				f.close()
				print('Статистика о вашей машине была записана в файл cars.txt')
				if money < int('0'):
					print('Вы потратили на автомобиль больше, чем вы имели денег. К сожалению, вы банкрот. Сейчас мы записываем вашу статистику в файл result.txt. Удачи в следующий раз.')
					a1 = 'Причина проигрыша: банкротство. Статистика: имя(ник): {}, название компании: {}, капитал: {}$. Удачи в следующий раз!'.format(nickname, company, money)
					f = open('result.txt', 'w')
					f.write(a1)
					f.close()
					path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'save.json')
					os.remove(path)
					quit()
			elif car_answer == no:
				money = money + budjet
				print('Вы выбросили проект на помойку. Ваше состояние: {}$'.format(money))
			else:
				print('Ваш вариант ответа не найден. Проверьте правильность ввода данных.')
				pass
		compilar_car()
		return None

except Exception as er:
	logs('log.txt', now.strftime("[%d-%m-%Y %H:%M] Game has been crashed. Check code or re-installing game. Maybe you write not-valid nick or name of company?\n"))
	logs('log.txt', er)