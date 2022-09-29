# metaflow-iris-mlops-pipeline
Use metaflow to demo the iris classification MLOps pipeline.

# How to use it?
- Step 1: Install make
```bash
sudo apt-get update
sudo apt-get -y install make
```

- Step 2: Install python package
```bash
make install-python-packages
```

- Step 3: Show the pipeline
```bash
make show
```

- Step 4: Run the pipeline
```bash
make run-data-pipeline
make run-model-pipeline
```

- Step 5: If you want to reset the data folder, you can use the following command line:
```bash
make reset-folder
```