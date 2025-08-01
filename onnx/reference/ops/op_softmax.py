# Copyright (c) ONNX Project Contributors

# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import numpy as np

from onnx.reference.ops._op import OpRunUnaryNum


class Softmax(OpRunUnaryNum):
    def _run(self, X, axis=None):
        axis = axis or self.axis
        tmp = X - X.max(axis=axis, keepdims=1)
        Y = np.exp(tmp)
        Y /= Y.sum(axis=axis, keepdims=1)
        return (Y.astype(X.dtype),)
