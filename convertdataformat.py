import json
import xmltodict
from pprint import pprint

import yaml

import collections

def deep_convert_dict(layer):
    to_ret = layer
    if isinstance(layer, collections.OrderedDict):
        to_ret = dict(layer)

    try:
        for key, value in to_ret.items():
            if isinstance(value,list):
                    newvalue= []
                    for x in value:
                        newvalue.append(deep_convert_dict(x))
                    value= newvalue
            to_ret[key] = deep_convert_dict(value)
    except AttributeError:
        pass

    return to_ret

xmldoc='''
<breakfast_menu>
	<food>
		<name>Belgian Waffles</name>
		<price>$5.95</price>
		<description>
Two of our famous Belgian Waffles with plenty of real maple syrup
</description>
		<calories>650</calories>
	</food>
	<food>
		<name>French Toast</name>
		<price>$4.50</price>
		<description>
Thick slices made from our homemade sourdough bread
</description>
		<calories>600</calories>
	</food>
	<food>
		<name>Homestyle Breakfast</name>
		<price>$6.95</price>
		<description>
Two eggs, bacon or sausage, toast, and our ever-popular hash browns
</description>
		<calories>950</calories>
	</food>
</breakfast_menu>
'''

pythonstruct = dict(xmltodict.parse(xmldoc))

# remove ordered dict

jsonstruct= json.dumps(pythonstruct, sort_keys=True, indent=4, separators=(',', ': '))

yamlstruct= yaml.safe_dump(deep_convert_dict(pythonstruct), default_flow_style=False)

struct= [pythonstruct,jsonstruct,yamlstruct]

for i in struct:
    print(i)
    print('###')

import ipdb; ipdb.set_trace()
