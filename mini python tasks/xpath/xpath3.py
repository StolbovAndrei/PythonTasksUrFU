import json

def parse_bibtex(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    entries = {}
    current_key = None
    current_fields = {}
    
    for line in lines:
        line = line.strip()
        if line.startswith('@article{'):
            key = line.split('{')[1].split(',')[0]
            current_key = key
            current_fields = {}
        elif line.endswith('},'):
            if current_key:
                entries[current_key] = {
                    'type': 'article',
                    'fields': current_fields
                }
        elif '=' in line and current_key:
            field, value = line.split('=', 1)
            field = field.strip()
            value = value.strip(' {}')
            current_fields[field] = value
    
    return {'entries': entries}

bib_dict = parse_bibtex('references.bib')
print(json.dumps(bib_dict, indent=2))