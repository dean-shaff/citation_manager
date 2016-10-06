<script type="text/x-mathjax-config">
          MathJax.Hub.Config({tex2jax: {inlineMath: [['$','$'], ['\(','\)']]}});
          </script>
<script type="text/javascript" async
            src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_CHTML">
            </script>
<link rel="stylesheet" type="text/css" href="default.css">
## Stochastic Neighbor Embedding
### Geoffrey Hinton and Sam Roweis
This article is about Stochastic Neighbor embedding.

## Visualizing Data using t-SNE
### Geoffrey Hinton and Laurens van der Maaten
This article is about t-distributed Stochastic Neighbor embedding. It's like SNE's better, bigger brother. The thing to note about this is that the don't do a good job of making clear what the normalization is in the $q(i,j)$ joint probability.
We might implement $q(i,j)$ as follows:

```python
import numpy as np 

def qij(Y):
    n = Y.shape[0]
    Y_squared = np.sum(Y**2, axis=1)
    q_no_norm = 1. / (1 + ((Y_squared - 2*np.dot(Y, Y.T)) + Y_squared.reshape(n,1))) 
    # or we can do this as follows:
    # q_no_norm = 1. / (1 + ((Y_squared - 2*np.dot(Y, Y.T)).T + Y_squared)) 
    q_no_norm[np.arange(n),np.arange(n)] = 0.0
    norm = np.sum(q_no_norm)
    qij = q_no_norm / norm
    return qij, q_no_norm
```
