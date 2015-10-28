def constant(f):
    def fset(self,value):
        raise TypeError
    def fget(self):
        return f()
    return property(fget, fset)

class _Const(object):

    @constant
    def kphi0():
        return 4.56542e-06
    @constant
    def krinvpars():
        return 7.60903e-07
    @constant
    def kz():
        return 0.0561523
    @constant
    def kt():
        return 0.00116984
    @constant
    def kpt():
        return 111111

