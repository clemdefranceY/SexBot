import discord 
import random

token = "DISCORD_TOKEN"

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_message(message):
    if message.content == "!verite":
        Verd = random.randint(0,12)
        if Verd == 1:
            await message.channel.send("Aimerais-tu faire un jeu de rôle sexuel ?")
        if Verd == 2:
            await message.channel.send("Aimerais-tu essayer le libertinage ?")
        if Verd == 3:
           await message.channel.send("As-tu déjà été attaché pendant que tu faisais l'amour ?")
        if Verd == 4:
           await message.channel.send("Quelle partie du corps préfères-tu chez ton ami ?")
        if Verd == 5:
           await message.channel.send("Quel est ton plus gros fantasme ?")
        if Verd == 6:
           await message.channel.send("Quelle est la personne avec laquelle tu as eu le plus de plaisir au lit ?")
        if Verd == 7:
           await message.channel.send("As-tu déjà eu une relation homosexuelle ou lesbienne?")
        if Verd == 8:
           await message.channel.send("Avec combien de personnes as-tu déjà couché ?")
        if Verd == 9:
           await message.channel.send("Quand as-tu fait l'amour pour la dernière fois ?")
        if Verd == 10:
           await message.channel.send("Quel est l'endroit le plus étrange dans lequel tu as eu des relations sexuelles ?")
        if Verd == 11:
           await message.channel.send("Quelle est ta position sexuelle préférée ?")
        if Verd == 12:
           await message.channel.send("Est-ce que tu as déjà été dérangé(e) par quelqu'un pendant que tu faisais l'amour ?")
    if message.content == "!action":
        acd = random.randint(0,12)
        if acd == 1: 
          await message.channel.send("Faites l'amour en position des petites cuillères")
        if acd == 2: 
          await message.channel.send("Lèche les tétons de ton ami avec un glaçon dans la bouche")
        if acd == 3: 
          await message.channel.send("Embrasse langoureusement ton ami")
        if acd == 4: 
          await message.channel.send("Fais tout ce que ton ami t'ordonne pendant les 5 prochaines minutes")
        if acd == 5: 
          await message.channel.send("Guide les mains de ton ami sur ton corps")
        if acd == 6: 
         await message.channel.send("Réalise une position du Kamasutra")
        if acd == 7: 
          await message.channel.send("Faites l'amour en levrette")
        if acd == 8: 
          await message.channel.send("Gémis aussi fort que tu peux sans rigoler.")
        if acd == 9: 
          await message.channel.send("Choisis une couleur d'un vêtement que tu portes. Tous les joueurs doivent retirer tout vêtement de cette couleur pendant 2 tours.")
        if acd == 10: 
          await message.channel.send("Fais une lap-danse pendant 10 secondes au joueur en face de toi.")
        if acd == 11: 
            await message.channel.send("Supplie la personne à ta gauche de te donner une fessée.")
        if acd == 12: 
           await message.channel.send("Laisse un autre joueur te faire un suçon où il veut.")

    if message.content == "!nude":
       nud = random.randint(0,12)
       if nud == 1: 
        with open('nude/1.png', 'rb') as a:
            pic1 = discord.File(a)
            await message.channel.send(file=pic1)
       if nud == 2: 
        with open('nude/2.png', 'rb') as b:
          pic2 = discord.File(b)
        await message.channel.send(file=pic2)
       if nud == 3: 
        with open('nude/3.png', 'rb') as c:
          pic3 = discord.File(c)
        await message.channel.send(file=pic3)
       if nud == 4: 
        with open('nude/4.png', 'rb') as d:
          pic4 = discord.File(d)
        await message.channel.send(file=pic4)
       if nud == 5: 
        with open('nude/5.png', 'rb') as e:
          pic5 = discord.File(e)
        await message.channel.send(file=pic5)         
       if nud == 6: 
        with open('nude/6.png', 'rb') as f:
          pic6 = discord.File(f)
        await message.channel.send(file=pic6)
       if nud == 7: 
        with open('nude/7.png', 'rb') as g:
          pic7 = discord.File(g)
        await message.channel.send(file=pic7)
       if nud == 8: 
        with open('nude/8.png', 'rb') as h:
          pic8 = discord.File(h)
        await message.channel.send(file=pic8)
       if nud == 9: 
        with open('nude/9.png', 'rb') as i:
          pic9 = discord.File(i)
        await message.channel.send(file=pic9)
       if nud == 10: 
        with open('nude/10.png', 'rb') as j:
          pic10 = discord.File(j)
        await message.channel.send(file=pic10)
       if nud == 11: 
        with open('nude/11.png', 'rb') as k:
          pic11 = discord.File(k)
        await message.channel.send(file=pic11)
       if nud == 12: 
        with open('nude/12.png', 'rb') as l: 
            pic12 = discord.File(l)
            await message.channel.send(file=pic12)

client.run(token=token)