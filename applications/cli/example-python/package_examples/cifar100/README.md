# CIFAR100 CNN training example

* Train model (adjust resources to environment, increase number of epochs for better accuracy):
```bash
nctl experiment submit cifar100_cnn.py  --name cifar-100-cnn-11 \
-p workersCount 1 \
-p processesPerNode 1 \
-p cpu 20 \
-p memory 18Gi \
-p cpus 10 \
--template tf-training-horovod \
--requirements requirements.txt \
-- --epochs 5 --use-horovod --output-path /mnt/output/experiment --cpu-count 10
```

* Alternatively, model can be trained without horovod:
```bash
nctl experiment submit cifar100_cnn.py  --name cifar-100-cnn \
-p cpu 14 \
-p memory 8Gi \
--requirements requirements.txt \
-- --epochs 5 --output-path /mnt/output/experiment --cpu-count 7
```

* Monitor training with TensorBoard*:
```bash
nctl launch tb cifar-100-cnn
```

* Start prediction instance: 
```bash
nctl predict launch -n cifar-100-cnn-inference --model-location /mnt/output/home/cifar-100-cnn/cifar100_tf_model
```

Test prediction instance using either: 
- Jupyter notebook:
```bash
nctl experiment interact --filename cifar100.ipynb
```
- nctl:
```bash
nctl predict stream --name cifar-100-cnn-inference --data example-image.json
``` 
