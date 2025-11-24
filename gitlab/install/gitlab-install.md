# GitLab CE Installation (Lab)

> Example for Ubuntu Server, adjust to your distribution if needed.

1. Install dependencies:
   ```bash
   sudo apt-get update
   sudo apt-get install -y curl ca-certificates tzdata openssh-server
   ```

2. Add GitLab repository and install:
   ```bash
   curl https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.deb.sh | sudo bash
   sudo EXTERNAL_URL="https://gitlab.lab.local" apt-get install -y gitlab-ce
   ```

3. Configure GitLab (if needed):
   - Edit `/etc/gitlab/gitlab.rb`:
     - `external_url "https://gitlab.lab.local"`
     - Enable Container Registry (e.g. `registry.gitlab.lab.local`)
   - Reconfigure:
     ```bash
     sudo gitlab-ctl reconfigure
     ```

4. Get root password:
   ```bash
   sudo cat /etc/gitlab/initial_root_password
   ```

5. Access the UI at `https://gitlab.lab.local` and change the root password.
