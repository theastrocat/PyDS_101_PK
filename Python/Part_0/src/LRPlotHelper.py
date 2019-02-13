import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression


class ModelPlotter(object):
    def __init__(self, model, data):
        self.fit_model = model
        self.data = data.values
        self.columns = data.columns
        self.plot_model()

    def plot_model(self):
        X = self.data[:,:-1]
        y = self.data[:,-1]
        xx, yy = np.mgrid[min(X[:,0])-1:max(X[:,0])+1:.01, min(X[:,1])-1:max(X[:,1])+1:.01]
        grid = np.c_[xx.ravel(), yy.ravel()]
        probs = self.fit_model.predict_proba(grid)[:, 1].reshape(xx.shape)
        f, ax = plt.subplots(figsize=(20, 15))
        contour = ax.contourf(xx, yy, probs, 25, cmap="RdBu",
                              vmin=0, vmax=1)
        ax_c = f.colorbar(contour)
        ax_c.set_label("$P(y = 1)$")
        ax_c.set_ticks([0, .25, .5, .75, 1])

        ax.scatter(X[:,0], X[:, 1], c=y, s=50,
                   cmap="RdBu", vmin=-.2, vmax=1.2,
                   edgecolor="white", linewidth=1)

        ax.set(aspect="equal",
               xlabel=self.columns[0],
               ylabel=self.columns[1])
