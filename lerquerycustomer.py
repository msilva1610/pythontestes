import xml.etree.ElementTree as ET

tree = ET.parse('QueryCustomerPartyResponseEBM.xml')

root = tree.getroot()

# print(root.tag)
# print(root.attrib)

# for child in root:
#     print(child.tag, child.attrib)

# print([elem.tag for elem in root.iter()])

for elem in root.iter():
    print(elem.tag)

# {http://www.sky.com.br/ArchitectureSchemas}returnMessage

s = '{http://www.sky.com.br/ArchitectureSchemas}returnMessage'
for i in root.iter(s):
    # print(i.attrib)
    # print(i.tag)
    print(i.text)
