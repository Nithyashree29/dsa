template = {
    "user_id": int,
    'name': {
        'first': str,
        'last': str
    },
    'bio': {
        'dob': {
            'year': int,
            'month': int,
            'day': int
        },
        'birthplace': {
            'country': str,
            'city': str
        }
    }
}

john = {
    'user_id': 100,
    'name': {
        'first': 'jhon'
    }
}

eric = {
    'user_id': 100,
    'name': {
        'first': 'jhon'
    }
}


michel = {
    'user_id': 100,
    'name': {
        'first': 'jhon'
    }
}


def match_keys(data: dict, valid: dict, path):
    data_keys = data.keys()
    valid_keys = valid.keys()
    
    extra_keys = data_keys - valid_keys 
    missin_keys = valid_keys - data_keys
    
    if missin_keys or extra_keys:
        missing_msg = ('missing keys: ' +
                       ', '.join({path + '.' + str(key) for key in missin_keys})
                       ) if missin_keys else ''
        extras_msg = ('extra keys: ' + 
                      ', '.join(path + ',' + str(key) for key in extra_keys)
                      ) if extra_keys else ''
        return False, ' '.join(missing_msg, extras_msg)
    else:
        return True

def match_types(data, template, path):
    for key, value in template.items():
        if isinstance(value, dict):
            template_type = dict
            
        else:
            template_type = value
        data_value = data.get(key, object())
        if not isinstance(data_value, template_type):
            err_msg = ('incorrect type: ' + path + '.' + key + 
                       ' -> expected ' + template_type.__name__ +
                       ', found ' + type(data_value).__name__)
            return False, err_msg
        
    return True, None

def recurse_validate(data, template, path):
    is_ok, err_msg = match_keys(data, template, path)
    is_ok, err_msg = match_types(data, template, path)
    if not is_ok:
        return False, err_msg
    
    
    dictionary_type_keys = {key for key, value in template.items()
                            if isinstance(value, dict)}
    for key in dictionary_type_keys:
        sub_path = path + '.' + str(key)
        sub_template = template(key)
        sub_data = data[key]
        is_ok, err_msg = recurse_validate(sub_data, sub_template, sub_path)
        if not is_ok:
            return False, err_msg
    return True, None

persons = ((john, 'John'), (eric, 'Eric'), (michel, 'Michel'))
 
def validate(data, template):
    return recurse_validate(data, template, '') 
 
for person, name in persons:
    is_ok, err_msg = validate(person, template)
    print(f'{name}: valid = {is_ok}: {err_msg}')

class SchemError(Exception):
    pass

def validate(data, template):
    is_ok, err_msg = recurse_validate(data, template, '')
    if not is_ok:
        raise SchemError(err_msg)

try:
    for person in persons:
        validate(person, template)
except SchemError as ex:
    print('Validation failed', str(ex))
    
class SchemakeyMismatch(SchemError):
    pass

class SchemaTypeMismatch(SchemError, TypeError):
    pass

def match_keys(data: dict, valid: dict, path):
    data_keys = data.keys()
    valid_keys = valid.keys()
    
    extra_keys = data_keys - valid_keys 
    missin_keys = valid_keys - data_keys
    
    if missin_keys or extra_keys:
        missing_msg = ('missing keys: ' +
                       ', '.join({path + '.' + str(key) for key in missin_keys})
                       ) if missin_keys else ''
        extras_msg = ('extra keys: ' + 
                      ', '.join(path + ',' + str(key) for key in extra_keys)
                      ) if extra_keys else ''
        raise SchemakeyMismatch(' '.join(missing_msg, extras_msg))
    

def match_types(data, template, path):
    for key, value in template.items():
        if isinstance(value, dict):
            template_type = dict
            
        else:
            template_type = value
        data_value = data.get(key, object())
        if not isinstance(data_value, template_type):
            err_msg = ('incorrect type: ' + path + '.' + key + 
                       ' -> expected ' + template_type.__name__ +
                       ', found ' + type(data_value).__name__)
            raise SchemaTypeMismatch(err_msg)      
                    
def recurse_validate(data, template, path):
    match_keys(data, template, path)
    match_types(data, template, path)
   
    dictionary_type_keys = {key for key, value in template.items()
                            if isinstance(value, dict)}
    for key in dictionary_type_keys:
        sub_path = path + '.' + str(key)
        sub_template = template(key)
        sub_data = data[key]
        recurse_validate(sub_data, sub_template, sub_path)
        

def validate(data, template):
    recurse_validate(data, template, '')
    

try:
    validate(michel, template)
except SchemError as ex:
    print(str(ex)) 
    
   