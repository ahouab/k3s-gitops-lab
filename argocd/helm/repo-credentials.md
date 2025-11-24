# Argo CD Git Repository Credentials (GitLab)

1. Generate an SSH key (on the Argo CD admin machine or similar):
   ```bash
   ssh-keygen -t ed25519 -C "argocd@gitlab.lab.local"
   ```

2. Add the public key (`.pub`) as a **Deploy Key** to the GitLab repositories:
   - `app-source` (optional, usually read-only for Argo CD)
   - `app-deploy` (required)

3. In Argo CD:
   - Settings → Repositories → Connect Repo using SSH
   - URL example: `ssh://git@gitlab.lab.local:group/app-deploy.git`
   - Paste the private key and the known hosts entry.
