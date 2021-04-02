from linebot.models import (
    QuickReplyButton, URIAction   
)

def facilities():
  places = ['令和市民大学', '令和市みらいの文化センター', 'ふぃろと愉快な仲間たち', '令和市note直通特急', '思考の渦', 'ゆかりの部屋', '令和他力本願寺',  '蟹家飯店', '令和市郵便局', '令和市立病院', '【DDD】', 'しさく公園', '令和市デジタル庁澪標研究棟']

  urls = ['https://line.me/ti/g2/27Ul0_tr-YyDMHIgzCS7Ow', 'https://line.me/ti/g2/7DHG49ErBIh5npZ_gZd5jw', 'https://line.me/ti/g2/XvISahCX8Yt0b6TPTC1DPA', 'https://line.me/ti/g2/1fG-xDlclF4CXt-8k3n_jQ', 'https://discord.gg/A6NbcNnFY6', 'https://line.me/ti/g2/x3tNKIam9FfbcR7LgR980Q', 'https://line.me/ti/g2/tl4x1jhp7wuJovem38W8yw',  'https://line.me/ti/g2/ug0rKcEWvPtiOVj2u-P3hw', 'https://line.me/ti/g2/Jl9udQeJtpSZaNs5OGsONg', 'https://line.me/ti/g2/aPdxTIf03gvb9_g-gqMpXQ', 'https://line.me/ti/g2/BXMu9SDB6ow8DIACeLsnzQ', 'https://line.me/ti/g2/W4k67QKcAi36NfciiTsDpg', 'https://line.me/ti/g2/6ZT9AW-wGagQ8cfiMkm3DQ']

  items = [QuickReplyButton(
        action=URIAction(
            label=f"{place}", uri=f"{url}"
            )
        ) for place, url in zip(places, urls)]
  return items
