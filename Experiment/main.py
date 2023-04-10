import torch
import numpy as np
from Model import ISTA, FISTA
"""

"""


def main():
    path = './StimulateData/MatrixA.npy'
    A = np.load(path)
    A = torch.from_numpy(A)
    A = A.float()
    n, m = A.size(0), A.size(1)
    # print(n, m)

    x_single = torch.load('./StimulateData/x_single.pt')
    y_single = torch.load('./StimulateData/y_single.pt')
    # print(x_single)

    """
    ISTA
    """
    ista_max_iteration = 1000
    ista_Lasso_lamda = 0.5
    ista_err = 1e-7
    ista = ISTA.ISTA()
    ista.ista(A, y_single, x_single, ista_max_iteration, ista_err, ista_Lasso_lamda)

    """
    FISTA
    """
    fista_max_iteration = 1000
    fista_Lasso_lamda = 0.25
    fista_err = 1e-7
    fista = FISTA.FISTA()
    fista.fista(A, y_single, x_single, fista_max_iteration, fista_err, fista_Lasso_lamda)





if __name__ == '__main__':
    main()