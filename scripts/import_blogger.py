import re
import xml.etree.ElementTree as ET

node = lambda x: "{http://www.w3.org/2005/Atom}"+x
bnode = lambda x: "{http://schemas.google.com/blogger/2018}"+x
title = lambda x: x.find(node("title")).text
content = lambda x: x.find(node("content")).text
date = lambda x: x.find(bnode("created")).text

def clean_content(content: str) -> str:
    content = re.sub("<p.*?>", "", content)
    content = re.sub("&nbsp;", "\n\n", content)
    return (
        content
        .replace("</p>", "\n\n"))

def write_blog_post(blogger_item, output_location = ""):
    if title(blogger_item) is not None:
        d = date(blogger_item).split("T")[0]
        print(f"Writing {output_location}/{d}.md")
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

