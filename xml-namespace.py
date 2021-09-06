
import xmltodict
import pprint
import json

with open('person.xml') as fd:
    doc = xmltodict.parse(fd.read(), process_namespaces=True)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(json.dumps(doc))
