import discord
from collections import OrderedDict
import json
import random
import copy

def emoji(ctx, name):
    name = name.replace('.','').lower().replace(' ','').replace('_','').replace('-','')
    if name == 'chestmagic':
        name = 'chestmagical'
    e = discord.utils.get(ctx.bot.game_emojis, name=name)
    return e

def cdir(obj):
    return [x for x in dir(obj) if not x.startswith('_')]

def random_color():
    return random.randint(0, 0xFFFFFF)

async def format_profile(ctx, name, p):
    embeds = []
    if p["competitive"]:
        em = discord.Embed(color=random_color(), title='Competitive')
        try:
            em.set_author(name=name, icon_url=p['competitive']['overall_stats']['avatar'])
        except:
            em.set_author(name=name)

        em.set_thumbnail(url=p['competitive']['overall_stats']['rank_image'])
        tier = p["competitive"]["overall_stats"]["tier"] or "none"

        embed_fields = [
            ('Level', p['competitive']['overall_stats']['prestige']*100+p['competitive']['overall_stats']['level'], True),
            ('Win-Loss-Draw', f"{p['competitive']['overall_stats']['wins']}-{p['competitive']['overall_stats']['losses']}-{p['competitive']['overall_stats']['ties']}", True),
            ('Games Played', p['competitive']['overall_stats']['games'], True),
            ('Win Rate', str(p['competitive']['overall_stats']["win_rate"]), True),
            ("Tier", tier.title(), True)
            ("Kills", str(p["competitive"]["game_stats"]["eliminations"]), True),
            ("Top Kills in a Game", str(p["competitive"]["game_stats"]["eliminations_most_in_game"]), True),
            ("Solo Kills", str(p["competitive"]["game_stats"]["solo_kills"]), True),
            ("Final Blows", str(p["competitive"]["game_stats"]["final_blows"]), True),
            ("Deaths", str(p["competitive"]["game_stats"]["deaths"]), True),
            ("K/D", str(p["competitive"]["game_stats"]["kpd"]), True),
            ("Gold Medals", str(p["competitive"]["game_stats"]["medals_gold"]), True),
            ("Silver Medals", str(p["competitive"]["game_stats"]["medals_silver"]), True)
            ]

        for n, v, i in embed_fields:
            if v:
                em.add_field(name=n, value=v, inline=i)

        embeds.append(em)
    em = discord.Embed(color=random_color(), title='Quickplay')
    try:
        em.set_author(name=name, icon_url=p['quickplay']['overall_stats']['avatar'])
    except:
        em.set_author(name=name)

    em.set_thumbnail(url=p['quickplay']['overall_stats']['rank_image'])
    tier = p["quickplay"]["overall_stats"]["tier"] or "none"

    embed_fields = [
        ('Level', p['quickplay']['overall_stats']['prestige']*100+p['quickplay']['overall_stats']['level'], True),
        ('Wins', f"{p['quickplay']['overall_stats']['wins']}", True),
        ('Games Played', p['quickplay']['overall_stats']['games'], True),
        ("Tier", tier.title(), True),
        ("Kills", str(p["quickplay"]["game_stats"]["eliminations"]), True),
        ("Top Kills in a Game", str(p["quickplay"]["game_stats"]["eliminations_most_in_game"]), True),
        ("Solo Kills", str(p["quickplay"]["game_stats"]["solo_kills"]), True),
        ("Final Blows", str(p["quickplay"]["game_stats"]["final_blows"]), True),
        ("Deaths", str(p["quickplay"]["game_stats"]["deaths"]), True),
        ("K/D", str(p["quickplay"]["game_stats"]["kpd"]), True),
        ("Gold Medals", str(p["quickplay"]["game_stats"]["medals_gold"]), True),
        ("Silver Medals", str(p["quickplay"]["game_stats"]["medals_silver"]), True)
        ]

    for n, v, i in embed_fields:
        if v:
            em.add_field(name=n, value=v, inline=i)

    embeds.append(em)
    return embeds
