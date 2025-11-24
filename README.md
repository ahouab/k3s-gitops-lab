# K3s GitOps Lab (GitLab CI + Argo CD + Helm)

This repository contains a complete example lab to practice GitOps with:

- GitLab CE + GitLab Runner
- K3s (lightweight Kubernetes)
- Argo CD
- Helm (for application deployment)

Structure:

- `gitlab/`   — GitLab and runner installation and CI example
- `k3s/`      — K3s control plane and worker installation notes
- `argocd/`   — Argo CD Helm deployment and applications
- `app-source/` — Sample web application + GitLab CI pipeline
- `app-deploy/` — Helm chart + dev/prod values for GitOps
- `docs/`     — High-level architecture and lab scenarios

© Walter Assets — All rights reserved

