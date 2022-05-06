import easyocr
import json
from pylab import rcParams
from IPython.display import Image
rcParams['figure.figsize'] = 8, 16\

reader = easyocr.Reader(['en'])
#Image("sample.png") 

def scan():
    output = reader.readtext('sample.png')
    name = output[4][-2]
    dob = output[5][-2][19:]
    gender = output[6][-2][6:]
    adhaarNo = output[7][-2]
    nadhaar = []
    for i in adhaarNo:
        if(i.isnumeric()==True):
            nadhaar.append(i)
    adhaarstr = ''.join(nadhaar)
    thisdict = {
                "Name": name ,
                "DoB": dob,
                "Gender": gender,
                "Adhaar No": adhaarstr
               }
    json_object = json.dumps(thisdict, indent = 0) 
    with open("output.json", "w") as outfile:
        outfile.write(json_object)           
    print(thisdict)           
