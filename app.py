import time
from telethon.sync import TelegramClient
from telethon.tl import functions

api_id = 'apiid'  # Telegram API ID'nizi buraya ekleyin
api_hash = 'apihash'  # Telegram API anahtarınızı buraya ekleyin
phone_number = 'telnumaranız 90 ile başlayın, Ülke kodunuzla'  # Telefon numaranızı buraya ekleyin
username = 'mesajı göndermek istediğiniz kanalın kullanıcı adı'  # Hedef kullanıcının veya botun kullanıcı adını buraya ekleyin

client = TelegramClient('otomasyon_session', api_id, api_hash)

async def main():
    await client.start()
    me = await client.get_me()
    print(f"Oturum açıldı: {me.username}")

    while True:
        message = 'Mesajınızıburayagiriniz'
        await client(functions.messages.SendMessageRequest(
            peer=username,
            message=message
        ))
        print("Mesaj gönderildi.")
        time.sleep(2)

with client:
    client.loop.run_until_complete(main())

