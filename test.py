# This is a written example used to test and debug the state of v4.0
import interactions

TOKEN = "stop drinking gfuel it sucks."

client = interactions.Client(token=TOKEN)


@client.event
async def on_ready():
    print(f"{client.me.username}#{client.me.discriminator} logged in.")

    # await client.http.request(
    #     Route("POST", "/applications/883788893512683520/guilds/852402668294766612/commands"),
    #     json={"type": 1, "name": "digiorno", "description": "v4.0.0 baby!"},
    # )


@client.command(name="test", description="my balls", scope=789032594456576001)
async def command_name(ctx):
    print(f"making sure: {ctx}")
    print(dir(ctx))
    print(ctx.author._json)


client.start()