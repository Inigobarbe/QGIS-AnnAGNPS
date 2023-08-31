import numpy as np

from .. import ProblemSpec


def evaluate(X: np.ndarray, A: np.ndarray, M: np.ndarray) -> np.ndarray:
    """Test function taken from Oakley and O'Hagan (2004) (see Eqn. 21 in [1])


    References
    ----------
    .. [1] Oakley, J.E., O’Hagan, A., 2004.
           Probabilistic sensitivity analysis of complex models: a Bayesian approach.
           Journal of the Royal Statistical Society: Series B
           (Statistical Methodology) 66, 751–769.
           https://doi.org/10.1111/j.1467-9868.2004.05304.x
    """
    a1, a2, a3 = A

    num_ins = X.shape[0]
    Y = np.zeros(num_ins)
    for i in range(num_ins):
        x_i = X[i]
        Y[i] = a1 @ x_i + a2 @ np.sin(x_i) + a3 @ np.cos(x_i) + x_i.T @ (M @ x_i)

        a3.T.dot(np.cos(X[0]))

    return Y


if __name__ == "__main__":

    # Raw values taken from: http://www.jeremy-oakley.staff.shef.ac.uk/psa_example.txt
    M = np.array(
        [
            -2.25e-02,
            -1.85e-01,
            1.34e-01,
            3.69e-01,
            1.72e-01,
            1.37e-01,
            -4.40e-01,
            -8.14e-02,
            7.13e-01,
            -4.44e-01,
            5.04e-01,
            -2.41e-02,
            -4.59e-02,
            2.17e-01,
            5.59e-02,
            2.57e-01,
            5.38e-02,
            2.58e-01,
            2.38e-01,
            -5.91e-01,
            -8.16e-02,
            -2.87e-01,
            4.16e-01,
            4.98e-01,
            8.39e-02,
            -1.11e-01,
            3.32e-02,
            -1.40e-01,
            -3.10e-02,
            -2.23e-01,
            -5.60e-02,
            1.95e-01,
            9.55e-02,
            -2.86e-01,
            -1.44e-01,
            2.24e-01,
            1.45e-01,
            2.90e-01,
            2.31e-01,
            -3.19e-01,
            -2.90e-01,
            -2.10e-01,
            4.31e-01,
            2.44e-02,
            4.49e-02,
            6.64e-01,
            4.31e-01,
            2.99e-01,
            -1.62e-01,
            -3.15e-01,
            -3.90e-01,
            1.77e-01,
            5.80e-02,
            1.72e-01,
            1.35e-01,
            -3.53e-01,
            2.51e-01,
            -1.88e-02,
            3.65e-01,
            -3.25e-01,
            -1.21e-01,
            1.25e-01,
            1.07e-01,
            4.66e-02,
            -2.17e-01,
            1.95e-01,
            -6.55e-02,
            2.44e-02,
            -9.68e-02,
            1.94e-01,
            3.34e-01,
            3.13e-01,
            -8.36e-02,
            -2.53e-01,
            3.73e-01,
            -2.84e-01,
            -3.28e-01,
            -1.05e-01,
            -2.21e-01,
            -1.37e-01,
            -1.44e-01,
            -1.15e-01,
            2.24e-01,
            -3.04e-02,
            -5.15e-01,
            1.73e-02,
            3.90e-02,
            3.61e-01,
            3.09e-01,
            5.00e-02,
            -7.79e-02,
            3.75e-03,
            8.87e-01,
            -2.66e-01,
            -7.93e-02,
            -4.27e-02,
            -1.87e-01,
            -3.56e-01,
            -1.75e-01,
            8.87e-02,
            4.00e-01,
            -5.60e-02,
            1.37e-01,
            2.15e-01,
            -1.13e-02,
            -9.23e-02,
            5.92e-01,
            3.13e-02,
            -3.31e-02,
            -2.43e-01,
            -9.98e-02,
            3.45e-02,
            9.51e-02,
            -3.38e-01,
            6.39e-03,
            -6.12e-01,
            8.13e-02,
            8.87e-01,
            1.43e-01,
            1.48e-01,
            -1.32e-01,
            5.29e-01,
            1.27e-01,
            4.51e-02,
            5.84e-01,
            3.73e-01,
            1.14e-01,
            -2.95e-01,
            -5.70e-01,
            4.63e-01,
            -9.41e-02,
            1.40e-01,
            -3.86e-01,
            -4.49e-01,
            -1.46e-01,
            5.81e-02,
            -3.23e-01,
            9.31e-02,
            7.24e-02,
            -5.69e-01,
            5.26e-01,
            2.37e-01,
            -1.18e-02,
            7.18e-02,
            7.83e-02,
            -1.34e-01,
            2.27e-01,
            1.44e-01,
            -4.52e-01,
            -5.56e-01,
            6.61e-01,
            3.46e-01,
            1.41e-01,
            5.19e-01,
            -2.80e-01,
            -1.60e-01,
            -6.84e-02,
            -2.04e-01,
            6.97e-02,
            2.31e-01,
            -4.44e-02,
            -1.65e-01,
            2.16e-01,
            4.27e-03,
            -8.74e-02,
            3.16e-01,
            -2.76e-02,
            1.34e-01,
            1.35e-01,
            5.40e-02,
            -1.74e-01,
            1.75e-01,
            6.03e-02,
            -1.79e-01,
            -3.11e-01,
            -2.54e-01,
            2.58e-02,
            -4.30e-01,
            -6.23e-01,
            -3.40e-02,
            -2.90e-01,
            3.41e-02,
            3.49e-02,
            -1.21e-01,
            2.60e-02,
            -3.35e-01,
            -4.14e-01,
            5.32e-02,
            -2.71e-01,
            -2.63e-02,
            4.10e-01,
            2.66e-01,
            1.56e-01,
            -1.87e-01,
            1.99e-02,
            -2.44e-01,
            -4.41e-01,
            1.26e-02,
            2.49e-01,
            7.11e-02,
            2.46e-01,
            1.75e-01,
            8.53e-03,
            2.51e-01,
            -1.47e-01,
            -8.46e-02,
            3.69e-01,
            -3.00e-01,
            1.10e-01,
            -7.57e-01,
            4.15e-02,
            -2.60e-01,
            4.64e-01,
            -3.61e-01,
            -9.50e-01,
            -1.65e-01,
            3.09e-03,
            5.28e-02,
            2.25e-01,
            3.84e-01,
            4.56e-01,
            -1.86e-01,
            8.23e-03,
            1.67e-01,
            1.60e-01,
        ]
    ).reshape(15, 15)

    A = np.array(
        [
            [
                0.0118,
                0.0456,
                0.2297,
                0.0393,
                0.1177,
                0.3865,
                0.3897,
                0.6061,
                0.6159,
                0.4005,
                1.0741,
                1.1474,
                0.7880,
                1.1242,
                1.1982,
            ],
            [
                0.4341,
                0.0887,
                0.0512,
                0.3233,
                0.1489,
                1.0360,
                0.9892,
                0.9672,
                0.8977,
                0.8083,
                1.8426,
                2.4712,
                2.3946,
                2.0045,
                2.2621,
            ],
            [
                0.1044,
                0.2057,
                0.0774,
                0.2730,
                0.1253,
                0.7526,
                0.8570,
                1.0331,
                0.8388,
                0.7970,
                2.2145,
                2.0382,
                2.4004,
                2.0541,
                1.9845,
            ],
        ]
    )

    sp = ProblemSpec(
        {
            "names": ["x{}".format(i) for i in range(1, 16)],
            "bounds": [
                [0.0, 0.835],
            ]
            * 15,
            "dists": ["norm"] * 15,
        }
    )

    (
        sp.sample_latin(2048, seed=101)
        .evaluate(evaluate, A, M)
        .analyze_rbd_fast(seed=101, num_resamples=100)
    )

    print(sp)

    # analytic S1 values
    analytic = np.array(
        [
            0.00156,
            0.000186,
            0.001307,
            0.003045,
            0.002905,
            0.023035,
            0.024151,
            0.026517,
            0.046036,
            0.014945,
            0.101823,
            0.135708,
            0.101989,
            0.105169,
            0.122818,
        ]
    )

    S1 = sp.analysis.to_df()
    S1["lower"] = S1["S1"] - S1["S1_conf"]
    S1["analytic"] = analytic
    S1["upper"] = S1["S1"] + S1["S1_conf"]

    print(np.all((analytic >= S1["lower"]) & (analytic <= S1["upper"])))
    print((analytic >= S1["lower"]) & (analytic <= S1["upper"]))
