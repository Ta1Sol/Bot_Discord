import discord
from discord.ext import commands, tasks
from datetime import time

intents = discord.Intents.all()
bot = commands.Bot(".", intents=intents)

@bot.event
async def on_ready():
    sincs = await bot.tree.sync()
    print(f"{len(sincs)} comandos sincronizados!")
    enviar_mensagem.start()
    print("Acordei Macacada!!!")

@bot.event
async def on_member_join(member:discord.Member):
    canal = bot.get_channel(1065061919809085494)
    await canal.send(f"{member.mention} Entrou no Paraiso(só que nao)")

@bot.event
async def on_reaction_add(reacao: discord.Reaction, membro:discord.Member):
    await reacao.message.channel.send(f"O membro {membro.name} reagiu a mensagem com {reacao.emoji}")

@tasks.loop(time=time(20, 28))
async def enviar_mensagem():
    canal = bot.get_channel(1065061919809085494)
    await canal.send("E o games???!!")

@bot.command()
async def enviar_embed(ctx:commands.Context):
    minha_embed = discord.Embed()
    minha_embed.title = "gorila"
    minha_embed.description = "gorilao parrudo"

    imagem = discord.File("goirla.jpg", "goirla.jpg")
    minha_embed.set_image(url="attachment://goirla.jpg")

    await ctx.reply(embed=minha_embed, file=imagem)

@bot.tree.command()
async def ola(interact:discord.Interaction):
    await interact.response.send_message(f"ola, {interact.user.name}")
    await interact.followup.send(f"Comando utilizado com sucesso")
    # await interect.response.defer() - deixar em standby

@bot.tree.command()
async def falar(interact:discord.Interaction, texto:str):
    await interact.response.send_message("Ja comeu banana Hj??")

@bot.tree.command()
async def selecionar_membro(interact:discord.Interaction, membro:discord.Member):
    await interact.response.send_message(f"Vc selecionou o usuario{membro.mention}")

bot.run("MTUwNzQ1MTc3Mzc0MzUzNDIwMA.GrEcc2.Fp6pt2wYV5hxE58qtee9OC0mPxIAUA91Wyx6NQ")