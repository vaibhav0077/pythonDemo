from telethon import TelegramClient, events
import time

# Remember to use your own values from my.telegram.org!
api_id = 
api_hash = 

client = TelegramClient('anon', api_id, api_hash)
client.start()
@client.on(events.NewMessage)
async def handler(event):
 #   chat_id = event.chat_id
#    print(chat_id)
# print(events)
#with TelegramClient ( 'anon', api_id, api_hash ) as client :
    today = time.asctime(time.localtime(time.time()))
    await client.send_message('@Ak_Gaming_07', today )
    print(today)
    #time.sleep(10)
    await client.send_message(-390585843, today)

# ...to your contacts
# await client.send_message(+916354713284, 'Hello, friend!')
# ...or even to any username
# await client.send_message('@Ak_Gaming_07', 'Always You get my reply')


client.run_until_disconnected()
