import discord
from discord import Embed
import random
import datetime
import os
from googletrans import Translator, constants   
from discord.ext import commands, tasks
client = commands.Bot(command_prefix="cnv-")


generaltopic = ['Free time', 'Books', 'TV Shows', 'Hobbies', 'Pets',
 'Restaurants', 'Humor', 'Social Media', 'Cars',
 'School', 'Family', 'Coffee', 'Cooking', 'Addiction', 'Languages',
  'Super heroes', 'Earth', 'Drinking', 'Ice cream', 'Sleep', 'Dancing', 'Singing',
   'Art', 'Facts', 'Musical instruments',"Games","Cities","Religion","Planes","Songs","Marriage","Jobs","Humans","Communism","Capitalism","Bussines"
   ,"Computers","Pyramids","Swimming","Love","Money","Lessons",
   "Transportation","Vegetarians","Dreaming","Programming","Reading","Obesity","Pandemics","Countries","Feelings"]

questiontopic = [' WHAT CAN YOU DO THAT NO ONE ELSE CAN', 'WHAT IS THE CRAZIEST STORY YOU’VE EVER HEARD',
 'WHAT IS THE NERDIEST THING YOU DO IN YOUR SPARE TIME', 'IF YOU COULD TELEPORT WHERE WOULD YOU GO, AND WHY',
  'WOULD YOU ACCEPT A ONE-WAY TICKET TO MARS', 'WHAT IS THE ONE THING YOU HAVE ALWAYS WANTED TO DO',
   'IF YOU COULD WIN ANY AWARD WHAT WOULD IT BE, AND WHY', 'WHAT DO YOU LIKE MORE, BEING A LEADER OR A FOLLOWER',
    'WHAT’S THE BEST BOOK YOU’VE READ THIS YEAR', 'WHAT IS THE FIRST THING YOU NOTICE ABOUT SOMEONE WHEN YOU MEET',
     'IF YOU WERE A MOVIE DIRECTOR, WHAT GENRE OF MOVIE WOULD YOU MAKE', 'WHICH COLOR BEST REFLECTS YOUR PERSONALITY AND WHY',
      'WHEN YOU GO TO THE ZOO, WHAT ANIMAL WOULD YOU MOST LIKE TO BE? WHY',
       'UNIVERSITY OR LIFE EXPERIENCE, WHICH DO YOU FEEL BEST PREPARES YOU FOR LIFE',
        'HOW WOULD YOU CONQUER THE EARTH', 'IF YOU COULD SEND A MESSAGE TO AN ALIEN SPECIES, WHAT WOULD IT BE',
         'WHAT ANIMAL WOULD YOU WANT TO BRING WITH YOU ON A JOURNEY', 'WHAT’S YOUR BEST KARAOKE SONG',
          'ARE THERE INAPPROPRIATE JOKES YOU CAN LAUGH ABOUT ALL DAY', 'WHAT’S THE FUNNIEST THING YOU DID BECAUSE YOU WERE BORED', 
          'WHAT’S THE WEIRDEST HABIT YOU HAD AS A CHILD', 'WHAT IS THE WORST PET YOU HAVE EVER HAD', 'WHAT DOES IT MEAN TO BE HUMAN', 
          'ARE HUMANS BETTER AT CREATION OR DESTRUCTION', 'IS LIFE UNFAIR', ' WHAT IS TRUE STRENGTH', ' IF YOU COULD DO ANYTHING YOU WANTED RIGHT NOW, WHAT WOULD IT BE',
           'WHAT’S THE CRAZIEST THING YOU HOPE TO DO ONE DAY', 'IF YOU COULD HAVE ANY CAREER, WHAT WOULD YOU CHOOSE', 
           'HOW IMPORTANT IS HONESTY TO YOU', 'WHAT IS YOUR EARLIEST MEMORY', 'WHAT SINGLE THING WOULD YOU CHANGE ABOUT THE WORLD IF YOU COULD']

thisorthattopic = ['BACON OR SAUSAGE', 'CHINESE OR JAPANESE FOOD', 'DOGS OR CATS', 'IOS OR ANDROID',
 'CAKE OR PIE', 'TRAIN OR PLANE', 'COFFEE OR TEA', 'BEER OR WINE', 'SOUP OR SANDWICH', 'CARD GAME OR BOARD GAME',
  ' MOTORCYCLE OR BICYCLE', 'BOOK OR EBOOK', 'NINJAS OR PIRATES', 'TV SHOWS OR MOVIES', 'WHAT’S WORSE: LAUNDRY OR DISHES', 
  'COUCH OR RECLINER', 'WORKING ALONE OR WORKING IN A TEAM', ' PERFECT TEETH OR PERFECT HAIR', 'ARCTIC OR THE DESERT', 
  'FOREST OR BEACH', ' THEME PARK OR WATER PARK', ' THEME PARK OR WATER PARK', 'AFRICA OR ASIA', 'CITY OR COUNTRY', 
  'ABS OR CHEST', 'LUST OR LOVE', 'WEIRD OR NORMAL', 'TRUTH OR DARE', 'TOUCH OR TASTE', 'FACEBOOK OR TWITTER', 
  'WHILE WALKING: MUSIC OR PODCASTS', 'BIG PARTY OR SMALL GATHERING', 'CLASSICAL ART OR MODERN ART', 'CURLY OR STRAIGHT',
   'SPRING OR FALL', 'CREDIT CARD OR CASH', 'MOBILE GAMES OR CONSOLE GAMES', 'ICED COFFEE OR HOT COFFEE', 'OCEAN OR MOUNTAINS',
    'HAMBURGER OR TACO', 'PASSENGER OR DRIVER']

personaltopic = ['What is your name ?', 'How old are you ?', 'Where are you from ?', 'Who is your hero?', 'If you could live anywhere, where would it be?', 'What is your biggest fear?',
 'What is your favorite family vacation?', 'What would you change about yourself if you could?', 'What really makes you angry?', 'What motivates you to work hard?', 'What is your favorite thing about your career?',
  'What is your biggest complaint about your job?', 'What is your proudest accomplishment?', "What is your child's proudest accomplishment?",
  'What is your favorite book to read?',
  'What makes you laugh the most?', 'What was the last movie you went to? What did you think?', 'What did you want to be when you were small?', 'What does your child want to be when he/she grows up?',
  'If you could choose to do anything for a day, what would it be?',
  'What is your favorite game or sport to watch and play?',
  'Would you rather ride a bike, ride a horse, or drive a car?', 'What would you sing at Karaoke night?', 'What two radio stations do you listen to in the car the most?', 'Which would you rather do: wash dishes, mow the lawn, clean the bathroom, or vacuum the house?',
   'If you could hire someone to help you, would it be with cleaning, cooking, or yard work?',
    'If you could only eat one meal for the rest of your life, what would it be?', 'Who is your favorite author?']

valoranttopic = ['What is the best map in your opinion ?', 'What team do you support ?', 'What is your favorite weapon ?', 'What is your highest rank ?', 'Do you prefer solo or squad ?',
 'What is your main agent ?', 'Do you use aim trainer ?', 'What was your best score in the game ?', 'Do you have any strategy for attacking ?',
  'Do you prefer to play support or duelist ?', 'What is your nick ?', 'Do you follow news ?']

wouldyourathertopic = ['Would you rather lose the ability to read or lose the ability to speak', 'Would you rather be in jail for a year or lose a year off your life', 'Would you rather always be 10 minutes late or always be 20 minutes early', 'Would you rather be able to talk to land animals, animals that fly, or animals that live under the water', 
'Would you rather have all traffic lights you approach be green or never have to stand in line again',
 'Would you rather give up all drinks except for water or give up eating anything that was cooked in an oven', 
 'Would you rather be able to see 10 minutes into your own future or 10 minutes into the future of anyone but yourself',
  'Would you rather have an easy job working for someone else or work for yourself but work incredibly hard', 'Would you rather be the first person to explore a planet or be the inventor of a drug that cures a deadly disease', 'Would you rather go back to age 5 with everything you know now or know now everything your future self will learn', 
  'Would you rather be able to control animals (but not humans) with your mind or control electronics with your mind', 'Would you rather have unlimited international first-class tickets or never have to pay for food at restaurants', 'Would you rather see what was behind every closed door or be able to guess the combination of every safe on the first try', 'Would you rather be able to dodge anything no matter how fast it’s moving or be able to ask any three questions and have them answered accurately', 'Would you rather be forced to dance every time you heard music or be forced to sing along to any song you heard', 'Would you rather be an unimportant character in the last movie you saw or an unimportant character in the last book you read', 
  'Would you rather move to a new city or town every week or never be able to leave the city or town you were born in', 'Would you rather travel the world for a year on a shoestring budget or stay in only one country for a year but live in luxury',
 'Would you rather live in virtual reality where you are all powerful or live in the real world and be able to go anywhere but not be able to interact with anyone or anything', 'Would you rather have whatever you are thinking to appear above your head for everyone to see or have absolutely everything you do live streamed for anyone to see', 'Would you rather wake up as a new random person every year and have full control of them for the whole year or once a week spend a day inside a stranger without having any control of them', ' Would you rather know how above or below average you are at everything or know how above or below average people are at one skill/talent just by looking at them', 'Would you rather live until you are 200 but look like you are 200 the whole time even though you are healthy or look like you are 25 all the way until you die at age 65',
  'Would you rather your only mode of transportation be a donkey or a giraffe', 'Would you rather only be to use a fork (no spoon) or only be able to use a spoon (no fork)', 'Would you rather have to read aloud every word you read or sing everything you say out loud',
 'Would you rather be unable to move your body every time it rains or not be able to stop moving while the sun is out',
  'Would you rather have all dogs try to attack you when they see you or all birds try to attack you when they see you',
   'Would you rather have skin that changes color based on your emotions or tattoos appear all over your body depicting what you did yesterday',
    'Would you rather there be a perpetual water balloon war going on in your city/town or a perpetual food fight', 'Would you rather have to fart loudly every time you have a serious conversation or have to burp after every kiss', 'Would you rather become twice as strong when both of your fingers are stuck in your ears or crawl twice as fast as you can run', 'Would you rather be a famous director or a famous actor', 'Would you rather be a practicing doctor or a medical researcher', 'Would you rather live in a cave or live in a tree house', ' Would you rather be able to control fire or water', 'Would you rather be able to teleport anywhere or be able to read minds', 'Would you rather be an amazing painter or a brilliant mathematician', 'Would you rather have a flying carpet or a car that can drive underwater', 'Would you rather never be stuck in traffic again or never get another cold', 'Would you rather be forced to eat only spicy food or only incredibly bland food',
  ' Would you rather be fantastic at riding horses or amazing at driving dirt bikes']


@client.event
async def on_ready() :
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="cnv-helpme"))

    print("Bot is ready")





@client.command()
async def general(message,lang = "en") :

    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    if lang == "tr" :
        r = 255
        g = 0
        b = 0
    channel = message.channel
    context = random.choice(generaltopic)
    translator = Translator()
    context = translator.translate(context,dest=lang)
    title = translator.translate("Lets talk about",dest=lang)
    embed = discord.Embed(timestamp=datetime.datetime.utcnow(), color=discord.Color.from_rgb(r,g,b))
    embed.add_field(name=title.text, value=context.text)


    await channel.send(embed=embed)


@client.command()
async def translate(message,lang, *,word) :


    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    if lang == "tr" :
        r = 255
        g = 0
        b = 0
    channel = message.channel
    contextt = word
    translator = Translator()
    contextt = translator.translate(word,dest=lang)
    title = f"{contextt.origin} ({contextt.src}) --> {contextt.text} ({contextt.dest})"
    embed = discord.Embed(timestamp=datetime.datetime.utcnow(), color=discord.Color.from_rgb(r,g,b))
    embed.add_field(name="Traslated", value=title)


    await channel.send(embed=embed)


@client.command()
async def question(message,lang = "en") :

    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    if lang == "tr" :
        r = 255
        g = 0
        b = 0
    channel = message.channel
    context = random.choice(questiontopic)
    translator = Translator()
    context = translator.translate(context,dest=lang)
    title = translator.translate("Your question is",dest=lang)
    embed = discord.Embed(timestamp=datetime.datetime.utcnow(), color=discord.Color.from_rgb(r,g,b))
    embed.add_field(name=title.text, value=context.text)
    await channel.send(embed=embed)







@client.command()
async def thisorthat(message,lang = "en") :

    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    if lang == "tr" :
        r = 255
        g = 0
        b = 0
    channel = message.channel
    context = random.choice(thisorthattopic)
    translator = Translator()
    context = translator.translate(context,dest=lang)
    title = translator.translate("This or that",dest=lang)
    embed = discord.Embed(timestamp=datetime.datetime.utcnow(), color=discord.Color.from_rgb(r,g,b))
    embed.add_field(name=title.text, value=context.text)
    await channel.send(embed=embed)





@client.command()
async def personal(message,lang = "en") :

    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    if lang == "tr" :
        r = 255
        g = 0
        b = 0
    channel = message.channel
    context = random.choice(personaltopic)
    translator = Translator()
    context = translator.translate(context,dest=lang)
    title = translator.translate("Let's get to know you",dest=lang)
    embed = discord.Embed(timestamp=datetime.datetime.utcnow(), color=discord.Color.from_rgb(r,g,b))
    embed.add_field(name=title.text, value=context.text)
    await channel.send(embed=embed)




@client.command()
async def wouldyourather(message,lang = "en") :

    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    if lang == "tr" :
        r = 255
        g = 0
        b = 0
    channel = message.channel
    context = random.choice(wouldyourathertopic)
    translator = Translator()
    context = translator.translate(context,dest=lang)
    title = translator.translate("Would you rather",dest=lang)
    embed = discord.Embed(timestamp=datetime.datetime.utcnow(), color=discord.Color.from_rgb(r,g,b))
    embed.add_field(name=title.text, value=context.text)
    await channel.send(embed=embed)


@client.command()
async def languages(message) :
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    channel = message.channel
    title = "Supported Languages"
    embed = discord.Embed(timestamp=datetime.datetime.utcnow(), color=discord.Color.from_rgb(r,g,b))
    embed.add_field(name=title, value='[Here !](https://cloud.google.com/translate/docs/languages)')
    await channel.send(embed=embed)
    

@client.command()
async def add(message) :
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    channel = message.channel
    title = "Add me to your server "
    embed = discord.Embed(timestamp=datetime.datetime.utcnow(), color=discord.Color.from_rgb(r,g,b))
    embed.add_field(name=title, value='[Here !](https://discord.com/api/oauth2/authorize?client_id=744956642214543362&permissions=84992&scope=bot)')
    await channel.send(embed=embed)


@client.command()
async def helpme(message) :
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    channel = message.channel
    title = "All Commands"
    xxx = "cnv-general [language] , to get general topics"+"\n"+"cnv-question [language] , to get interesting questions"+"\n"+"cnv-thisorthat [language] , to get this or that questions"+"\n"+"cnv-personal [language] , to get personal questions"+"\n"+"cnv-wouldyourather [language] , to get would you rather questions"+"\n"+"cnv-add , to add me"+"\n"+"cnv-translate [language] [sentence] , to translate sentences"+"\n"+"cnv-languages , to see supported languages"
    embed = discord.Embed(timestamp=datetime.datetime.utcnow(), color=discord.Color.from_rgb(r,g,b))
    embed.add_field(name=title, value=xxx)
    await channel.send(embed=embed)
    
@client.command()
async def botservers(ctx):
    await ctx.send("I'm in " + str(len(client.guilds)) + " servers")

client.run(token)
