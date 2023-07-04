import discord
import time
import random

number = [1]
running = True
name2 = ["нет"]
name1 = ["минуты", "минут", "мин", "сек"]
hello_words = [ "привет", "hello", "hi", "ку", "как дела", "хай", "саламалейкум", "cалам"]
info_words = [ "как сделать", "куда обратиться", "помощь", "помогите", "поддержка", "спасите", "помоги" ]
ar_words = [ "арсений", "артур", "артём", "саша", "саня", "артёмка" ]
#guess = int(input('Введите целое число : '))
s = 'саша iopasd fghjklz xcvbnm'
print(s.title())

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content.lower()
    msg_list = msg.split()


#Главные команды
    find_hello_words = False
    for item in hello_words:
        if msg.find(item) >= 0:
            find_hello_words = True
    if (find_hello_words):
        await message.channel.send(f' {message.author.mention} Привет! Как твои дела?')

    find_ar_words = False
    for item in ar_words:
        if msg.find(item) >= 0:
            ares_words = True
    if (find_ar_words):
        await message.channel.send(f' {message.author.mention} Привет!')

    find_info_words = False
    for item in info_words:
        if msg.find(item)>=0:
            find_info_words = True
    if (find_info_words):
        await message.channel.send(f' {message.author.mention} Спасибо за обращение, ваш вопрос передан Админу. Ожидай')

    if msg == '$help':
        await message.channel.send('\nКоманды бота Full-Master'
                                   '\n1) Где живёт ****?'


                                   )

    if (msg in hello_words) or len(list(set(msg_list + hello_words)))<len(msg_list) + len(hello_words):
        time.sleep(2)
        await message.channel.send('Ты в порядке да?')

#игра в числа

    if message.content.startswith('$Давай сыграем в игру'):
        while running:
            await message.channel.send  (int(input('Введите целое число: ')))
            guess = (int(input('Введите целое число : ')))
            if message.content.startswith [guess == number]:
                await message.channel.send ('Поздравляю, вы угадали.')
            elif message.content.startswith [guess < number]:
                await message.channel.send ('Нет, загаданное число немного больше этого.')
            else:
                await message.channel.send ('Нет, загаданное число немного меньше этого.')




#Адреса


    if message.content.startswith('где живёт Артур?'):
        await message.channel.send(' Артур проживает на улице Соломенковской, дом 3, кв.47 ')

    if message.content.startswith('где живёт Артём?'):
        await message.channel.send(' Артём проживает на улице Соломенковской, дом 5а, кв.68 ')

    if message.content.startswith('где живёт Ваня?'):
        await message.channel.send(' Ваня чаще всего бомжует, но числится на улице Южной, дом 12а, кв.15 ')

    if message.content.startswith('где живёт Саня?'):
        await message.channel.send(' Саня проживает на улице Южной, дом 24а, кв.72 ')

    if message.content.startswith('где живёт Арсений?'):
        await message.channel.send(' Арсений проживает на улице Соломенковской, дом 3а, кв.72 ')

    if message.content.startswith('Где живёт Артур?'):
        await message.channel.send(' Артур проживает на улице Соломенковской, дом 3, кв.47 ')

    if message.content.startswith('Где живёт Артём?'):
        await message.channel.send(' Артём проживает на улице Соломенковской, дом 5а, кв.68 ')
    if message.content.startswith('Где живёт Артем?'):
        await message.channel.send(' Артём проживает на улице Соломенковской, дом 5а, кв.68 ')
    if message.content.startswith('где живёт Артём?'):
        await message.channel.send(' Артем проживает на улице Соломенковской, дом 5а, кв.68 ')

    if message.content.startswith('Где живёт Ваня?'):
        await message.channel.send(' Ваня чаще всего бомжует, но числится на улице Южной, дом 12а, кв.15 ')

    if message.content.startswith('Где живёт Саня?'):
        await message.channel.send(' Саня проживает на улице Южной, дом 24а, кв.72 ')

    if message.content.startswith('Где живёт Арсений?'):
        await message.channel.send(' Арсений проживает на улице Соломенковской, дом 3а, кв.72 ')


client.run('***********************')