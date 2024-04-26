# UTRAD
(Non official, modified installation)
UTRAD for neural networks
## Installation
```
conda create -n utrad python=3.7
conda install pytorch==1.12.1 torchvision==0.13.1 torchaudio==0.12.1 cudatoolkit=11.3 -c pytorch
pip install -r requirements.txt
```

## Running 
1. Fetch the Mvtec datasets, check option media_dir and data_root, should modify in your local env.
2. Run training by using command:
```
python main.py --dataset_name grid
```
where --dataset_name is used to specify the catogory.

3. Validate with command:
```
python valid.py --dataset_name grid
```
4. Validate with unaligned setting:
```
python valid.py --dataset_name grid --unaligned_test
```
