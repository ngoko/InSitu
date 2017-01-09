from orchestration import *
# define basic blocs
f1 = QFunc(func=lambda x: 
           2*x.get_value('sender', 'init')['data'][0], 
           name='f1', 
           next_name=['f211', 'f221', 'f3'])
f211 = QFunc(func=lambda x: 
             x.get_value('sender', 'f1')['data'][0] 
             * x.get_value('sender', 'init')['data'][0],
             name='f211',
             next_name='f212')
f212 = QFunc(func=lambda x: 
             x.get_value('sender', 'f211')['data'][0]/3.,
             name='f212',
             next_name='f3')
f221 = QFunc(func=lambda x: 
             x.get_value('sender', 'f1')['data'][0]+1,
             name='f221',
             next_name=['f2221', 'f2222'])
f2221 = QFunc(func=lambda x: 
              x.get_value('sender', 'f221')['data'][0]-2,
             name='f2221',
             next_name='f3')
f2222 = QFunc(func=lambda x: 
              x.get_value('sender', 'f221')['data'][0]-3,
             name='f2222',
             next_name='f3')

f3 = QFunc(func=lambda x: 
           x.get_value('sender', 'f1')['data'][0] 
           + x.get_value('sender', 'f212')['data'][0] 
           + x.get_value('sender', 'f2221')['data'][0] 
           + x.get_value('sender', 'f2222')['data'][0],
           name='f3')
# define f21 workflow
f21 = QWorkflow(workflow=[f211, f212],
               name='f21',
               next_name='f3')
# define f222 parallel work
f222 = QParallelWork(list_of_func=[f2221, f2222],
                    name='f222',
                    next_name='f3')
# define f22 workflow
f22 = QWorkflow(workflow=[f221, f222],
               name='f22',
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
        'data':[2, 3],
        'sender':['init', 'init'],
        'receiver':['f1', 'f211']
    })
# run the workflow
res = f(d)
print(res['data'][0])
