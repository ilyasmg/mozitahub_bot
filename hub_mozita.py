import json
import settings
import telegram
import logging
from pathlib import Path
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

###########
## UTILS ##
###########
def load_list_from_path(generic_path):
    return json.loads(open(generic_path).read()) if Path(generic_path).exists() else []

def load_dict_from_path(generic_path):
    return json.loads(open(generic_path).read()) if Path(generic_path).exists() else {}

###############
## SENTENCES ##
###############
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

###################
## COMMANDS HANDLER
###################
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text(frasi['start'], parse_mode=telegram.ParseMode.HTML)

def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def help_command(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text(frasi['help'], parse_mode=telegram.ParseMode.HTML)

def gruppi_command(update, context):
    """Send a message when the command /gruppi is issued."""
    update.message.reply_text(frasi['gruppi'], parse_mode=telegram.ParseMode.HTML)

def avvisi_command(update, context):
    """Send a message when the command /avvisi is issued."""
    update.message.reply_text(frasi['avvisi'], parse_mode=telegram.ParseMode.HTML)

def vademecum_command(update, context):
    """Send a message when the command /vademecum is issued."""
    update.message.reply_text(frasi['vademecum'], parse_mode=telegram.ParseMode.HTML)

def meeting_command(update, context):
    """Send a message when the command /meeting is issued."""
    update.message.reply_text(frasi['meeting'], parse_mode=telegram.ParseMode.HTML)

def supporto_command(update, context):
    """Send a message when the command /supporto is issued."""
    update.message.reply_text(frasi['supporto'], parse_mode=telegram.ParseMode.HTML)

def progetti_command(update, context):
    """Send a message when the command /progetti is issued."""
    update.message.reply_text(frasi['progetti'], parse_mode=telegram.ParseMode.HTML)

def feedback_command(update, context):
    """Send a message when the command /feedback is issued."""
    update.message.reply_text(frasi['feedback'], parse_mode=telegram.ParseMode.HTML)

def social_command(update, context):
    """Send a message when the command /social is issued."""
    update.message.reply_text(frasi['social'], parse_mode=telegram.ParseMode.HTML)

def info_command(update, context):
    """Send a message when the command /info is issued."""
    update.message.reply_text(frasi['info'], parse_mode=telegram.ParseMode.HTML)

def regolamento_command(update, context):
    """Send a message when the command /rules is issued."""
    update.message.reply_text(frasi['rules'], parse_mode=telegram.ParseMode.HTML)

############
## GROUPS ##
############
def home_command(update, context):
    """Send a message when the command /home is issued."""
    update.message.reply_text(frasi['home'], parse_mode=telegram.ParseMode.HTML)

def news_command(update, context):
    """Send a message when the command /news is issued."""
    update.message.reply_text(frasi['news'], parse_mode=telegram.ParseMode.HTML)

def developers_command(update, context):
    """Send a message when the command /developers is issued."""
    update.message.reply_text(frasi['developers'], parse_mode=telegram.ParseMode.HTML)

def l10n_command(update, context):
    """Send a message when the command /l10n is issued."""
    update.message.reply_text(frasi['l10n'], parse_mode=telegram.ParseMode.HTML)

def design_command(update, context):
    """Send a message when the command /design is issued."""
    update.message.reply_text(frasi['design'], parse_mode=telegram.ParseMode.HTML)

def iot_command(update, context):
    """Send a message when the command /iot is issued."""
    update.message.reply_text(frasi['iot'], parse_mode=telegram.ParseMode.HTML)


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
    dp.add_handler(CommandHandler("home", social_command))
    dp.add_handler(CommandHandler("news", social_command))
    dp.add_handler(CommandHandler("developers", social_command))
    dp.add_handler(CommandHandler("l10n", social_command))
    dp.add_handler(CommandHandler("design", social_command))
    dp.add_handler(CommandHandler("iot", social_command))

    # on noncommand i.e message - echo the message on Telegram
    # dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()