import discord

g4TxtPerms = discord.PermissionOverwrite(create_instant_invite=False,
                                         read_messages=True,
                                         send_messages=True,
                                         manage_channels=True,
                                         add_reactions=True,
                                         send_tts_messages=False,
                                         manage_messages=True,
                                         embed_links=True,
                                         attach_files=True,
                                         read_message_history=True,
                                         mention_everyone=True,
                                         external_emojis=True,
                                         manage_roles=False,
                                         manage_webhooks=False
                                         )

g4VocalPerms = discord.PermissionOverwrite(create_instant_invite=False,
                                           manage_roles=False,
                                           manage_webhooks=False,
                                           manage_channels=True,
                                           priority_speaker=False,
                                           stream=True,
                                           view_channel=True,
                                           connect=True,
                                           speak=True,
                                           mute_members=True,
                                           use_voice_activation=True,
                                           steam=True
                                           )
