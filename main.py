import xml.dom.minidom
import xml.etree.ElementTree as ET

def format_l5x(input_file, output_file):
    try:
        # Read and parse the XML content
        tree = ET.parse(input_file)
        root = tree.getroot()

        # Convert XML to a formatted string
        rough_string = ET.tostring(root, encoding="utf-8")
        dom = xml.dom.minidom.parseString(rough_string)

        # Properly format XML without extra blank lines
        formatted_xml = "\n".join([line for line in dom.toprettyxml(indent="    ").split("\n") if line.strip()])

        # Save formatted XML to the output file
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(formatted_xml)

        print(f"Formatted .L5X file saved to: {output_file}")


    except Exception as e:
        print(f"Error processing the L5X file: {e}")

# Example usage
input_file =  "/home/user/Documents/PLC_Program/PLC_Program_L5X_File.L5X"          # Path for the Original L5X file
output_file = "/home/user/Documents/PLC_Program/PLC_Program_L5X_File_Ident.L5X"    # Path for the Idented L5X file
format_l5x(input_file, output_file)
