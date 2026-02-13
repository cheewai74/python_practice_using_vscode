'''
To write an ElementTree object back to an XML string or file, you can use
ET.tostring or ET.ElementTree.write.
'''

import xml.etree.ElementTree as ET

xml_data = '''
<person>
    <name>John</name>
    <age>32</age>
    <children>
        <child>Sam</child>
        <child>Chloe</child>
    </children>
    <job>Developer</job>
</person>
'''
root = ET.fromstring(xml_data)
xml_string = ET.tostring(root, encoding='unicode')
print(xml_string)

tree = ET.ElementTree(root)
with open('data.xml','wb') as file:
    tree.write(file, encoding='utf-8', xml_declaration=True)