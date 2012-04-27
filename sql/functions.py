#This file is part of python-sql.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.

from sql import Column, Flavor

__all__ = ['Abs', 'Cbrt', 'Ceil', 'Degrees', 'Div', 'Exp', 'Floor', 'Ln',
    'Log', 'Mod', 'Pi', 'Power', 'Radians', 'Random', 'Round', 'SetSeed',
    'Sign', 'Sqrt', 'Trunc', 'WidthBucket',
    'Acos', 'Asin', 'Atan', 'Atan2', 'Cos', 'Cot', 'Sin', 'Tan',
    'BitLength', 'CharLength', 'Upper']

# TODO Data formating
# TODO Date/Time
# TODO EXISTS, ANY/SOME, ALL

# Mathematical


class Function(Column):
    __slots__ = ('args',)
    table = ''
    name = ''
    _function = ''

    def __init__(self, *args):
        self.args = args

    def __str__(self):
        param = Flavor.get().param

        def format(arg):
            if isinstance(arg, basestring):
                return param
            else:
                return str(arg)
        return self._function + '(' + ', '.join(map(format, self.args)) + ')'

    @property
    def params(self):
        p = ()
        for arg in self.args:
            if isinstance(arg, basestring):
                p += (arg,)
            elif hasattr(arg, 'params'):
                p += arg.params
        return p


class Abs(Function):
    __slots__ = ()
    _function = 'ABS'


class Cbrt(Function):
    __slots__ = ()
    _function = 'CBRT'


class Ceil(Function):
    __slots__ = ()
    _function = 'CEIL'


class Degrees(Function):
    __slots__ = ()
    _function = 'DEGREES'


class Div(Function):
    __slots__ = ()
    _function = 'DIV'


class Exp(Function):
    __slots__ = ()
    _function = 'EXP'


class Floor(Function):
    __slots__ = ()
    _function = 'FLOOR'


class Ln(Function):
    __slots__ = ()
    _function = 'LN'


class Log(Function):
    __slots__ = ()
    _function = 'LOG'


class Mod(Function):
    __slots__ = ()
    _function = 'MOD'


class Pi(Function):
    __slots__ = ()
    _function = 'PI'


class Power(Function):
    __slots__ = ()
    _function = 'POWER'


class Radians(Function):
    __slots__ = ()
    _function = 'RADIANS'


class Random(Function):
    __slots__ = ()
    _function = 'RANDOM'


class Round(Function):
    __slots__ = ()
    _function = 'ROUND'


class SetSeed(Function):
    __slots__ = ()
    _function = 'SETSEED'


class Sign(Function):
    __slots__ = ()
    _function = 'SIGN'


class Sqrt(Function):
    __slots__ = ()
    _function = 'SQRT'


class Trunc(Function):
    __slots__ = ()
    _function = 'TRUNC'


class WidthBucket(Function):
    __slots__ = ()
    _function = 'WIDTH_BUCKET'

# Trigonometric


class Acos(Function):
    __slots__ = ()
    _function = 'ACOS'


class Asin(Function):
    __slots__ = ()
    _function = 'ASIN'


class Atan(Function):
    __slots__ = ()
    _function = 'ATAN'


class Atan2(Function):
    __slots__ = ()
    _function = 'ATAN2'


class Cos(Function):
    __slots__ = ()
    _function = 'Cos'


class Cot(Function):
    __slots__ = ()
    _function = 'COT'


class Sin(Function):
    __slots__ = ()
    _function = 'SIN'


class Tan(Function):
    __slots__ = ()
    _function = 'TAN'

# String


class BitLength(Function):
    __slots__ = ()
    _function = 'BIT_LENGTH'


class CharLength(Function):
    __slots__ = ()
    _function = 'CHAR_LENGTH'


class Lower(Function):
    __slots__ = ()
    _function = 'LOWER'


class OctetLength(Function):
    __slots__ = ()
    _function = 'OCTET_LENGTH'

# TODO overlay, position, substring, trim


class Upper(Function):
    __slots__ = ()
    _function = 'UPPER'

# TODO other string
