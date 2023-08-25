#[The keyboards file]

from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

#======


support = 't.me/CKAMADMiN'

def markup_main():
	"Function of return main markup"
	"Cancel markup"
	markup = InlineKeyboardMarkup(row_width=1)
	markup.row(InlineKeyboardButton(text="Купить 🥇", callback_data="buygold"), InlineKeyboardButton(text="Вывести 🥇", callback_data="vivodgold"))
	markup.row(InlineKeyboardButton(text="⚙️ Профиль", callback_data="profile"))
	markup.row(InlineKeyboardButton(text="⚙️ Курс голды", callback_data="golds"))

	markup.row(InlineKeyboardButton(text="💼 Поддержка", callback_data="support"))
	return markup

def exitmenu():
	"Function of return main markup"
	"Cancel markup"
	markup = InlineKeyboardMarkup(row_width=1)
	markup.row(InlineKeyboardButton(text="❌", callback_data="exit"))	
	return markup


def aadmin(user_id):
	"Function of return main markup"
	"Cancel markup"
	markup = InlineKeyboardMarkup(row_width=1)
	markup.row(InlineKeyboardButton(text="Баланс QiWi", callback_data="promo"))
	markup.row(InlineKeyboardButton(text="Нагрузка", callback_data="lite"))
	markup.row(InlineKeyboardButton(text="Заявки на выдачу", callback_data="start"))
	markup.row(InlineKeyboardButton(text="Статистика", callback_data="pro"))
	markup.row(InlineKeyboardButton(text="Рассылка", callback_data="super"))
	markup.row(InlineKeyboardButton(text="Перезагрузка серверов", callback_data="super"))
	markup.row(InlineKeyboardButton(text="Выдача серверов", callback_data="super"))

	markup.row(InlineKeyboardButton(text="❌", callback_data="exit"))

	return markup

def profile():
	"Function of return main markup"
	"Cancel markup"
	markup = InlineKeyboardMarkup(row_width=1)
	markup.row(InlineKeyboardButton(text="➕Пополнить баланс", callback_data="pay"))

	markup.row(InlineKeyboardButton(text="🏆Реферальная система", callback_data="reff"))
	markup.row(InlineKeyboardButton(text="❌", callback_data="exit"))


	return markup

def profilekey():
	"Function of return main markup"
	"Cancel markup"
	markup = InlineKeyboardMarkup(row_width=1)
	markup.row(InlineKeyboardButton(text="❌", callback_data="exitprofile"))


	return markup

def vivod():
	"Function of return main markup"
	"Cancel markup"
	markup = InlineKeyboardMarkup(row_width=1)
	markup.row(InlineKeyboardButton(text="✅", callback_data="a_"))


	return markup

def clients():

	markup = InlineKeyboardMarkup(row_width=1)
	markup.row(InlineKeyboardButton(text="Контакты", callback_data="contacts"))
	markup.row(InlineKeyboardButton(text='Условия использования', url='https://telegra.ph/Usloviya-ispolzovaniya-01-29'))
	markup.row(InlineKeyboardButton(text='Политика конфиденциальности', url='https://telegra.ph/Politika-konfidencialnosti-01-29-8'))
	markup.row(InlineKeyboardButton(text="❌", callback_data="exitc"))

	return markup

def supportMenu():

	markup = InlineKeyboardMarkup(row_width=1)
	markup.row(InlineKeyboardButton (text='Написать в поддержку', url=support))
	markup.row(InlineKeyboardButton(text="❌", callback_data="exit"))

	return markup


#=====