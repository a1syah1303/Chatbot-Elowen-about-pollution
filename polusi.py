import discord
from discord.ext import commands
TOKEN = 'TOKEN KAMU'
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

ide = {
    "botol": "Botol plastik bisa dijadikan tempat pensil atau pot tanaman",
    "kertas": "Kertas bekas bisa dipakai untuk catatan atau anyaman kertas",
    "kaleng": "Kaleng bisa dijadikan tempat lilin atau wadah alat tulis",
    "plastik": "Plastik bisa dijadikan tas daur ulang",
    "kardus": "Kardus bisa dibuat jadi tempat penyimpanan atau bisa dipotong dan ditempel kertas lalu dijadikan pajangan :>"
}

@bot.event
async def on_ready():
    print("Bot siap!")

@bot.command() 
async def about(ctx): 
    await ctx.send("Hi! aku Elowen. Apakah kamu tahu penyebab polusi?") 
    await ctx.send(f'Polusi disebabkan oleh berbagai aktivitas manusia yang melepaskan zat berbahaya ke lingkungan') 
    await ctx.send(f'Dan, sebagai upaya untuk melakukan hal tersebut, kamu bisa melakukan sesuatu loh! seperti mendaur ulang sampah.')
@bot.command()
async def mulai(ctx):
    await ctx.send(
        "Ada apa di rumahmu?\n"
        "Ketik: botol / kertas / kaleng / plastik / kardus\n"
        "Ketik 'stop' untuk berhenti"
    )

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    while True:
        try:
            msg = await bot.wait_for("message", timeout=30.0, check=check)
            barang = msg.content.lower()

            if barang == "stop":
                await ctx.send("Oke, sampai jumpa!")
                break

            elif barang in ide:
                await ctx.send(ide[barang])
                await ctx.send("Mau coba lagi? ketik barang lain atau 'stop'")
            
            else:
                await ctx.send("Barang belum ada di daftar, coba lagi ya!")

        except:
            await ctx.send("Waktu habis! coba lagi ya")
            break


bot.run('TOKEN KAMU')