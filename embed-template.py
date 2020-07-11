
###############
# Help {name} #
###############

Embed = discord.Embed(title="{name}",
                      color=0xEE8700,
                      description="",
                      )

Embed.add_field(name="Quèsaco ?",
                value="{description}",
                inline=False
                )

Embed.add_field(name="Commande",
                value="{description de la commande}",
                inline=False
                )

Embed.add_field(name="Tuto",
                value="{lien vers un ou des tutos}",
                inline=False
                )
