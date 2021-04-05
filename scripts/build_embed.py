import discord

def buildApexStatus(status):
  servers = {"EA_novafusion":"EA Servers","EA_accounts":"EA Accounts","ApexOauth_Crossplay":"Apex Servers"}
  servers_loc = ["US-East", "US-Central"]
  embedVar = discord.Embed(title="Apex Legends Status", description="Current server status for Apex Legends", color=0xe74c3c, url="https://apexlegendsstatus.com")
  embedVar.set_thumbnail(url="https://apexlegendsstatus.com/assets/layout/apexlogo.png")

  for s in servers:
    embedVar.add_field(name="-----------------------", value="\n\u200b", inline=False)
    embedVar.add_field(name=servers[s],value="-", inline=False)
    for l in servers_loc:
      val_str = "**"+str(status[s][l]["HTTPCode"])+"**"
      val_str = val_str + " | *Status* - **" + str(status[s][l]["Status"])
      val_str = val_str + "** | *Response Time* - **" + str(status[s][l]["ResponseTime"])+"**"
      embedVar.add_field(name=l.replace("-", " "), value=val_str, inline=False)

  return embedVar