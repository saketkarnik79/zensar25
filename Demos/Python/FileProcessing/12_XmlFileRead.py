import xml.etree.ElementTree as ET

tree = ET.parse("students.xml")

root = tree.getroot()

for student in root.findall("student"):

    student_id = student.find("id").text
    name = student.find("name").text
    course = student.find("course").text

    print(student_id, name, course)