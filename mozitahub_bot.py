# TODO: URGENTE! gestire i callback
# TODO: creare un nuovo database con le frasi che attualmente sono in JSON? (puo essere una buona idea, ma bisogna valutare)
# TODO: comando vademecum, in quanto prima i file erano salvati localmente in una cartella, bisogna inventarsi un modo per auto aggiornarli cosi non dobbiamo aggiornarli ogni volta
# TODO: gestire la parte admin
# TODO: modificare le stringhe -> togliere i nomi delle variabili li, aggiungerli nel codice (alcune parti non sono state sviluppate, occhio a cosa si modifica)

import json
import telegram
import logging
import settings
import DBManager
from pathlib import Path
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler

#########
# UTILS #
#########

version = "2.0.0"
last_updated = "27-10-2020"
next_meeting = "06-11-2020"

# run db-init if it is the first time / they do not exist
DBManager.populate_db()

#############
# SENTENCES #
#############
# loading sentences from file
if Path("frasi.json").exists():
    frasi = json.loads(open("frasi.json", encoding="utf8").read())
else:
    print("File frasi non presente.")
    exit()

# update bot
updater = Updater(settings.TOKEN, use_context=True)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


####################
# COMMANDS HANDLER #
####################
def start(update, context):
    """Send a message when the command /start is issued."""
    keyboard = [
        [InlineKeyboardButton(text=frasi["button_start"], callback_data='/help')],
        [InlineKeyboardButton(text=frasi["button_start2"], callback_data='/supporto')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(frasi['start'], parse_mode=telegram.ParseMode.HTML, reply_markup=reply_markup)


def help_command(update, context):
    """Send a message when the command /help is issued."""
    reply_markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=frasi["button_testo_gruppi"], callback_data='/gruppi'),
         InlineKeyboardButton(
             text=frasi["button_testo_social"], callback_data='/social'),
         InlineKeyboardButton(text=frasi["button_testo_supporto"], callback_data='/supporto')],

        [InlineKeyboardButton(text=frasi["button_testo_avvisi"], callback_data='/avvisi'),
         InlineKeyboardButton(
             text=frasi["button_testo_call"], callback_data='/meeting'),
         InlineKeyboardButton(text=frasi["button_testo_progetti_attivi"], callback_data='/progetti')],

        [InlineKeyboardButton(text=frasi["button_testo_vademecum"], callback_data='/vademecum'),
         InlineKeyboardButton(
             text=frasi["button_testo_regolamento"], callback_data='/regolamento'),
         InlineKeyboardButton(text=frasi["button_testo_info"], callback_data='/info')],
        [InlineKeyboardButton(text=frasi["button_feedback"],
                              callback_data='/feedback')],
    ])

    update.message.reply_text(frasi['help'], reply_markup=reply_markup, parse_mode=telegram.ParseMode.HTML)


def gruppi_command(update, context):
    """Send a message when the command /gruppi is issued."""

    reply_markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=frasi["button_testo_home"], url='https://t.me/joinchat/BCql3UMy26nl4qxuRecDsQ'),
         InlineKeyboardButton(text=frasi["button_testo_news"], url='https://t.me/mozItaNews')],
        [InlineKeyboardButton(text=frasi["button_testo_vog_div_volontario"],
                              url='https://t.me/joinchat/B1cgtEQAHkGVBTbI0XPd-A')],
        [InlineKeyboardButton(text=frasi["button_testo_developers"],
                              url='https://t.me/joinchat/B1cgtENXHcxd3jzFar7Kuw'),
         InlineKeyboardButton(text=frasi["button_testo_L10n"], url='https://t.me/mozItaL10n')],
        [InlineKeyboardButton(text=frasi["button_testo_design"], url='https://t.me/joinchat/B1cgtA7DF3qDzuRvsEtT6g'),
         InlineKeyboardButton(text=frasi["button_testo_iot"], url='https://t.me/joinchat/B1cgtEzLzr0gvSJcEicq1g')],
        [InlineKeyboardButton(
            text=frasi["button_mostra_help"], callback_data='/help')],
    ])

    update.message.reply_text(frasi['gruppi'], parse_mode=telegram.ParseMode.HTML, reply_markup=reply_markup)


def avvisi_command(update, context):
    """Send a message when the command /avvisi is issued."""
    reply_markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=frasi["button_avvisi"], callback_data="/avvisiOn"),
         InlineKeyboardButton(text=frasi["button_avvisi2"], callback_data="/avvisiOff")],
        [InlineKeyboardButton(
            text=frasi["button_mostra_help"], callback_data='/help')],
    ])

    update.message.reply_text(frasi['avvisi'], parse_mode=telegram.ParseMode.HTML, reply_markup=reply_markup)


def vademecum_command(update, context):
    """Send a message when the command /vademecum is issued."""
    update.message.reply_text(frasi['vademecum'], parse_mode=telegram.ParseMode.HTML)


def meeting_command(update, context):
    """Send a message when the command /meeting is issued."""
    reply_markup = InlineKeyboardMarkup(inline_keyboard=[
        # [InlineKeyboardButton(text=frasi["button_call"],
        # callback_data='/listacall')],
        [InlineKeyboardButton(text=frasi["button_vai_a_canale_youtube"],
                              url='https://www.youtube.com/channel/UCsTquqVS0AJxCf4D3n9hQ1w')],
        [InlineKeyboardButton(text=frasi["button_call2"],
                              callback_data='/prossimoMeeting')],
        [InlineKeyboardButton(
            text=frasi["button_mostra_help"], callback_data='/help')],
    ])
    update.message.reply_text(frasi['meeting'].format(next_meeting), parse_mode=telegram.ParseMode.HTML, reply_markup=reply_markup)


def supporto_command(update, context):
    """Send a message when the command /supporto is issued."""

    reply_markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=frasi["button_forum"],
                              url='https://forum.mozillaitalia.org/')],
        [InlineKeyboardButton(
            text=frasi["button_mostra_help"], callback_data='/help')],
    ])

    update.message.reply_text(frasi['supporto'], parse_mode=telegram.ParseMode.HTML, reply_markup=reply_markup)


def progetti_command(update, context):
    """Send a message when the command /progetti is issued."""
    # lets build project list for mozilla's projects...
    reply_markup = []

    # builds projects list from db
    for project in DBManager.mozilla_projects_list.all():
        reply_markup.append([InlineKeyboardButton(
            text=project['name'], url=project['link'])])

    reply_markup.append(back_to_menu_button(True))
    reply_markup = InlineKeyboardMarkup(inline_keyboard=reply_markup)

    update.message.reply_text(frasi['progetti'], parse_mode=telegram.ParseMode.HTML, reply_markup=reply_markup)

    # ...now it's the time of lunch
    reply_markup = []

    for project in DBManager.mozilla_italia_projects_list.all():
        reply_markup.append([InlineKeyboardButton(
            text=project['name'], url=project['link'])])

    reply_markup.append(back_to_menu_button(True))
    reply_markup = InlineKeyboardMarkup(inline_keyboard=reply_markup)

    update.message.reply_text(frasi['progetti_ita'], parse_mode=telegram.ParseMode.HTML, reply_markup=reply_markup)


def feedback_command(update, context):
    """Send a message when the command /feedback is issued."""
    update.message.reply_text(frasi['feedback'], parse_mode=telegram.ParseMode.HTML, reply_markup=back_to_menu_button())


def social_command(update, context):
    """Send a message when the command /social is issued."""
    reply_markup = []

    # builds social list from db
    for social in DBManager.social_list.all():
        reply_markup.append([InlineKeyboardButton(
            text=social['name'], url=social['link'])])

    reply_markup.append(back_to_menu_button(True))

    reply_markup = InlineKeyboardMarkup(inline_keyboard=reply_markup)
    update.message.reply_text(frasi['social'], parse_mode=telegram.ParseMode.HTML, reply_markup=reply_markup)


def info_command(update, context):
    """Send a message when the command /info is issued."""
    final_message = ""

    # builds dev list from db
    for person in DBManager.assistants_list.all():
        final_message += "- " + person['handler'] + "(" + person['username'] + ")" + "\n"

    update.message.reply_text(frasi['info'].format(version, last_updated) + "\n" + final_message, parse_mode=telegram.ParseMode.HTML,
                              reply_markup=back_to_menu_button())


def regolamento_command(update, context):
    """Send a message when the command /regolamento is issued."""
    reply_markup = []

    # builds social list from db
    for social in DBManager.social_list.all():
        reply_markup.append([InlineKeyboardButton(
            text=social['name'], url=social['link'])])

    reply_markup.append(back_to_menu_button(True))
    reply_markup = InlineKeyboardMarkup(inline_keyboard=reply_markup)

    update.message.reply_text(frasi['regolamento'], parse_mode=telegram.ParseMode.HTML, reply_markup=reply_markup)


##################
# GROUPS HANDLER #
##################
def home_command(update, context):
    """Send a message when the command /home is issued."""
    update.message.reply_text(frasi['home'], parse_mode=telegram.ParseMode.HTML, reply_markup=back_to_menu_button())


def news_command(update, context):
    """Send a message when the command /news is issued."""
    update.message.reply_text(frasi['news'], parse_mode=telegram.ParseMode.HTML, reply_markup=back_to_menu_button())


def developers_command(update, context):
    """Send a message when the command /developers is issued."""
    update.message.reply_text(frasi['developers'], parse_mode=telegram.ParseMode.HTML,
                              reply_markup=back_to_menu_button())


def l10n_command(update, context):
    """Send a message when the command /l10n is issued."""
    update.message.reply_text(frasi['l10n'], parse_mode=telegram.ParseMode.HTML, reply_markup=back_to_menu_button())


def design_command(update, context):
    """Send a message when the command /design is issued."""
    update.message.reply_text(frasi['design'], parse_mode=telegram.ParseMode.HTML, reply_markup=back_to_menu_button())


def iot_command(update, context):
    """Send a message when the command /iot is issued."""
    update.message.reply_text(frasi['iot'], parse_mode=telegram.ParseMode.HTML, reply_markup=back_to_menu_button())


def back_to_menu_button(*just_array: bool):
    """
    it defines "back to main menu" button
    :return: if True in params return the array, else by default it returns a InlineKeyboardMarkup
    """
    reply_markup = []
    back_button = [InlineKeyboardButton(text=frasi["button_mostra_help"], callback_data="/help")]

    if just_array:
        return back_button

    reply_markup.append(back_button)
    reply_markup = InlineKeyboardMarkup(inline_keyboard=reply_markup)
    return reply_markup


def manage_callback(update, context):
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()

    if query.data == "/help":
        # TODO: help_command must be issued in some way
        pass

# MAIN FUNCTION
def main():
    """Start the bot."""
    updater = Updater(settings.TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("gruppi", gruppi_command))
    dp.add_handler(CommandHandler("supporto", supporto_command))
    dp.add_handler(CommandHandler("avvisi", avvisi_command))
    dp.add_handler(CommandHandler("meeting", meeting_command))
    dp.add_handler(CommandHandler("progetti", progetti_command))
    dp.add_handler(CommandHandler("vademecum", vademecum_command))
    dp.add_handler(CommandHandler("regolamento", regolamento_command))
    dp.add_handler(CommandHandler("info", info_command))
    dp.add_handler(CommandHandler("feedback", feedback_command))
    dp.add_handler(CommandHandler("social", social_command))

    # Mozilla Telegram Groups
    dp.add_handler(CommandHandler("home", home_command))
    dp.add_handler(CommandHandler("news", news_command))
    dp.add_handler(CommandHandler("developers", developers_command))
    dp.add_handler(CommandHandler("l10n", l10n_command))
    dp.add_handler(CommandHandler("design", design_command))
    dp.add_handler(CommandHandler("iot", iot_command))

    updater.dispatcher.add_handler(CallbackQueryHandler(manage_callback))

    # on noncommand i.e message - echo the message on Telegram
    # dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()