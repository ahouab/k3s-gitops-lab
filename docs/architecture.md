# K3s GitOps Lab Architecture

## Components

- **GitLab CE** for source code, container registry, and CI/CD pipelines.
- **K3s** as the Kubernetes distribution (1 control-plane node, 1 worker node).
- **Argo CD** for GitOps-based continuous delivery.
- **Helm** for packaging and deploying applications.
- **GitLab CI** to build images, push to the registry, and update Helm values.

## GitOps Flow

1. Developer pushes code to `app-source` repository in GitLab.
2. GitLab CI:
   - runs tests
   - builds and scans a Docker image
   - pushes image to GitLab Container Registry
   - updates the image tag in the `app-deploy` Helm values file (`values-dev.yaml`)
3. Argo CD watches the `app-deploy` repo and syncs changes to the K3s cluster.
4. Promotion to production is handled through a Git merge request that changes `values-prod.yaml`, then a manual sync in Argo CD.
