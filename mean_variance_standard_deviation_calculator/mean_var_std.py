import numpy as np

def calculate(list):
  if (len(list)<9):
      raise ValueError('List must contain nine numbers.')
  else :
    arr = np.asarray(list)
    arr = arr.reshape(3,3)
    calculations =  {'mean':[],'variance':[] ,'standard deviation':[],'max':[],'min':[],'sum':[]}
    t1 = np.mean(arr, axis = 0)
    t1 = t1.tolist()
    t2 = np.mean(arr, axis = 1)
    t2 = t2.tolist()
    calculations['mean'] = [t1 , t2 , np.mean(arr)]
    t1 = np.var(arr, axis = 0)
    t1 = t1.tolist()
    t2 = np.var(arr, axis = 1)
    t2 = t2.tolist()
    calculations['variance'] = [t1 , t2 , np.var(arr)]
    t1 = np.std(arr, axis = 0)
    t1 = t1.tolist()
    t2 = np.std(arr, axis = 1)
    t2 = t2.tolist()
    calculations['standard deviation'] = [t1 , t2 , np.std(arr)]
    t1 = np.max(arr, axis = 0)
    t1 = t1.tolist()
    t2 = np.max(arr, axis = 1)
    t2 = t2.tolist()
    calculations['max'] = [t1 , t2 , np.max(arr)]
    t1 = np.min(arr, axis = 0)
    t1 = t1.tolist()
    t2 = np.min(arr, axis = 1)
    t2 = t2.tolist()
    calculations['min'] = [t1 , t2 , np.min(arr)]
    t1 = np.sum(arr, axis = 0)
    t1 = t1.tolist()
    t2 = np.sum(arr, axis = 1)
    t2 = t2.tolist()
    calculations['sum'] = [t1 , t2 , np.sum(arr)]




  return calculations
