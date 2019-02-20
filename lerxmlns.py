import xml.etree.ElementTree as ET

tree = ET.parse('ns.xml')

root = tree.getroot()

print(root.tag)


# ns = {'real_person': 'http://people.example.com',
#       'role': 'http://characters.example.com'}

# for actor in root.findall('real_person:actor', ns):
#     name = actor.find('real_person:name', ns)
#     print(name.text)
#     for char in actor.findall('role:character', ns):
#         print(' |-->', char.text)

nsmap = {}
# for event, elem in ET.iterparse('ns.xml'):
#     print(elem[0])

# for event, elem in ET.iterparse('ns.xml',['end']):
#      print(elem[1])


for event, elem in ET.iterparse('ns.xml',['end', ]):
    print(event, elem.text)