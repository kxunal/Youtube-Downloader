from telegram.ext import Updater, CommandHandler, MessageHandler
from pytube import YouTube
from config import TOKEN


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='ʜᴇʟʟᴏ! ɪ ᴄᴀɴ ᴅᴏᴡɴʟᴏᴀᴅ ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏꜱ ꜰᴏʀ ʏᴏᴜ. ꜱᴇɴᴅ ᴍᴇ ᴀ ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏ ʟɪɴᴋ.')

def download_video(update, context):
    url = update.message.text
    try:
        yt = YouTube(url)
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
        context.bot.send_message(chat_id=update.effective_chat.id, text='ᴠɪᴅᴇᴏ ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ!')
        context.bot.send_document(chat_id=update.effective_chat.id, document=open(yt.title + '.mp4', 'rb'))
    except Exception as e:
        context.bot.send_message(chat_id=update.effective_chat.id, text='ꜰᴀɪʟᴇᴅ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ. ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ᴛʜᴇ ʟɪɴᴋ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ.')

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.regex(r'^https:\/\/www\.youtube\.com\/.*$'), download_video))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
