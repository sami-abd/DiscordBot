import discord
import responses

async def send_message(message, user_message, is_direct_message):
    try:
        
        response = responses.handle_response(user_message)
        if response:
            await message.author.send(response) if is_direct_message else await message.channel.send(response)

    except Exception as e:
        print(e)
       
def run_discord_bot():
    
    
    TOKEN = input('Enter your Bot\'s token found in the Bot section on discord.com: ')
    client = discord.Client(intents=discord.Intents.all())
    
    @client.event
    async def on_ready():
        print(f'{client.user} is functional!')
    
    @client.event
    async def on_message(message):
        #Makes sure bot doesnt repond to itself and causes an infinite loop
        #collecting user data
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        
        if message.author == client.user:
            print(f"(BOT) {username} said: '{user_message}' ({channel})")
            return 
        
        # Debug printing
        print(f"{username} said: '{user_message}' ({channel})")
        
        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_direct_message=True)
        else:
            await send_message(message, user_message, is_direct_message=False)

    client.run(TOKEN)