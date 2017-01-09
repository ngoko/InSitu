import selection as sel
import qarnot
import numpy as np
LENGTH = 5*44100  # length (in samples) of audios
# set qarnot connection
params = 'samples.conf'
conn = qarnot.connection.Connection(params)
profile = 'docker-batch'
cst = {'DOCKER_REPO': "amaurydurand/my-python"}   
# set dataset 
train_root = 'dataset/Train'
train_directories = [train_root + '/Non_alarm',
                     train_root + '/Alarm']
train_labels = [0, 1]
remote_root_train='data_train'
test_root = 'dataset/Test'
test_directories = [test_root + '/Non_alarm',
                    test_root + '/Alarm']
test_labels = [0, 1]
remote_root_test='data_test'

# set features parameters grid 
frame_sizes = [2048,4096]
fpgrid = [{'frame_size': frame_sizes,
           'early_integration': ['stack', 'mean']}]
# set hyperparameters grid
hpgrid = {'C': [0.1,1,10]}
method = 'logreg'

# define all blocks
train_disk_fun = \
sel.QCreateDisk(name='train_disk_fun',
                next_name='extraction_train_task')
test_disk_fun = \
sel.QCreateDisk(name='test_disk_fun',
                next_name='extraction_test_task')

# common arguments for all tasks
task_args = {'connection':conn,
             'profile':profile,
             'task_constants':cst}
# common arguments for extraction
extraction_args = dict({'instancecount':20,
                        'frame_size':frame_sizes},
                       **task_args)
                   
extraction_train_task = \
sel.QExtractFeaturesTask(name='extraction_train_task',
                         remote_root=remote_root_train
                         next_name='add_code_fun',
                         **extraction_args)
extraction_test_task = \
sel.QExtractFeaturesTask(name='extraction_test_task',
                         remote_root=remote_root_test,
                         next_name='sel_task',
                         **extraction_args)
add_code_fun = \
sel.QCreateDisk(name='add_code_fun',
                next_name=['lkocv_task', 'sel_task'])

lkocv_task = \
sel.QLKOCVTask(name="lkocv_task",
               next_name='sel_task',
               method=method,
               num_samples=LENGTH,
               features_params_grid=fpgrid,
               hyperparams_grid=hpgrid,
               remote_root=remote_root_train,
               **task_args)
sel_task = \
sel.QSelectionTask(name="sel_task",
                   next_name='download_func',
                   method=method,
                   remote_root_train=remote_root_train,
                   remote_root_test=remote_root_test,
                   **task_args)
download_func = \
sel.QDownloadResults(name='download_func',
                     next_name='',
                     method=method,
                     path=path)

# workflow for training
train_workflow = \
orch.QWorkflow([train_disk_fun, extraction_train_task,
                add_code_fun],
               name='train_workflow',
               next_name=['lkocv_task', 'sel_task'])
# workflow for testing
test_workflow = \
orch.QWorkflow([test_disk_fun, extraction_test_task],
               name='test_workflow',
               next_name='sel_task')
# parallel work for extraction
extraction_parallel = \
orch.QParallelWork([train_workflow, test_workflow],
                   name='extraction_parallel',
                   next_name='lkocv_task')
# global workflow
workflow = \
orch.QWorkflow([extraction_parallel, lkocv_task,
                sel_task, download_func],
               name='workflow', verbose=True)

# define inputs and run workflow
train_args={
    'conn': conn,
    'dirs': directories,
    'labels': labels,
    'name': "train_data1",
    'remote_root': remote_root_train,
    'dirs_root' :train_root,
}

test_args={
    'conn': conn,
    'dirs': test_directories,
    'labels': test_labels,
    'name': "test_data1",
    'remote_root': remote_root_test,
    'dirs_root' :test_root
}
iin = orch.QData({'data': [train_args, test_args],
                  'sender': ['init', 'init'],
                  'receiver': ['train_disk_fun',
                               'test_disk_fun']
              })
workflow(iin)
