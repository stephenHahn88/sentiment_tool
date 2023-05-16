import numpy as np
import numpy.linalg as nla
from numpy.random import randn, dirichlet
from numpy.linalg import norm
from particles import state_space_models as ssms
from particles import distributions as dists
import particles
from gatherMatrices import getHarmonyEmissionMatrix, emotions
import pickle
from pprint import pprint

"""
alpha_t = Phi * alpha_t-1 + epsilon_t
epsilon_t ~ MVN(0, Sigma_e)
Phi ~ MVN(Mu, Sigma_p)
p_t ~ Dir(alpha_t)
h_t ~ Cat(Vocab, p_t * Emission_probs)
"""

class StudentT(dists.ProbDist):
    def __init__(self, location: np.array, scale: np.array, nu: int):
        if location.shape[0] != scale.shape[0] or location.shape[0] != scale.shape[1]:
            raise ValueError(f"location and scale must have complementary dimensions. Got {location.shape} and {scale.shape} instead.")
        if nu < 1:
            raise ValueError(f"nu must be a positive integer. Got {nu} instead")
        try:
            self.cholesky = nla.cholesky(scale)
        except:
            raise ValueError("scale matrix must be a (d, d) positive definite matrix")

        self.location = location
        self.scale = scale
        self.nu = nu

    @property
    def dim(self):
        return self.scale.shape[-1]

class SentimentSSM(ssms.StateSpaceModel):
    default_params = {
        'phi': np.eye(len(emotions))
    }  # optional

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with open("../data/allDF.pickle", "rb") as f:
            self.df = pickle.load(f)

    def PY(self, t, alpha_t_1, alpha_t):  # dist of Y_t at time t, given X_t and X_{t-1}
        # USING P_T LIKE THIS DOESN'T WORK BECAUSE IT DEPENDS ON THE P_T THAT IS SAMPLED
        # RATHER THAN LOOKING AT THE WHOLE DIRICHLET DIST
        # p_t = dirichlet(alpha_t)
        # p_t = np.expand_dims(p_t, 0)

        # SIMPLIFIED MODEL GOING DIRECTLY FROM ALPHA TO H
        alpha_t = np.expand_dims(alpha_t, 0)
        emissionMatrix = getHarmonyEmissionMatrix(self.df)

        h_dist = np.matmul(alpha_t, emissionMatrix).squeeze()
        h_dist = h_dist / norm(h_dist, ord=1)

        return dists.Categorical(h_dist)

    def PX(self, t, alpha_t_1):  # dist of X_t at time t, given X_{t-1}
        return dists.MvNormal(
            loc=np.matmul(self.phi, alpha_t_1.T).squeeze(), #+ np.random.multivariate_normal(
            #     mean=[0 for _ in range(len(emotions))],
            #     cov=np.eye(len(emotions))
            # ),
            cov=np.eye(len(emotions))
        )

    def PX0(self):  # dist of X_0
        mvn = dists.MvNormal(
            loc=np.array([2 for _ in range(len(emotions))]),
            cov=np.eye(len(emotions))
        )
        return mvn


if __name__ == "__main__":
    _ = ""
    ssm = SentimentSSM()
    alpha, h = ssm.simulate(40)
    fkm = ssms.Bootstrap(ssm=ssm, data=h)
    filter = particles.SMC(fk=fkm, N=200)
    filter.run()












