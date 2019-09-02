import xml.etree.ElementTree as ET

#XML 
tree = ET.parse('hk_Resp.xml')
root = tree.getroot()
child = root.getchildren()

for child in root:
    print(child.value(response)