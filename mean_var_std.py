import numpy as np

def calculate(list):
  
  if len(list) < 9:
    
    raise ValueError("List must contain 9 numbers.")
  
  else:

    calculations = dict.fromkeys(['mean', 'variance', 'standard deviation'])

    shaped_data = np.array(list).reshape(3,3)
    calculations['mean'] = [shaped_data.mean(0).tolist(), shaped_data.mean(1).tolist(), shaped_data.mean().tolist()]

    calculations['standard deviation'] = [shaped_data.std(0).tolist(), shaped_data.std(1).tolist(), shaped_data.std().tolist()]
    
    calculations['variance'] = [shaped_data.var(0).tolist(), shaped_data.var(1).tolist(), shaped_data.var().tolist()]

  return calculations