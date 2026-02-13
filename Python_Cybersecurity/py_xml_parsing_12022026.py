import xml.etree.ElementTree as ET

xml_data = '''
<person>
    <name>John</name>
    <age>30</age>
    <city>Singapore</city>
    <children>
        <child>Sam</child>
        <child>Chloe</child>
    </children>
</person>
'''

root = ET.fromstring(xml_data)
print("============== Root Tag ==========================")
print(root.tag)
print("============== Name Element ==========================")
print(root.find('name').text)


# Adding new element
job = ET.SubElement(root, 'job')
job.text = 'Developer'
print(root.find('job').text)

# Update an existing element
root.find('age').text = '32'
print(root.find('age').text)

# Remove an element
city = root.find('city')
root.remove(city)

# Print modified xml
print("============== Print modified xml ==========================")
ET.dump(root)