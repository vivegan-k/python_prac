#From a given input json (nested json), create a list of all keys and another list of all values
d1 = {
"problems": [{
    "Diabetes":[{
        "medications":[{
            "medicationsClasses":[{
                "className":[{
                    "associatedDrug":[{
                        "name":"asprin",
                        "dose":"",
                        "strength":"500 mg"
                    }],
                    "associatedDrug#2":[{
                        "name":"somethingElse",
                        "dose":"",
                        "strength":"500 mg"
                    }]
                }],
                "className2":[{
                    "associatedDrug":[{
                        "name":"asprin",
                        "dose":"",
                        "strength":"500 mg"
                    }],
                    "associatedDrug#2":[{
                        "name":"somethingElse",
                        "dose":"",
                        "strength":"500 mg"
                    }]
                }]
            }]
        }],
        "labs":[{
            "missing_field": "missing_value"
        }]
    }],
    "Asthma":[{}]
}]}


def nested_json(d1, keys=[], values=[]):
    print(d1)
    for key, value in d1.items():
        keys.append(key)
        if type(value) is list:
            for val in value:
                if type(val) is dict:
                    nested_json(val,keys, values)
        elif type(value) is dict:
            nested_json(d1[key],keys, values)
        else:
            values.append(value)
    return keys, values

print(nested_json(d1))
    
