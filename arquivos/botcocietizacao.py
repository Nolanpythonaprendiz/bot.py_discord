import discord


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
    if message.content.startswith('$LIXO'):
        await message.channel.send("O lixo é responsabilidade de todos nós. Jogar resíduos no lugar certo, reciclar e evitar o desperdício são pequenas atitudes que ajudam a preservar o meio ambiente. Se cada pessoa fizer a sua parte, podemos construir um mundo mais limpo, saudável e sustentável.")
    elif message.content.startswith('$COMO AJUDAR'):
        await message.channel.send("Para ajudar a limpar o meio ambiente, você pode:\n🗑️ Jogar o lixo na lixeira correta.\n♻️ Separar materiais recicláveis, como papel, plástico, vidro e metal.\n🌳 Plantar e cuidar de árvores.\n🚯 Não jogar lixo nas ruas, rios ou terrenos.\n🧹 Participar de mutirões de limpeza.\n💧 Evitar desperdiçar água.\n🔄 Reutilizar objetos sempre que possível.\n📢 Incentivar outras pessoas a cuidarem do meio ambiente.Uma pequena atitude de cada pessoa pode fazer uma grande diferença! 🌎💚")
    elif message.content.startswith('!senha'):
        await message.channel.send(senha())
    else:
        await message.channel.send(message.content)

client.run("MTUzMTc2NzU3MDMzMDQxOTMzMA.G-PrYU.u_s-PC5mlLaRbXPkN4dXBn7fAeX-1lBCcTG834")