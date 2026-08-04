import discord
from senha import senha

# A variável intents armazena as permissões do bot
intents = discord.Intents.default()
# Ativar a permissão para ler o conteúdo das mensagens
intents.message_content = True
# Criar um bot e passar as permissões
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Fizemos login como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hello!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('!senha'):
        await message.channel.send(senha())
    else:
        await message.channel.send(message.content)

client.run("MTUzMTc2NzU3MDMzMDQxOTMzMA.G-PrYU.u_s-PC5mlLaRbXPkN4dXBn7fAeX-1lBCcTG834")