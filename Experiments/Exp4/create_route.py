def create_roufile():
    xml_content = """<?xml version="1.0" encoding="UTF-8"?>
<routes>
    <!-- You can add your specific XML nodes and data here -->
</routes>
"""

    with open("test.rou.xml", "w") as file:
        file.write(xml_content)

if __name__ == "__main__":
    create_roufile()