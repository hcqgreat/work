k8s安装步骤及注意事项
1、准备系统环境，安装docker，关闭系统交换空间，关闭系统防火墙，禁用SELinux
    (1)启动docker和kubelet服务，并设置开机自启动systemctl enable docker && systemctl start docker
        systemctl enable kubelet && systemctl start kubelet
    (2)swapoff -a (临时关闭系统交换空间)，修改/etc/fstab文件（永久关闭系统交换空间）
    (3)systemctl disable firewalld, systemctl stop firewalld (关闭系统防火墙)
    (4)setenforce 0 或修改/etc/sysconfig/selinux中SELINUX=enforcing改为SELINUX=disabled后重启（禁用SELinux）
    (5)使用kubeadm init安装master
       命令：kubeadm init kubeadm  init --kubernetes-version=v1.18.2 --pod-network-cidr=192.168.0.0/16
            必须指定kubernetes-version否则会按照最新去下载镜像
            pod-network-cidr指定加入集群的node网段
           kubeadm init --config=init-config.yaml
    (6)按提示执行命令
        mkdir -p $HOME/.kube
        sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
        sudo chown $(id -u):$(id -g) $HOME/.kube/config
    (7)按照网络插件（kubectl get nodes会看到master节点是notready状态）
        kubectl apply -f kube_flnnel.yml(会下载镜像并部署)