# UTRANS_Embedding
UTrans-Embedding used for JSSP instance
code is implemented using UTRAD

## Installation
```
conda create -n utrans python=3.7
conda install pytorch==1.12.1 torchvision==0.13.1 torchaudio==0.12.1 cudatoolkit=11.3 -c pytorch
pip install -r requirements.txt
```

## Running 
For Using Only Instance Vector(100*20) implement
```
python models.py
```

For Using Instance Vector + Sparse Embedding implement
```
python models_se.py
```
