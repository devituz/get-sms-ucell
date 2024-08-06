import requests
from bs4 import BeautifulSoup
import time
import telebot
from datetime import datetime

telegram_token = "7223835990:AAGCgfT6jqaekgBzWQdBmLbNJVyBRdROIjw"
chat_id = "7321341340"

# Telegram bot obyekti yaratish
bot = telebot.TeleBot(telegram_token)

def send_message(message):
    bot.send_message(chat_id=chat_id, text=message)

# URL
url = "https://my.ucell.uz/"

# Headerlar
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Host": "my.ucell.uz",
    "Referer": "https://my.ucell.uz/PcSms",
    "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
}

# Cookie tokenlari ro'yxati
cookies = [
    "lang=a6d6dba8afe4b98bf115b3293c75849a957a8c54%7Euz; _ga=GA1.2.1407516973.1722942805; _gid=GA1.2.92820946.1722942805; _culture=uz; _crp=s; ASP.NET_SessionId=4aut2ld1vw220sdcum25nf1i; .UWCCFRONTNXAUTH=0C55F2B888002164A4499E0C85729EC5FF2ED811BCACE1918063EEABEE0D2F0CB4DE78FB1FDDC08AD07B68A886F933EA3A8B7E7B1E0A2E164F50D483EC9ACE4D4D87A963BC6B106A565B3A49A61CE737891B9BDE6E2C0350FBC41161C0F8946D2A622DF62A61AD888EFFB82EF03BD6BD33C9BCE378945C3F016B04A2CE034206058AEA530B8708A82395585270FF8577823585F942E3DE4CDA9E273FE061A0D23F7385EF3ECDA3006EA2FD48F5875AE393BC4A9EBD0FF454E294872D8F753CBC6EB4372E04D157077325CE0F6CF3B33036E37F3E9CDC3AD536D8A83D7A14ED8F9E13B8BD701B6ADEC00F69E16C11CFDD97C935939105A39C789EBE8588E37CDA8BB61F0DFF5710C4A0B5A88AF01804BF42FDAB6DB5FE6F1086D28E77560AF6D16F58C4A7BFACBB731304F3A7E6CD4A4B58CF5C76BDF8A85DB1E19FE4EB69D949137F3CC28E3D8975D03C190003CA5F2A",
    "lang=a6d6dba8afe4b98bf115b3293c75849a957a8c54%7Euz; _ga=GA1.2.1407516973.1722942805; _gid=GA1.2.92820946.1722942805; _culture=uz; _crp=s; .UWCCFRONTNXAUTH=0A9752B3DE6AC3032247CEA0EB60EC24A8025612A6E9EC38FE6683338F4EAE5B70C0F71120B05B0B3539433FAC0C18FB6208A7CA3205AF362E43E2DEA2D9DCB0D1F9C6C8982D06224503CEFC9B2BE54461EB124000476F71611CA6DD43DEC43FCEEACB80B5E7E0379E4C43BAB2BD3D7B475997B14BA3BC3F2AD4BBD73F4992842EDC347C00A01256C27350829F01309DE6B57E7886A9168CDB21B58179739E41F52AB1B4A418AD3275BDFEC8D9BA11E472D88C207D4E9A0F5D62F0FDF8C3D102A3E372358E1BD8A3F499A3566648A8605DD3DFD908F43AB16BF85BE0750DC6547EAD8B4E67075E087E1869FA09B7A69C2E3651085898606D6C29B8AC47E5FF3202409B495353119EEB68BF0A17EF90B0937A92614DE5E7365A2F7DC06AF3AB8A5EA42502F8AAD8237063A68C9369105AE117F45959CABC7812C3F231DD8AADF49C0B57B4E5477282F85513EE51551781; ASP.NET_SessionId=knd2dvruhmwhxgy21ne4qskp"
    # Qo'shimcha cookie tokenlar
]

# Hisobot uchun o'zgaruvchi
request_number = 1
last_request_time = datetime.now()

while True:
    overall_report = ""
    for idx, cookie in enumerate(cookies):
        headers["Cookie"] = cookie

        # GET so'rovi yuborish
        response = requests.get(url, headers=headers)

        # HTMLni tahlil qilish
        soup = BeautifulSoup(response.text, 'html.parser')

        # Telefon raqamni olish
        phone_number = soup.find('span', id='nav_subscriber_num')

        # Hozirgi vaqtni olish
        current_time = datetime.now()
        time_diff = current_time - last_request_time

        # Hisobotni tayyorlash
        report_message = f"Token {idx + 1} - {request_number}-GET so'rovi yuborildi\n"
        report_message += f"Status Code: {response.status_code}\n"
        report_message += f"Soat: {current_time.strftime('%Y-%m-%d %H:%M:%S')}\n"
        report_message += f"Oraliq vaqt: {time_diff}\n"
        report_message += f"Cookie: {cookie}\n"

        # Telefon raqamni tayyorlash (agar mavjud bo'lsa)
        if phone_number:
            report_message += f"Telefon raqam: {phone_number.text}\n"
        else:
            report_message += "Telefon raqam topilmadi.\n"

        # Hisobotni umumiy hisobotga qo'shish
        overall_report += report_message + "\n"

    # Hisobotni chiqarish
    # print(overall_report)

    # Telegram bot orqali yuborish
    send_message(overall_report)

    # Hisobot raqamini oshirish
    request_number += 1

    # Oldingi so'rov vaqtini yangilash
    last_request_time = datetime.now()

    # Har 60 sekundda takrorlash
    time.sleep(1200)  # 60 sekund kutish
