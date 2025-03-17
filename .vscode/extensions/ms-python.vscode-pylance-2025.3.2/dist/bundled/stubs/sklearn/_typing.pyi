# This file is generated by docs2stub. These types are intended
# to simplify the stubs generated by docs2stub. They are not
# intended to be used directly by other users.

import decimal
import io
import typing_extensions

import numpy as np
import numpy.typing
import pandas as pd
from scipy.sparse import spmatrix

from .base import BaseEstimator, ClassifierMixin, RegressorMixin

Decimal = decimal.Decimal
PythonScalar: typing_extensions.TypeAlias = str | int | float | bool

ArrayLike = numpy.typing.ArrayLike
MatrixLike: typing_extensions.TypeAlias = np.ndarray | pd.DataFrame | spmatrix
FileLike = io.IOBase
PathLike = str
Int: typing_extensions.TypeAlias = int | np.int8 | np.int16 | np.int32 | np.int64
Float: typing_extensions.TypeAlias = float | np.float16 | np.float32 | np.float64

PandasScalar: typing_extensions.TypeAlias = pd.Period | pd.Timestamp | pd.Timedelta | pd.Interval
Scalar: typing_extensions.TypeAlias = PythonScalar | PandasScalar

Estimator = BaseEstimator
Classifier = ClassifierMixin
Regressor = RegressorMixin

Color: typing_extensions.TypeAlias = tuple[float, float, float] | str
