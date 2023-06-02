import glob
import discord
import json

# Create a subclass of Client and override its handler methods
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

        # Get the guild by ID
        guild = self.get_guild()
        
        # Get all JSON files from the directory
        files = glob.glob('htmls/*.json')

        for file in files:
            # Load data from JSON
            with open(file) as f:
                data = json.load(f)

            channel_name = data['channel']['name']
            channel = discord.utils.get(guild.channels, name=channel_name)

            # Create a new text channel
            # overwrites = {
            #     guild.default_role: discord.PermissionOverwrite(read_messages=False),
            #     guild.me: discord.PermissionOverwrite(read_messages=True)
            # }
            channel = guild.create_text_channel(data['channel']['name'], position=0 slowmode_delay=0, nsfw=False, reason=None)

            # Restore messages
            for msg in data['messages']:
                try:
                    channel.send(msg['content'])
                    time.sleep(1)
                except Exception as e:
                    print(e)

# Instantiate client
client = MyClient()
client.run('token')
