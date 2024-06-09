# guide doc

https://yashna-shravani.medium.com/deploying-sbert-in-production-using-torchserve-cc1e438a90d

# zip

zip the model dir to pytorch_model.bin

# install

pip install torch-model-archiver

# torch-model-archiver

torch-model-archiver --model-name sentence_Transformer_BERT --version 1.0 --serialized-file pytorch_model.bin --handler run_handler.py --extra-files handler.py --export-path ./ --runtime python3 -f

# run container

docker run --rm -it -p 3000:8080 -n sbert ptserve-sbert:v1
