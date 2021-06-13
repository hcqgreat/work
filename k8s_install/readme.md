# ubuntu16.04 k8s安装步骤及注意事项
##### 准备系统环境，安装docker，关闭系统交换空间，关闭系统防火墙，禁用SELinux
##### 步骤：
1. 安装ubuntu16.04 server <br>
2. 固定IP地址 <br>
   修改/etc/network/interfaces文件内容如： <br>
        source /etc/network/interfaces.d/* <br>
        # The loopback network interface <br>
        auto lo <br>
        iface lo inet loopback <br>
        # The primary network interface <br>
        auto enp0s3 <br>
        iface enp0s3 inet static <br>
        address 192.168.1.200 <br>
        netmask 255.255.255.0 <br>
        gateway 192.168.1.1 <br>
        dns-nameserver 8.8.8.8 <br>
        # This is an autoconfigured IPv6 interface  <br>
        iface enp0s3 inet6 auto <br>
3. swapoff -a (临时关闭系统交换空间)，修改/etc/fstab文件（永久关闭系统交换空间）<br>
4. systemctl disable firewalld, systemctl stop firewalld (关闭系统防火墙) <br>
5. setenforce 0 或修改/etc/sysconfig/selinux中SELINUX=enforcing改为SELINUX=disabled后重启（禁用SELinux）<br>
6. 安装相关工具 <br>
   sudo apt-get update && apt-get install -y apt-transport-https curl <br>
   sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - <br>
   apt-get install docker.io -y <br>
   curl -s https://mirrors.aliyun.com/kubernetes/apt/doc/apt-key.gpg | sudo apt-key add - <br>
   sudo tee /etc/apt/sources.list.d/kubernetes.list <<EOF 
   deb https://mirrors.aliyun.com/kubernetes/apt/ kubernetes-xenial main
   EOF <br>
   sudo apt-get update <br>
   sudo apt-get install -y kubelet kubeadm kubectl <br>
   sudo apt-mark hold kubelet kubeadm kubectl <br>
7. 启动docker和kubelet服务，并设置开机自启动systemctl enable docker && systemctl start docker && systemctl enable kubelet && 
systemctl start kubelet <br>
8. 使用kubeadm init安装master <br>
       命令：sudo kubeadm init --pod-network-cidr 192.168.0.0/16 --image-repository registry.cn-hangzhou.aliyuncs.com/google_containers  --kubernetes-version=v1.21.1 <br>
            必须指定kubernetes-version否则会按照最新去下载镜像 <br>
            pod-network-cidr指定加入集群的node网段 <br>
           kubeadm init --config=init-config.yaml <br>
9. 按提示执行命令 <br>
        mkdir -p $HOME/.kube <br>
        sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config <br>
        sudo chown $(id -u):$(id -g) $HOME/.kube/config <br>
10. 按照网络插件（kubectl get nodes会看到master节点是notready状态）<br>
        kubectl apply -f kube_flnnel.yml(会下载镜像并部署) <br>
11. 集群加入节点，在节点执行 <br>
        kubectl join --config= join-config.yaml <br>
   
    kubeadm join 192.168.1.200:6443 --token xqykxq.ugq7y2zs57e7ak6v --discovery-token-ca-cert-hash sha256:bc63fe9e89981949f4f9e440a7ae47817bbd097246dfe2400d7e5829e5ecc914