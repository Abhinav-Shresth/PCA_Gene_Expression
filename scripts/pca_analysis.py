import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# -----------------------------------
# Load labels
# -----------------------------------

labels = pd.read_csv(
    "pca_project/data/class.tsv",
    sep="\t",
    header=None
)

labels = labels.iloc[:, 0]

# -----------------------------------
# Load expression matrix
# -----------------------------------

expr = pd.read_csv(
    "pca_project/data/filtered.tsv.gz",
    sep="\t",
    compression="gzip"
)

# REMOVE WHITESPACES FROM COLUMN NAMES
expr.columns = expr.columns.str.strip()

# -----------------------------------
# Gene IDs
# -----------------------------------

xbp1_id = "4404"
gata3_id = "4359"

print("Using XBP1 ID:", xbp1_id)
print("Using GATA3 ID:", gata3_id)

# -----------------------------------
# Extract expression values
# -----------------------------------

x_xbp1 = expr[xbp1_id]
x_gata3 = expr[gata3_id]

# -----------------------------------
# Colors
# -----------------------------------

colors = labels.map({
    0: "black",
    1: "red"
})

# -----------------------------------
# Figure 1a
# -----------------------------------

plt.figure(figsize=(6, 6))

plt.scatter(
    x_gata3,
    x_xbp1,
    c=colors
)

plt.xlabel("GATA3")
plt.ylabel("XBP1")

plt.savefig(
    "pca_project/results/figure1a.png",
    dpi=300,
    bbox_inches="tight"
)

# -----------------------------------
# PCA
# -----------------------------------

X = expr.values

pca = PCA(n_components=2)

X_pca = pca.fit_transform(X)

pc1 = X_pca[:, 0]
pc2 = X_pca[:, 1]

# -----------------------------------
# Figure 1c
# -----------------------------------

plt.figure(figsize=(8, 4))

y_all = np.ones(len(pc1)) * 2
y_er_neg = np.ones(sum(labels == 0)) * 1
y_er_pos = np.ones(sum(labels == 1)) * 0

plt.scatter(
    pc1,
    y_all,
    c=colors,
    s=20
)

plt.scatter(
    pc1[labels == 0],
    y_er_neg,
    c="black",
    s=20
)

plt.scatter(
    pc1[labels == 1],
    y_er_pos,
    c="red",
    s=20
)

plt.yticks([0, 1, 2], ["ER+", "ER-", "All"])

plt.xlabel("Projection onto PC1")

plt.savefig(
    "pca_project/results/figure1c.png",
    dpi=300,
    bbox_inches="tight"
)

# -----------------------------------
# Variance plot
# -----------------------------------

plt.figure(figsize=(8, 5))

variance = pca.explained_variance_ratio_ * 100

plt.bar(
    np.arange(1, len(variance) + 1),
    variance
)

plt.xlabel("Principal Component")
plt.ylabel("Proportion of variance (%)")

plt.savefig(
    "pca_project/results/variance_plot.png",
    dpi=300,
    bbox_inches="tight"
)

print("Done")