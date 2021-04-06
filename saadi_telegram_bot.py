from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import random
import poem_back
from time import sleep


def hello(update, context):
    update.message.reply_text(
        'سلام {}'.format(update.message.from_user.first_name))
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="من برای تو هر وقت که بخوای یک بیت یا یک شعر سعدی ارسال میکنم!")
    context.bot.send_message(chat_id=update.effective_chat.id, text="برای دریافت شعر تصادفی فقط کافیه random/ رو بزنی")
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="یا میتونی با فرستادن یک واژه، اونو داخل ابیات سعدی سرچ کنی")
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="یا با ارسال یک عدد غزل nام سعدی رو دریافت کنی")


def send_poem(num, update, context):
    poem = poem_back.Poem.load_poem_pickle("./saadi/divan/ghazals/{}.pm".format(num))
    txt = "غزل شماره " + str(num)
    #print(txt)
    context.bot.send_message(chat_id=update.effective_chat.id, text=txt)
    for beyt in poem["all_beyts"]:
        beyt_txt = beyt.print_b(sep="\n")
        #print(beyt_txt)
        context.bot.send_message(chat_id=update.effective_chat.id, text=beyt_txt)


def random_poem(update, context):
    random_num = random.randint(1, 637)
    send_poem(random_num, update, context)


def search_result(update, context):
    target_word = update.message.text
    num_ref = "0123456789۰۱۲۳۴۵۶۷۸۹"
    ref_en = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #print(target_word)
    alisnum = True
    num_count = 0
    for char in target_word:
        if not char in num_ref:  # char was a alpha
            alisnum = False
        else:  # char is a number
            num_count += 1
    is_english_char = False
    for char1 in target_word:
        if char1 in ref_en:
            is_english_char = True
    if num_count < len(target_word) and num_count != 0 or is_english_char:  # contains both number and alpha or english car
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="ببین داداش یا شایدم آبجی اگه میخوای منو اذیت کنی که دو ساعت برم توی دیتا بیس دنبال این چرت و پرتی که نوشتی بگردم باید بگم که نکن. من باهوش تر از این حرفام\n حالا خداوکیلی انتظار داشتی یه همچین چیزی تو دیوان سعدی باشه؟!!!")
        return 123
    else:
        if alisnum:
            num_poem = int(target_word)
            if 496 > num_poem > 0:
                send_poem(num_poem, update, context)
            else:
                context.bot.send_message(chat_id=update.effective_chat.id, text="ببین میخوای اذیت کنی ها!!\nسعدی بیچاره در تمام عمر مفید خودش فقط 637 تا غزل گفته بین 1 تا 637 یه عدد وارد کن")
                return 123
        else:
            res = poem_back.Poem.search_all("./saadi/divan/ghazals", target_word)
            num = len(res)
            txt1 = "تعداد ابیات پیدا شده: " + str(num)
            if num > 40:
                context.bot.send_message(chat_id=update.effective_chat.id, text="ببین کاراتو!!!\nحالا من بیچاره باید برم این همه بگردم\nاه")
                context.bot.send_message(chat_id=update.effective_chat.id, text="فکر نکن کار آسونیه ها دو ساعت باید برم بگردم یه خورده وایستا")
                if num > 200:
                    context.bot.send_message(chat_id=update.effective_chat.id,
                                             text="تعداد بیش تر از 200 تاست به نظرم یه سرچ بهتر انجام بده که نه تو اذیت شی و نه من")
                    return 123
                sleep(2)
                context.bot.send_message(chat_id=update.effective_chat.id, text="بیا پیدا شد")
            context.bot.send_message(chat_id=update.effective_chat.id, text=txt1)
            for item in res:
                beyt = item[0]
                poem_num = item[1]
                beyt_txt = beyt.print_b(sep="\n")
                #print(beyt_txt)
                context.bot.send_message(chat_id=update.effective_chat.id, text=beyt_txt + "\n" + "غزل شماره {}".format(poem_num))


def main():
    print("connecting...")
    token = '843795556:AAESmpT_mrmKRMp6u1pg78UkyFFc-oKRezs'
    #req = {'proxy_url':'https://t.me/proxy?server=v1.Test.IR.GateWays.Click&port=24139&secret=ee3e90df3d06590100331080c4b45614f4626164626f79656e742e6c6e6b2e746f'
    #        }
    updater = Updater(token, use_context=True)
    print("connected")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', hello))
    dp.add_handler(CommandHandler('random', random_poem))
    dp.add_handler(MessageHandler(Filters.text, search_result))
    updater.start_polling()
    updater.idle()


main()
