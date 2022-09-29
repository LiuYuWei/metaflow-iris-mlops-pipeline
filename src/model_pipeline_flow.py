from metaflow import FlowSpec, step, Parameter


class ModelPipelineFlow(FlowSpec):
    """
    Model pipeline flow
    """
    dataset_path = Parameter(
        "dataset_path",
        help="The resource url of dataset.",
        default="./data/result/20220929_143717/dataset.pickle",
    )
    
    sklearn_model = Parameter(
        "sklearn_model",
        help="The model method.",
        default="RandomForestClassifier",
    )

    @step
    def start(self):
        """
        Use the Metaflow client to retrieve the latest successful run from our
        ModelPipelineFlow and assign them as data artifacts in this flow.
        """
        import pickle
        from metaflow import Flow, get_metadata

        # Print metadata provider
        print("Using metadata provider: %s" % get_metadata())

        # Load the analysis from the Flow.
        run = Flow("ModelPipelineFlow").latest_successful_run
        print("Using analysis from '%s'" % str(run))

        # Load
        with open(self.dataset_path, 'rb') as f:
            self.dataset = pickle.load(f)

        # Compute our two recommendation types in parallel.
        self.next(self.model_training)

    @step
    def model_training(self):
        """
        Data extraction
        """
        from model.training import model_training
        self.model, self.run = model_training(self.dataset, self.sklearn_model)
        
        self.next(self.model_evaluation)
    
    @step
    def model_evaluation(self):
        """
        Model evaluation
        """
        from model.evaluation import model_evaluation
        self.test_accuracy = model_evaluation(self.model, self.dataset)

        self.next(self.model_registry)
    
    @step
    def model_registry(self):
        """
        Model registry
        """
        from model.registry import model_registry
        self.model_registry_information = model_registry(self.run, self.test_accuracy)
        
        self.next(self.model_deployment)

    @step
    def model_deployment(self):
        """
        Model deployment
        """
        from model.deployment import model_deployment
        model_deployment(self.model_registry_information)
        
        self.next(self.end)
    
    @step
    def end(self):
        """
        Print the data ETL result.
        """
        print("Finish model training pipeline.")
        

if __name__ == "__main__":
    ModelPipelineFlow()
