import telebot
from telebot import types

# توكن البوت
TOKEN = "8132688584:AAGXu1jBADDsb_JxLyq6BzI2RcmIXmZ4HAk"
bot = telebot.TeleBot(TOKEN)

# رقم الهاتف للدفع
PAYMENT_NUMBER = "ضع رقمك هنا"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("طلب لوحة حسب الطلب")
    markup.row("عرض اللوحات الجاهزة", "طريقة الدفع")
    bot.send_message(
        message.chat.id,
        "أهلاً بك في *متجر بيع اللوحات الرقمية حسب الطلب*.\n\nاختر من الخيارات التالية:",
        parse_mode="Markdown",
        reply_markup=markup
    )

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "طلب لوحة حسب الطلب":
        bot.send_message(
            message.chat.id,
            "يرجى إرسال فكرتك أو وصف اللوحة التي تريدها.\nمثال: 'أريد لوحة لأنمي فتاة تقرأ كتابًا في المطر بأسلوب واقعي'."
        )

    elif message.text == "عرض اللوحات الجاهزة":
        send_ready_products(message.chat.id)

    elif message.text == "طريقة الدفع":
        bot.send_message(
            message.chat.id,
            f"الدفع يكون عبر تحويل رصيد إلى الرقم التالي:\n\n*{PAYMENT_NUMBER}*\n\n"
            "بعد التحويل، يرجى إرسال:\n"
            "- صورة إيصال أو إشعار التحويل\n"
            "- **ورقم الهاتف الذي تم الدفع من خلاله**\n\n"
            "حتى يتم تأكيد الطلب والبدء بالرسم.",
            parse_mode="Markdown"
        )

# نموذج مبدئي للمنتجات الجاهزة (تقدر تعدله)
def send_ready_products(chat_id):
    bot.send_message(chat_id, "حالياً لا توجد لوحات جاهزة للعرض.\nتابعنا ليصلك كل جديد قريباً!")

# تشغيل البوت
bot.polling()
