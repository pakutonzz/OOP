record_collection = {
  2548: {
    'albumTitle': 'Slippery When Wet',
    'artist': 'Bon Jovi',
    'tracks': ['Let It Rock', 'You Give Love a Bad Name']
  },
  2468: {
    'albumTitle': '1999',
    'artist': 'Prince',
    'tracks': ['1999', 'Little Red Corvette']
  },
  1245: {
    'artist': 'Robert Palmer',
    'tracks': []
  },
  5439: {
    'albumTitle': 'ABBA Gold'
  }
}

def update_records(record, id, property, value) :
    if id in record :
        if property != 'tracks' and value != '' :
            record[id][property] = value
        elif property == 'tracks' and value != '' :
            if 'tracks' in record[id] :
                record[id][property].append(value)
            else :
                record[id][property] = [value]
        elif value == '' :
            del record[id][property]
        
        return record

printrecord_collection = {
  2548: {
    'albumTitle': 'Slippery When Wet',
    'artist': 'Bon Jovi',
    'tracks': ['Let It Rock', 'You Give Love a Bad Name']
  },
  2468: {
    'albumTitle': '1999',
    'artist': 'Prince',
    'tracks': ['1999', 'Little Red Corvette']
  },
  1245: {
    'artist': 'Robert Palmer',
    'tracks': []
  },
  5439: {
    'albumTitle': 'ABBA Gold'
  }
}

def update_records(record, id, property, value) :
        if property != 'tracks' and value != '' :
            record[id][property] = value
        elif property == 'tracks' and value != '' :
            if 'tracks' in record[id] :
                record[id][property].append(value)
            else :
                record[id][property] = [value]
        elif id in record and value == '' :
            del record[id][property]
        
        return record

print(update_records(record_collection, 5436, 'tracks', '123456'))