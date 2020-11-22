pipeline{
    //默认整流水线在any节点上运行，any可以是标签
    agent any

    agent {
        label {
            label "<label>"
            customWorkspace "<desired directory>"
        }

    }

    agent {
        docker {
            image "image-name"
            label "worker-node"
            args "-v /dir:dir"
        }
    }

    agent {
        dockerfile {
            filename "subdir/dockerfile name"
            label "worker-node"
            args "-v /dir:dir"
        }
    }

    environment {
        TIMEZONE = "eastern"
    }

}
