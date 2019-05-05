## read dcm  file's metadata and print 

import os
import pydicom

def myprint(dataset, indent=0):
    """Go through all items in the dataset and print them with custom format
    Modelled after Dataset._pretty_str()
    """
    dont_print = ['Pixel Data', 'File Meta Information Version']

    indent_string = "   " * indent
    next_indent_string = "   " * (indent + 1)

    for data_element in dataset:
        if data_element.VR == "SQ":   # a sequence
            print(indent_string, data_element.name)
            for sequence_item in data_element.value:
                myprint(sequence_item, indent + 1)
                print(next_indent_string + "---------")
        else:
            if data_element.name in dont_print:
                print("""<item not printed -- in the "don't print" list>""")
            else:
                repr_value = repr(data_element.value)
                if len(repr_value) > 50:
                    repr_value = repr_value[:50] + "..."
                print("{0} {1:s} {2:s} = {3:s}".format(data_element.tag,indent_string,
                                                   data_element.name,
                                                   repr_value))


# ds2 = pydicom.dcmread('MR-MONO2-8-16x-heart')
ds2 = pydicom.dcmread('pic/MR-MONO2-16-head')

ds2.PatientName
ds2.Modality
ds2.StudyDescription 

print('Modality:'+ds2.Modality) 
myprint(ds2)

print('-----dataset metadata:----')
print(ds2)
