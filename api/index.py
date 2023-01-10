import configparser

from flask import Flask, abort, request
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from bloom import BLOOM

config = configparser.ConfigParser()
config.read_file(open("secret.cfg"))
line_bot_api = LineBotApi(config.get("LINE", "LINE_CHANNEL_ACCESS_TOKEN"))
line_handler = WebhookHandler(config.get("LINE", "LINE_CHANNEL_SECRET"))
working_status = True

app = Flask(__name__)
bloom = BLOOM()


@app.route("/")
def home():
    return "Flask ready!"


@app.route("/webhook", methods=["POST"])
def callback():
    # get X-Line-Signature header value
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        line_handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return "OK"


@line_handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    global working_status

    # online
    if event.message.text == "Hey Agent!":
        working_status = True
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="機器人上線！你可以問我各種事情，像是某個事件的歷史淵源，或是提供一段前文讓我續寫故事"),
        )
        return

    # offline
    if event.message.text == "Bye!":
        working_status = False
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="再會！下次再聊！"),
        )
        return

    if working_status:
        reply_msg = bloom.get_response(event.message.text)
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply_msg))


if __name__ == "__main__":
    app.run()
