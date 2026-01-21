import json
from lxml import etree as ET

def xml_to_dict(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    result = {}
    movies = []

    for movie_elem in root.findall('Movie'):
        movie_data = {}

        movie_data['rating'] = movie_elem.attrib['rating']

        for child in movie_elem:
            if child.tag == 'Title':
                title_data = {'text': child.text.strip()}
                if 'runtime' in child.attrib:
                    title_data['runtime'] = child.attrib['runtime']
                movie_data['Title'] = title_data

            elif child.tag == 'Director':
                director_data = {}
                name_elem = child.find('Name')
                name_data = {}
                if 'highratedmovie' in name_elem.attrib:
                    name_data['highratedmovie'] = name_elem.attrib['highratedmovie']
                name_data['First'] = name_elem.find('First').text.strip()
                name_data['Last'] = name_elem.find('Last').text.strip()
                director_data['Name'] = name_data
                movie_data['Director'] = director_data

            else:
                movie_data[child.tag] = child.text.strip()

        movies.append(movie_data)

    result['Movies'] = movies
    return result

movies_dict = xml_to_dict('movies.xml')
print(json.dumps(movies_dict, indent=2))

with open("file.txt", "w", encoding='utf-8') as f:
    json.dump(movies_dict, f, indent=2)