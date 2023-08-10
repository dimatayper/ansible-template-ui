import six

def b(s):
    if isinstance(s, six.text_type):
        return s.encode('utf-8')
    return s

def u(s):
    if isinstance(s, six.binary_type):
        return s.decode('utf-8')
    return s

native = u if six.PY3 else b
