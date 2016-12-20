!/usr/bin/env python
import qarnot

conn = qarnot.Connection('samples.conf')
task = conn.create_task('sample2-files', 'docker-batch', 1)
input_disk = conn.create_disk('sample2-files-input-resource')
input_disk.add_file('input/lorem.txt')
task.resources.append(input_disk)
task.constants['DOCKER_CMD'] = 'sh -c "cat lorem.txt | tr [:lower:] [:upper:] > LOREM.TXT"'
task.run()
