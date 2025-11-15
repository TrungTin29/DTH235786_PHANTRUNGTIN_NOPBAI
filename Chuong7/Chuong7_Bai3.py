'''
<?xml version="1.0" encoding="UTF-8" ?>
<employees>
<employee>
<id>1</id>
<name>Phan Trung Tin</name>
</employee>
<employee>
<id>2</id>
<name>Quách Thành Vũ</name>
</employee>
<employee>
<id>3</id>
<name>Khương Tiểu Soái</name>
</employee>
</employees>
'''

from xml.dom.minidom import parse
import xml.dom.minidom

DOMTree = xml.dom.minidom.parse("employees.xml")
collection = DOMTree.documentElement

empooyees = collection.getElementsByTagName("employee")

for employee in employees:
    tag_id = employee.getElementsByTagName('id')[0]
    id = tag_id.childNodes[0].data
    tag_name = employee.getElementsByTagName('name')[0]
    name = tag_name.childNodes[0].data
    print(id,'\t',name)
    

