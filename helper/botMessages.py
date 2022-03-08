#!/usr/bin/env python3


# Bot defined Messages
class BotMessage(object):
    common_text = "\n\n<u></u>"
    help_msg = f"<i>Just Send me any direct downloading link, and I will send you the file as telegram file.</i>{common_text}"
    start_msg = f"<b>Hi, I am URL_UploaderBot </b>\n{help_msg}"
    not_joined_community = f"<b>To use this bot, you need to Join our Channel and Group.</b>{common_text}"
    broadcast_failed = "<b>Broadcasting Message can`t be empty</b>"
    processing_url = "<i>Processing File</i>"
    starting_to_download = "<i>Starting to Upload the file.... Have Some Patience!!!</i>"
    unsuccessful_upload = f'Uploading went <b>failed</b>, Error...{common_text}'
    uploading_msg = "<b>File successfully downloaded Now uploading to Telegram.</b>"
    youtube_url = "<b>youtube videos not supported.</b>"
    telegramLimit = f"<b>It is more than limit of telegram.</b>"
    
