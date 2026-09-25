import xml.etree.ElementTree as ET

students = ET.Element("students")

student1 = ET.SubElement(students, "student")

ET.SubElement(student1, "id").text = "101"
ET.SubElement(student1, "name").text = "Rahul"
ET.SubElement(student1, "course").text = "Python"

student2 = ET.SubElement(students, "student")

ET.SubElement(student2, "id").text = "102"
ET.SubElement(student2, "name").text = "Priya"
ET.SubElement(student2, "course").text = "Java"

tree = ET.ElementTree(students)

tree.write("students.xml")