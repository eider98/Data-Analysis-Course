import numpy as np

def calculate(list):
    m = np.reshape(list,[3,3])
    out = {'mean':[],'variance':[],'standard deviation':[],'max':[],'min':[],'sum':[]}
    for i in [0,1,None]:
        out['mean'].append(np.mean(m,axis=i).tolist())
        out['variance'].append(np.var(m,axis=i).tolist())
        out['standard deviation'].append(np.std(m,axis=i).tolist())
        out['max'].append(np.max(m,axis=i).tolist())
        out['min'].append(np.min(m,axis=i).tolist())
        out['sum'].append(np.sum(m,axis=i).tolist())
    return out