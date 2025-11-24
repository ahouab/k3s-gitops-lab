# K3s Agent (Worker Node) Installation

On the worker VM (VM3):

1. Get the `node-token` from the control-plane node (VM2).

2. Install K3s agent:
   ```bash
   curl -sfL https://get.k3s.io |    K3S_URL="https://<CONTROL_PLANE_IP>:6443"    K3S_TOKEN="<NODE_TOKEN>"    INSTALL_K3S_EXEC="agent" sh -
   ```

3. Verify from the control-plane node:
   ```bash
   sudo k3s kubectl get nodes
   ```
