from metaflow import FlowSpec, step, Parameter


class DataPipelineFlow(FlowSpec):
    """
    Data pipeline flow
    """

    data_resource_url = Parameter(
        "data_resource_url",
        help="The resource url of dataset.",
        default="https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv",
    )
    
    dataset_name = Parameter(
        "dataset_name",
        help="The dataset name.",
        default="iris",
    )

    @step
    def start(self):
        """
        Use the Metaflow client to retrieve the latest successful run from our
        DataPipelineFlow and assign them as data artifacts in this flow.
        """
        from metaflow import Flow, get_metadata

        # Print metadata provider
        print("Using metadata provider: %s" % get_metadata())

        # Load the analysis from the Flow.
        run = Flow("DataPipelineFlow").latest_successful_run
        print("Using analysis from '%s'" % str(run))


        # Compute our two recommendation types in parallel.
        self.next(self.data_extraction)

    @step
    def data_extraction(self):
        """
        Data extraction
        """
        from data.extraction import data_extraction
        self.df = data_extraction(self.data_resource_url)

        self.next(self.data_transform)
    
    @step
    def data_transform(self):
        """
        Data transform
        """
        from data.transform import data_transform
        self.data, self.dataset = data_transform(self.df)

        self.next(self.data_load_to)
    
    @step
    def data_load_to(self):
        """
        Data Load to
        """
        from data.load_to import data_load_to
        data_load_to(self.data, self.dataset, self.dataset_name)

        self.next(self.end)
    
    @step
    def end(self):
        """
        Print the data ETL result.
        """
        print("Finish data ETL pipeline.")


if __name__ == "__main__":
    DataPipelineFlow()
