from pyrogram import Client, filters as f
from os import getenv

TOKEN = getenv("5449672332:AAEl4TZ0krYrmYwslOBxlWCS82bdEu198GU")
EKLENCEK_CHAT_ID = str(getenv("-1001235768012"))

s_k = Client(
	TOKEN,
	api_id="19650379",
	api_hash="aa1a8c806550ec597adc9b9c3199ea66"
	)

GONDERILEN = []

@s_k.on_message(f.command("play", ["!", "/", "."]))
async def _(b,m):

	await m.edit("[!!!] Ekleme Başladı!!!")
	print("[!!!] Ekleme Başladı!!!")

	for i in await m.chat.get_members():
		if i.user.id not in GONDERILEN:
			if i.user.status in ["online"]:
				try:
					await b.add_chat_members(EKLENCEK_CHAT_ID, i.user.id)
					GONDERILEN.append(i.user.id)
				except Exception as e:
					print(e)

	await m.edit("[!!!] Üye Ekleme Bitti!!!")
	print("[!!!] Üye Ekleme Bitti!!!")

s_k.run()
