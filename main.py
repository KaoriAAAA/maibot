import random
import discord
import os
import json
import datetime
import re
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

with open('config.json', 'r') as file:
    config = json.load(file)

bot = commands.Bot(command_prefix=("mai, ", "(", "mei, ", "MAI, ", "MEI, "), intents=intents, case_insensitive=True, help_command=None)

@bot.event
async def on_ready():
    print(f'estou pronta pra funcao')
    await bot.change_presence(activity=discord.Game(name="sua prima na cama"))

@bot.command()
async def hello(ctx):
    latency = round(bot.latency * 1000)
    await ctx.send(f'o meu ping e de {latency}ms posso jogar cs?')

@bot.command()
async def xota(ctx):
    meme_folder = 'f:/MEMES'  # A folder where you store meme images
    meme_files = os.listdir(meme_folder)
    meme_file = random.choice(meme_files)
    await ctx.send(file=discord.File(os.path.join(meme_folder, meme_file)))

@bot.command()
async def ronaldo(ctx):
    ronaldo_audio = 'f:/MEMES/ronaldo/ronal3.wav'
    await ctx.send(file=discord.File(ronaldo_audio))

@bot.command(aliases=['rola', 'pica', 'trozoba'])
async def piton(ctx):
    if ctx.message.mentions:
        target = ctx.message.mentions[0]
        if target.id == 417327061439479818:
            var = 100  # Always max size for you
        else:
            var = random.randint(1, 3)
        nome = target.display_name
    else:
        if ctx.author.id == 417327061439479818:
            var = 100
        else:
            var = random.randint(1, 50)
        nome = ctx.author.display_name

    penis = "8" + "=" * var + "D"
    await ctx.send(f'rola de {nome} = {penis}')

@bot.command()
async def help(ctx):
    caralhao = discord.Embed(
        title="MAI BOT AJUDA PORRA",
        description="aqui estão os comandos disponíveis:",
        color=0xf40068
    )

    caralhao.set_author(name="MAI BOT NAO CONFUNDA COM OUTROS BOTS", icon_url="https://i.imgur.com/e0Ehk26.jpeg")
    caralhao.add_field(name="```Importantes```", value="**help**: mostra esse menu", inline=False)
    caralhao.add_field(name="```Atumalaque```", value="**xota:** manda um meme\n**piton/rola/pica/trozoba @alguem:** mostra o tamanho da rola de @alguem se deixar sem marcar ninguem mostra o seu tamanho\n**fetiche @alguem:** descobre o fetiche de alguem\n**salsicha [pergunta]:** faça uma pergunta para o salsicha vidente\n**roleta/roletarussa @alguem:** o bot roda uma roleta russa. se o alvo morrer, ele muta o alvo por 28 dias. ***NÃO PRECISA DE PERMISSÃO DE MUTAR PARA USAR O COMANDO, CUIDADO***", inline=False)
    caralhao.add_field(name="```Utilitarios```", value="**limpa [n]**: limpa o chat em [n] mensagens. n precisa ser de 1 a 100. **[Precisa ter permissao de apagar mensagem]**\n**hello:** comando de ping\n**ronaldo:** ronaldo AIIIII AAAAAAAAAI\n**kick @alguem:** kicka alguem do server\n**ban @alguem:** bane alguem do server\n**mute/timeout @alguem [tempo] [motivo]:** da timeout em alguem pelo tempo especificado. formato de tempo e [numero][s, m, d, h]", inline=False)

    caralhao.set_image(url="https://media.tenor.com/aE4K8BTrwLwAAAAj/rodrigo-rodrigo-moraes.gif")

    caralhao.set_footer(text="prefixos disponiveis: [mei, ] [mai, ] [(] todos os comandos pode escrever com letra maiuscula ou minuscula ainda nao tem comando de / que nem bots melhores")

    await ctx.send(embed=caralhao)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def limpa(ctx, amount: int):
    if amount < 1 or amount > 100:
        await ctx.send("vai toma no cu faz direito")
        return

    try:
        deleted = await ctx.channel.purge(limit=amount)
        await ctx.send(f"limpei {len(deleted)} menages", delete_after=1)
    except discord.Forbidden:
        await ctx.send("voce nao pode fazer isso")

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, membro: discord.Member, *, motivo=None):
     try:
         await membro.kick(reason=motivo)
         await ctx.send(f'{membro} vai pro inferno arrombado')
     except discord.Forbidden:
        await ctx.send("voce nao pode fazer isso")

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, membro: discord.Member, *, motivo=None):
    try:
        await membro.ban(reason=motivo)
        await ctx.send(f'{membro} banido pelo adeeme por {motivo} kkkkkkkk adm nao mi tira do grupo nao :joy: :joy: :joy: 2020 shitpost status AAAAAAAAAAAAAAA')
    except discord.Forbidden:
        await ctx.send("voce nao pode fazer isso")

@bot.command(aliases=['timeout'])
@commands.has_permissions(kick_members=True)
async def mute(ctx, membro: discord.Member, delta=None, *, motivo=None):
    if delta is None:
        await ctx.send("manda o tempo burro (ex: 10m, 2h, 1d).")
        return

    match = re.fullmatch(r"(\d+)([smhd])", delta)
    if not match:
        await ctx.send("formato de tempo inválido, animal. use '10m', '2h', '1d', etc.")
        return

    quantidade, unidade = match.groups()
    quantidade = int(quantidade)

    # Create a timedelta based on the input
    delta = None
    if unidade == "s":
        delta = datetime.timedelta(seconds=quantidade)
    elif unidade == "m":
        delta = datetime.timedelta(minutes=quantidade)
    elif unidade == "h":
        delta = datetime.timedelta(hours=quantidade)
    elif unidade == "d":
        delta = datetime.timedelta(days=quantidade)

    if delta is None:
        await ctx.send("nao conheco essa unidade de tempo.")
        return

    try:
        await membro.timeout(delta, reason=motivo)
        await ctx.send(f'{membro.mention} foi mutado por {delta} devido a: {motivo}. Aqui vai um aviso para não mexer com a máfia do cu roxo.')
    except discord.Forbidden:
        await ctx.send("você não pode fazer isso.")

@bot.command()
async def fetiche(ctx, membro: discord.Member = None):
    if membro is None:
        membro = ctx.author

    lista1 = ["pés", "tentáculos", "cristianos ronaldos", "mulheres", "bimbuçus", "homens", "bundas", "o lucas", "motos", "edukofs", "padres", "pastores", "personagens de valorant", "betoneiras", "britadeiras", "filhas das putas", "jogadores de lol", "mains yasuo", "caminhoes fodas"]
    lista2 = ["cagando", "rezando", "cantando", "mijando", "pelados(as)", "se mexendo", "rebolando", "lendo um livro", "raspando o restinho de crack da latinha"]
    lista3 = ["em cima de uma kombi", "aula de calculo do zanco", "faeterj", "na igreja", "no minecraft", "em itupeva", "em bangu", "em 📍 Moreno - PE", "em hogwarts", "na casa da sua mae aquela puta", "na oficina", "no maracanã", "dentro do seu cu"]

    await ctx.send(f"{membro.mention} voce tem fetiche em {random.choice(lista1)} {random.choice(lista2)} {random.choice(lista3)}")

@bot.command()
async def salsicha(ctx, *, pergunta):
    respostas = ["se pa", "sim", "nao", "sei la mas voce tem um bucetao gostoso", "minha prima deve saber", "onze de setembro", "talvez", "<@417327061439479818> responde aí voce", "hmmm curiosa", "dominic toretto", "a resposta é bolsonaro", "acho que sim", "ouvi dizer que sexo selvagem ajuda com isso", "já vi isso daí. é um episódio de chaves né?"]
    await ctx.send(f"{random.choice(respostas)}")

@bot.command(aliases=['roleta'])
async def roletarussa(ctx, membro: discord.Member = None):
    tiro = random.randint(1,6)
    if membro is None:
        membro = ctx.author

    if tiro == 3:
        await membro.edit(nick="💀")
        await membro.timeout(datetime.timedelta(days=28))
        await ctx.send(f"{membro} caiu na pica na roleta russa e foi mutado por 28 dias f")
    else:
        await ctx.send("voce sobreviveu")

bot.run(config['token'])