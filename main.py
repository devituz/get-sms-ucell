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
    "lang=a6d6dba8afe4b98bf115b3293c75849a957a8c54%7Euz; _ga=GA1.2.1407516973.1722942805; _gid=GA1.2.92820946.1722942805; _culture=uz; _crp=s; ASP.NET_SessionId=knd2dvruhmwhxgy21ne4qskp; _gat=1; .UWCCFRONTNXAUTH=68BBF875BF8324C3BA08627E6CFAD29D99D71C7CD0B51E773B87377CCFEB177DDEDED18A2539B2B65E1E10DBE80DCC21E5A28F8B621960DC466840210E4AA880F151B97502DC5655ADF65D1A8A9B024057CD927719DCFB58A17FBD40160906C33A4594643F895FE31BD4A3C40FA7F0044CA6AC24176E5C8FC32C3AF290E67AA12E44F5B4354C9B1C633F1D8B6E1EEB8B0AB31287F3171B4C76FE05769C7E87AFC71ACE3701DA9942983BF0C39EF3186908631CC4F94168C85A9299F4B5C9B1CF3CCBC94570ACA42CD95BDCAEC6A87D20F55FF7F4956BDD701C083299DF70160FF8C19915E893CE9DBE0030277D58CB567DE0B969FE8226F2109F6FDDADAB8746BD2E238276A447548A31E6BE084EDEAAAC5FEA9C72F7C98A84F5DC4D124DA8A080BB25EF50B2EA860C8769A353720E99B89D8E9E4D8DF94E4887933E058520ADBCADF770723BE10647DE33AE541BC198",
    "lang=a6d6dba8afe4b98bf115b3293c75849a957a8c54%7Euz; _ga=GA1.2.1407516973.1722942805; _gid=GA1.2.92820946.1722942805; _culture=uz; _crp=s; .UWCCFRONTNXAUTH=81875BA3C2B560527C197544CA671676524CFF02F9F52A6B65D5B96E569D9A37852770C1070907170D7AB652C2E9AB04BB3BE298EE986E28500CE8493FA5B0A527BDADA5808F2D8D6DD99EC90523FA5DAD748E03A8286807397413448D994CA49A6F7058D991979FEF1B3D0C04DBC001EF43F06BA8D800EDE4E84C05244775216785CFE5130FCFE614E3310A6CBD9E8B1A12C1DC208E752B3C271A0DD07DD27F235CE213059905700C474C7E0F22320699F2B857A94EF6B3F0A4404AC191D4A27DF340C5D8580CF7AD063C36EA0250A7776FA7466A645341884806F2BD00F2DD2205F39D222BEF62137A154B7232CA73E1A918999A5AD3FC87CB1FB0ADEE9689BB495863D1A6D73D174C6D26D1FB52549F58CC2FACAF97607B148E561021CE1749081DFED88752AAB306C143D6774424772973F100667ECEA27B4BF180944A28F355EC06E6A0A4CF5AC2F128D88CA76A; ASP.NET_SessionId=x1iwenkvsg5ddvb322uiraiy; _gat=1"
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
