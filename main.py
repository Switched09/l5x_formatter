import xml.dom.minidom
import xml.etree.ElementTree as ET

# Define file paths
input_file = "~/Documents/PLC_Program/Pembina_ENT_SITE_L73_L5X_File.L5X"  # Replace with actual file path
output_file = "~/Documents/PLC_Program/Pembina_ENT_SITE_L73_L5X_File_Ident.L5X"  # Replace with actual file path

try:
    # Read and parse the XML content
    tree = ET.parse(input_file)
    root = tree.getroot()

    # Convert XML to a properly formatted string
    rough_string = ET.tostring(root, encoding="utf-8")
    formatted_xml = xml.dom.minidom.parseString(rough_string).toprettyxml(indent="    ")  # 4 spaces

    # Save formatted XML to the output file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(formatted_xml)

    print(f"Formatted .L5X file saved to: {output_file}")

except Exception as e:
    print(f"Error processing the L5X file: {e}")
