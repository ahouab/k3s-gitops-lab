# GitLab Runner Installation

1. Install GitLab Runner on the same VM or a separate one:
   ```bash
   curl -L https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.deb.sh | sudo bash
   sudo apt-get install -y gitlab-runner
   ```

2. Register a runner:
   ```bash
   sudo gitlab-runner register
   ```

   - GitLab URL: `https://gitlab.lab.local/`
   - Registration token: from your GitLab project or instance
   - Description: `k3s-gitops-lab-runner`
   - Tags: `docker,k8s`
   - Executor: `docker` (recommended for isolation)

3. Example Docker executor config:
   - Use `docker` default image: `docker:24.0`
   - Enable docker-in-docker if you want to build images inside containers.
