import soupsieve as BeautifulSoup
import regex as re
import glob
import json
import pathlib as path

files = glob.glob('htmls/*.html')

allData = []
for htmlName in files:
    if not path.exists(htmlName + ".json"):
        data = {}

        with open(htmlName + ".json", 'w') as file:
            json.dump(data, file)

    channel = htmlName.split("Communist Library - ")[1]
    data = {}
    html = open(html).read()
    soup = BeautifulSoup(html, 'html.parser')
    
    print(html)

    messages = soup.find_all(id='chatlog__message-container')

    for message in messages:
        content = message.find(id='chatlog__content')
        if content:
            content_lines = re.split('\*\n\*', content)
            for i, line in enumerate(content_lines):
                print(f"Content Line {i+1}: ", line)
                data["content"] = line
                data["channel"] = channel
                
    with open(htmlName + ".json", 'w') as file:
        json.dump(data, file)
