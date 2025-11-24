# K3s Server (Control Plane) Installation

1. On the control-plane VM (VM2):
   ```bash
   curl -sfL https://get.k3s.io | INSTALL_K3S_EXEC="server" sh -
   ```

2. Verify:
   ```bash
   sudo k3s kubectl get nodes
   ```

3. Get the node token (used by workers):
   ```bash
   sudo cat /var/lib/rancher/k3s/server/node-token
   ```

4. Create namespaces:
   ```bash
   sudo k3s kubectl create namespace app-dev
   sudo k3s kubectl create namespace app-prod
   sudo k3s kubectl create namespace argocd
   ```
