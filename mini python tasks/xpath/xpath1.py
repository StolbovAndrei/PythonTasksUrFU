from lxml import etree as ET

tree = ET.parse('movies.xml')
root = tree.getroot()

movies_runtime = {}
for movie in root.xpath('//Movie'):

    title_elem = movie.xpath('./Title')[0]
    runtime_attr = title_elem.get('runtime')
    
    title_text = movie.xpath('./Title/text()')
    
    if runtime_attr and title_text:
        movies_runtime[title_text[0].strip()] = runtime_attr.strip()

print(movies_runtime)