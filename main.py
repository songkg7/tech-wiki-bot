import telegram
from telegram.ext import Updater, MessageHandler, Filters

token = "1807876226:AAEd1cxYIymbr9VzrWOeln_BNXcyCcd87q4"
bot = telegram.Bot(token=token)

# 본인의 chat_id를 알아내는 과정이 필요합니다.
# chat_id 를 맞게 수정해주세요.
# chat_id = bot.getUpdates()[-1].message.chat_id
chat_id = 940986442

info_message = '''모르는게 있으면 물어보세요!
Skills : Java, Python
Algorithm : DP, BruteForce, Sort, ...
기술면접을 대비한 다양한 사전지식을 제공합니다.'''
bot.sendMessage(chat_id=chat_id, text=info_message)

updater = Updater(token=token)
dispatcher = updater.dispatcher
updater.start_polling()

java_info = '''
Java?
썬 마이크로시스템즈에서 1995년에 개발한 객체지향 프로그래밍 언어입니다.
창시자는 [제임스 고슬링]입니다.
2010년에 오라클이 썬 마이크로시스템즈를 인수하면서 Java의 소유권이 이전되었습니다.
'''

python_info = '''
Python?
1991년에 발표된, 매트랩과 유사한 인터프리터 방식의 프로그래밍 언어.
창시자는 [귀도 반 로섬(Guido van Rossum)].
문법이 매우 쉬워서 초보자들이 처음 프로그래밍을 배울 때 추천되는 언어입니다.
'''


def handler(update, context):
    user_text = update.message.text.lower()

    greeting = ["안녕", "hi", "ㅎㅇ"]

    if user_text in greeting:
        bot.sendMessage(chat_id=chat_id, text="안녕하세요!")

    elif "java" in user_text or "자바" in user_text:
        bot.sendMessage(chat_id=chat_id, text=java_info)

    elif "python" in user_text or "파이썬" in user_text:
        bot.sendMessage(chat_id=chat_id, text=python_info)


echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)
