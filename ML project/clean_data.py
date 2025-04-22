import os
import xml.etree.ElementTree as ET

#Map Labels to indices
classes = {"Handgun":0, "Short_rifle":1, "Knife":2}

#Path
original_dir = "/Users/grace/Desktop/Data/Original" #Replace with path to data on device

def convert(size, box):
    """"Takes the size of the image, and the box
    (contiaing x min, y min, x max, y max). Returns normalized bounding box (x_center, y_center, width, height)"""
    dw, dh = 1. / size[0], 1. / size[1]
    x = (box[0] + box[2]) / 2.0
    y = (box[1] + box[3]) / 2.0
    w = box[2] - box[0]
    h = box[3] - box[1]
    return (x * dw, y * dh, w * dw, h * dh)


for xml_file in os.listdir(original_dir):
    if xml_file.endswith("xml"):
        try:
            tree = ET.parse(os.path.join(original_dir, xml_file))
            root = tree.getroot()
            size = root.find('size')
            w = int(size.find('width').text)
            h = int(size.find('height').text) 
        
            label_file = os.path.join(original_dir, xml_file.replace(".xml",".txt"))
        
            with open(label_file, "w") as f:
                for obj in root.iter('object'):
                    cls_name = obj.find('name').text.strip()
                    cls_id = classes[cls_name]
                    xmlbox = obj.find('bndbox')
                    b = (float(xmlbox.find('xmin').text),
                        float(xmlbox.find('ymin').text),
                        float(xmlbox.find('xmax').text),
                        float(xmlbox.find('ymax').text))
                    bb = convert((w, h), b)
                    f.write(f"{cls_id} {' '.join([str(a) for a in bb])}\n")
                
        except ET.ParseError as e:
            print(e)

