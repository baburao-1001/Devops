import time

def deploy_application(environment, version):
    print(f"Deploying version {version} to {environment} environment...")
    time.sleep(2)  # Simulating deployment time
    print("Deployment successful!")

def run_tests(environment):
    print(f"Running tests on {environment} environment...")
    time.sleep(1)  # Simulating test execution time
    print("Tests passed successfully!")

def main():
    # Define deployment environment and version
    deployment_environment = "Production"
    deployment_version = "v1.0"

    # Deploy to Production
    deploy_application(deployment_environment, deployment_version)

    # Run tests in Production
    run_tests(deployment_environment)

    # Notify about successful deployment
    print(f"DevOps pipeline completed for {deployment_environment} environment.")

if __name__ == "__main__":
    main()
