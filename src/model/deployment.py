from primehub import PrimeHub, PrimeHubConfig

def model_deployment(model_registry_information):
    ph = PrimeHub(PrimeHubConfig())
    primehub_deploy_id = "iris-model-registry"

    # Deploy the model
    if model_registry_information["create_deploy"]:
        # Create a deployment
        config = {
            "id": primehub_deploy_id,
            "name": primehub_deploy_id,
            "modelImage": "infuseai/sklearn-prepackaged:v0.1.0",
            "modelURI": model_registry_information['modeluri'],
            "instanceType": "cpu-1",
            "replicas": 1
        }
        deployment = ph.deployments.create(config)
    else:
        config = {
            "modelURI": model_registry_information['modeluri']
        }
        deployment = ph.deployments.update(primehub_deploy_id, config)

    print(deployment)
