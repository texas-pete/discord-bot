import discord

#Setup and run client
client = discord.Client()


@client.event
async def on_message(message):
    serverID = client.get_guild(595026841979584533)  # bind server ID to variable
    if message.content =="&hello":
        await message.channel.send("Hello, traveler") #if user says hello, send this message
    if message.content == "&praise":
        await message.channel.send("Praise the sun!") #if users says praise, praise the sun
    if message.content == "&users":
        await message.channel.send(f"""Number of members: {serverID.member_count}""") #output number of members in server
    if message.content == "&help":
        embed = discord.Embed(title="Help with Solaire", description="Solaire's current commands")
        embed.add_field(name="&hello", value = "greets the user")
        embed.add_field(name="&praise", value="praise the sun!")
        embed.add_field(name="&users", value="reports number of users currently in server ")
        await message.channel.send(content=None, embed = embed)


print("Bot running")
client.run("NTk1MDgwMTU0NDA2MDYwMDY2.XRlyJQ.7x_Ork2ktr_moEfTbfN2CVltpeE")
