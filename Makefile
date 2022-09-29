DATA_RESOURCE_URL=https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv
DATASET_NAME=iris
DATASET_PATH=./data/result/20220929_143717/dataset.pickle
SKLEARN_MODEL=DecisionTreeClassifier

install-python-packages:
	pip install -r requirements.txt

show: show-data-pipeline show-model-pipeline

run: run-data-pipeline run-model-pipeline

show-data-pipeline:
	python src/data_pipeline_flow.py show

run-data-pipeline:
	python src/data_pipeline_flow.py run --data_resource_url ${DATA_RESOURCE_URL} --dataset_name ${DATASET_NAME}

show-model-pipeline:
	python src/model_pipeline_flow.py show

run-model-pipeline:
	python src/model_pipeline_flow.py run --dataset_path ${DATASET_PATH} --sklearn_model ${SKLEARN_MODEL}

reset-folder:
	rm -rf data/*