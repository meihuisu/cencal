# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.40
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
# This file is compatible with both classic and new-style classes.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_cencalvm', [dirname(__file__)])
        except ImportError:
            import _cencalvm
            return _cencalvm
        if fp is not None:
            try:
                _mod = imp.load_module('_cencalvm', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _cencalvm = swig_import_helper()
    del swig_import_helper
else:
    import _cencalvm
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class SpatialDB(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SpatialDB, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SpatialDB, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _cencalvm.delete_SpatialDB
    __del__ = lambda self : None;
    def label(self, *args): return _cencalvm.SpatialDB_label(self, *args)
    def open(self): return _cencalvm.SpatialDB_open(self)
    def close(self): return _cencalvm.SpatialDB_close(self)
    def queryVals(self, *args): return _cencalvm.SpatialDB_queryVals(self, *args)
    def query(self, *args): return _cencalvm.SpatialDB_query(self, *args)
    def multiquery(self, *args): return _cencalvm.SpatialDB_multiquery(self, *args)
SpatialDB_swigregister = _cencalvm.SpatialDB_swigregister
SpatialDB_swigregister(SpatialDB)

class CenCalVMDB(SpatialDB):
    __swig_setmethods__ = {}
    for _s in [SpatialDB]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, CenCalVMDB, name, value)
    __swig_getmethods__ = {}
    for _s in [SpatialDB]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, CenCalVMDB, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _cencalvm.new_CenCalVMDB(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cencalvm.delete_CenCalVMDB
    __del__ = lambda self : None;
    def open(self): return _cencalvm.CenCalVMDB_open(self)
    def close(self): return _cencalvm.CenCalVMDB_close(self)
    def queryType(self, *args): return _cencalvm.CenCalVMDB_queryType(self, *args)
    def queryRes(self, *args): return _cencalvm.CenCalVMDB_queryRes(self, *args)
    def minVs(self, *args): return _cencalvm.CenCalVMDB_minVs(self, *args)
    def queryVals(self, *args): return _cencalvm.CenCalVMDB_queryVals(self, *args)
    def filename(self, *args): return _cencalvm.CenCalVMDB_filename(self, *args)
    def cacheSize(self, *args): return _cencalvm.CenCalVMDB_cacheSize(self, *args)
    def filenameExt(self, *args): return _cencalvm.CenCalVMDB_filenameExt(self, *args)
    def cacheSizeExt(self, *args): return _cencalvm.CenCalVMDB_cacheSizeExt(self, *args)
    def squash(self, *args): return _cencalvm.CenCalVMDB_squash(self, *args)
    def query(self, *args): return _cencalvm.CenCalVMDB_query(self, *args)
CenCalVMDB_swigregister = _cencalvm.CenCalVMDB_swigregister
CenCalVMDB_swigregister(CenCalVMDB)


