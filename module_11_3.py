import inspect

def introspection_info(obj):
    inspect_dict = {}
    inspect_dict['type'] = type(obj)
    inspect_dict['attributes'] = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
    inspect_dict['methods'] = [method for method in dir(obj) if callable(getattr(obj, method))]
    inspect_dict['module'] = module = introspection_info.__module__
    inspect_dict['isinstance'] = isinstance(obj, int)

    return inspect_dict

number_info = introspection_info(42)
print(number_info)