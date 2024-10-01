def introspection_info(obj):
    dict_ = {}
    type_ = type(obj)
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith('__')]
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and method.startswith('__')]
    module = dict_.__class__.__module__

    dict_ = {'type_': type_,
             'attributes': attributes,
             'methods': methods,
             'module': module}
    return dict_


number_info = introspection_info(42)
print(number_info)
