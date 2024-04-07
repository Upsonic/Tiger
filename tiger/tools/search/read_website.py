import requests

from bs4 import BeautifulSoup
import re


def read_website(url: str, max_content_lenght: int = 5000) -> dict:
    html = requests.get(url).text
    soup = BeautifulSoup(html)
    meta_properties = [
        "og:description",
        "og:site_name",
        "og:title",
        "og:type",
        "og:url",
    ]
    meta = {}
    for property_name in meta_properties:
        try:
            tag = soup.find("meta", property=property_name)
            if tag:
                meta[property_name] = str(tag.get("content", None))
        except AttributeError:
            meta[property_name] = None
    for ignore_tag in soup(["script", "style"]):
        ignore_tag.decompose()
    title = soup.title.string if soup.title else ""
    content = soup.body.get_text() if soup.body else ""
    links = []
    for a in soup.find_all("a", href=True):
        links.append({"title": a.text.strip(), "link": a["href"]})
    content = re.sub(r"[\n\r\t]+", "\n", content)
    content = re.sub(r" +", " ", content)
    content = re.sub(r"[\n ]{3,}", "\n\n", content)
    content = content.strip()
    return {"meta": meta, "title": title, "content": content[:max_content_lenght], "sub_links": links}



tool_name = "search.read_website"
tool_obj = read_website
tool_requirements = ["beautifulsoup4==4.12.3", "requests"]