import re
import requests
import xml.etree.ElementTree as ET
from html_to_markdown import convert

node = lambda x: "{http://www.w3.org/2005/Atom}"+x
bnode = lambda x: "{http://schemas.google.com/blogger/2018}"+x
title = lambda x: x.find(node("title")).text
content = lambda x: x.find(node("content")).text
date = lambda x: x.find(bnode("created")).text

t="""[<img src='https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEirhyAcq2gRzrU7dgvC97hp7tgEL63oXJ8g0LLdn9nGAZRlx0wnqVx9Ozkytx73-SGMgGZKSV0u0BJMi461pebdrRZxWWPd5k1s1uq5zeExjcIGF6RVFZI7fReiQb4HO1JUfCN6xNA9ma0vtyc8Deenp_BnHcrsLz4lDbQux7lt8zGpngKFGcVfSb5-Vf40/w320-h240/CCC.jpeg' alt='Photo by Troy Astarte' title='Photo by Troy Astarte' width='320' height='240' />](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEirhyAcq2gRzrU7dgvC97hp7tgEL63oXJ8g0LLdn9nGAZRlx0wnqVx9Ozkytx73-SGMgGZKSV0u0BJMi461pebdrRZxWWPd5k1s1uq5zeExjcIGF6RVFZI7fReiQb4HO1JUfCN6xNA9ma0vtyc8Deenp_BnHcrsLz4lDbQux7lt8zGpngKFGcVfSb5-Vf40/s1280/CCC.jpeg)

CCC in CoFo: Photo by Troy Astarte

[<img src='https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgJkILSbbSYQ0xAeieJZ991w5f20EGjhlqlBEO9cEufFxEmV51IytqSUOCrlV986FtEHGfEVCjaMhTlVsGMrZiNeClIB7T4PiIBDTIPJhudKNXjUWrgSKqzmB5tmg9M6jJQL4NsAnzXnQapD83_-6wR66ykL6sfj_JGch9LWDpBKxyxocGh7gdyFSD3l1e2/w320-h148/CCC2025-Excursion.jpg' alt='Photo by Olga Petrovska' title='Photo by Olga Petrovska' width='320' height='148' />](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgJkILSbbSYQ0xAeieJZ991w5f20EGjhlqlBEO9cEufFxEmV51IytqSUOCrlV986FtEHGfEVCjaMhTlVsGMrZiNeClIB7T4PiIBDTIPJhudKNXjUWrgSKqzmB5tmg9M6jJQL4NsAnzXnQapD83_-6wR66ykL6sfj_JGch9LWDpBKxyxocGh7gdyFSD3l1e2/s4000/CCC2025-Excursion.jpg)

CCC in Langland Bay: Photo by Olga Petrovska
"""

def replace_images(content: str) -> str:
    content = convert(content)
    output = []
    for line in content.split("\n"):
        if line.startswith("[<img "):
            url = re.findall("\\(.*?\\)$", line)[0][1:-1]
            filename = f"../assets/{url.split('/')[-1]}"
            try:
                with open(filename, "wb") as f:
                    f.write(requests.get(url).content)
                filename = filename.replace("../assets/", "")
            except:
                filename = url
            alt = re.findall("alt=\'.*?\'", line)[0].replace("alt=\'", "")[:-1]
            line = "![" + alt + "](" + filename + ")"
            line = re.sub("\\(<img.*?>\\]", "", line)
        output.append(line)
    return "\n".join(output)
    

def clean_content(content: str) -> str:
    content = re.sub("<p.*?>", "", content)
    content = re.sub("&nbsp;", "\n\n", content)
    content = content.replace("</p>", "\n\n")
    content = replace_images(content)
    return content

def write_blog_post(blogger_item, output_location = ""):
    if title(blogger_item) is not None:
        d = date(blogger_item).split("T")[0]
        #print(f"Writing {output_location}/{d}.md")
        with open(f"{output_location}/{d}.md", "w") as text_file:
            text_file.write(f"""---
title: \"{title(blogger_item)}\"
date: {d}
---

{clean_content(content(blogger_item))}
""")

tree = ET.parse("feed.atom")
root = tree.getroot()

for blog_post in root.iter(node("entry")):
    write_blog_post(blog_post, output_location="../content/posts/")

