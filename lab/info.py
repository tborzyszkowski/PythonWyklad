def info(object, spacing=10, collapse=1):
    """Print methods and doc strings.

    Takes module, class, list, dictionary, or string."""
    def f(s):
        return " ".join(s.split())
    
    def g(s):
        return s
    
    methodList = [e for e in dir(object) if callable(getattr(object, e))]
    processFunc = collapse and f or g
    print "\n".join(["%s %s" %
                     (method.ljust(spacing),
                      processFunc(str(getattr(object, method).__doc__)))
                     for method in methodList])
