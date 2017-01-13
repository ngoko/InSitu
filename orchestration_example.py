from orchestration import *
# define basic blocks
f1 = QFunc(func=lambda x: 
           2*x.get_value('sender', 'init')['data'][0], 
           name='f1', 
           next_name=['f211', 'f22', 'f3'])
f211 = QFunc(func=lambda x: 
             x.get_value('sender', 'f1')['data'][0] 
             * x.get_value('sender', 'init')['data'][0],
             name='f211',
             next_name='f212')
f212 = QFunc(func=lambda x: 
             x.get_value('sender', 'f211')['data'][0]/3.,
             name='f212',
             next_name='f3')
f22 = QFunc(func=lambda x: 
             x.get_value('sender', 'f1')['data'][0]+1,
             name='f22',
             next_name='f3')
f3 = QFunc(func=lambda x: 
           x.get_value('sender', 'f1')['data'][0] 
           + x.get_value('sender', 'f212')['data'][0] 
           + x.get_value('sender', 'f22')['data'][0],
           name='f3')
# define f21 workflow
f21 = QWorkflow(workflow=[f211, f212],
               name='f21',
               next_name='f3')
# define f2 parallel work
f2 = QParallelWork(list_of_func=[f21, f22],
                  name='f2',
                  next_name='f3')
# define global workflow
f = QWorkflow(workflow=[f1, f2, f3],
              name='workflow',
              verbose=True)
# define input
d = QData({
        'data':[2, 4],
        'sender':['init', 'init'],
        'receiver':['f1', 'f211']
    })
# run the workflow
res = f(d)
print(res['data'][0])
