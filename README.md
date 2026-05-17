# Principal Component Analysis on Breast Cancer Gene Expression Data

This project performs Principal Component Analysis (PCA) on breast cancer gene expression data to study the separation of ER-positive (ER+) and ER-negative (ER−) tumor samples using transcriptomic features.

The analysis is based on the GEO dataset:

```text id="3qmyt5"
GSE5325
```

and reproduces key visualizations similar to Figure 1 from the referenced breast cancer study.

Assignment description referenced from 

## Project Structure

```text id="0g2xmv"
pca_project/
│
├── data/
│   ├── class.tsv
│   ├── columns.tsv.gz
│   └── filtered.tsv.gz
│
├── results/
│   ├── figure1a.png
│   ├── figure1c.png
│   └── variance_plot.png
│
└── scripts/
    └── pca_analysis.py
```

## Objective

The project focuses on:

1. Extracting expression levels of:

   * XBP1
   * GATA3

2. Visualizing their expression relationship across patient samples.

3. Performing PCA on the gene expression matrix.

4. Projecting samples onto principal components.

5. Studying separation between ER+ and ER− breast cancer samples.

## Dataset Description

### `class.tsv`

Contains class labels for patient samples:

| Label | Meaning           |
| ----- | ----------------- |
| `1`   | ER+ Breast Cancer |
| `0`   | ER− Breast Cancer |

### `filtered.tsv.gz`

Gene expression matrix containing expression values for all genes across samples.

### `columns.tsv.gz`

Mapping between probe IDs and gene names.

Example:

```text id="6ekj3e"
4404 → XBP1
```

## Workflow

## 1. Load Gene Expression Data

The expression matrix and metadata are loaded into Python using Pandas.

## 2. Extract XBP1 and GATA3

Expression values for:

* XBP1
* GATA3

are extracted across all 105 patient samples.

## 3. Generate Scatter Plot

A scatter plot is created similar to Figure 1a from the paper:

* X-axis: GATA3 expression
* Y-axis: XBP1 expression
* Points colored by ER class

Output:

```text id="n2e92n"
results/figure1a.png
```

## 4. Perform PCA

Principal Component Analysis is applied to the complete gene expression matrix.

The analysis computes:

* Principal Components
* Explained variance ratio
* Sample projections onto lower-dimensional space

## 5. Projection onto PC1

Samples are projected onto the first principal component to reproduce Figure 1c-like visualization.

Output:

```text id="4ldn7z"
results/figure1c.png
```

## 6. Variance Analysis

A scree / variance plot is generated to visualize variance explained by principal components.

Output:

```text id="r5sk1e"
results/variance_plot.png
```

## Example PCA Concepts

### Principal Components

Principal components are orthogonal directions capturing maximum variance in the data.

### PC1

Captures the largest variation across samples and often separates major biological classes.

### PC2

Captures secondary variation orthogonal to PC1.

## Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Scikit-learn

## Installation

Install dependencies:

```bash id="uh9r7r"
pip install numpy pandas matplotlib scikit-learn
```

## Running the Analysis

Execute the script:

```bash id="q10vrr"
python scripts/pca_analysis.py
```

Generated plots will be stored in:

```text id="mgm48v"
results/
```

## Expected Outputs

| File                | Description                 |
| ------------------- | --------------------------- |
| `figure1a.png`      | XBP1 vs GATA3 scatter plot  |
| `figure1c.png`      | Projection onto PC1         |
| `variance_plot.png` | PCA explained variance plot |

## Biological Context

Breast cancer subtypes are often distinguished using receptor expression biomarkers such as:

* Estrogen Receptor (ER)
* Progesterone Receptor (PR)
* HER2

Gene expression profiling combined with PCA enables visualization of subtype-specific transcriptional patterns.

In this dataset:

* ER+ samples cluster differently from ER− samples.
* Genes such as XBP1 and GATA3 show characteristic expression signatures.

