"""
Module containing function for plotting clustered data onto a two-dimensional scatterplot using
principal component analysis
"""
import pandas as pd
from sklearn.decomposition import PCA
from cluster_pval import pval_module
from cluster_pval import cluster_module
import plotly.express as px

def cluster_plot(clustered_df):
    """
    Function to plot first two principal components of clustered data

    Parameters:
    :param clustered_df: pandas dataframe of clustered RNA seq data
    :return: fig: two-dimensional scatterplot of dimensionally reduced data color-coded by cluster
    """
    #perform PCA and reduce data to two dimensions
    pca_2 = PCA(n_components=2)
    principal_components = pca_2.fit_transform(clustered_df)
    principal_df = pd.DataFrame(data = principal_components, columns = ['first principal component', 'second principal component'])

    #plot data in scatterplot
    clustered_df = clustered_df.sort_values(['cluster'], ascending=True)
    clustered_df['cluster'] = clustered_df['cluster'].astype(str)
    fig = px.scatter(x=principal_df[:, 0], y=principal_df[:, 1], color=clustered_df['cluster'],
    labels={'x': "First Principal Component", 'y': "Second Principal Component", 'color': "Cluster"},
    title="Scatter plot of clustered cells", 
    template="simple_white")

    return fig