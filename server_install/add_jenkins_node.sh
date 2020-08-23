apt-get update
apt-get install openjdk-8-jdk curl -y
curl -O http://127.0.0.1:8080/jnlpJars/agent.jar
java -jar agent.jar -jnlpUrl http://localhost:8080/computer/localhost_1/slave-agent.jnlp -secret 0133bebc0f4a69d9bfc9fe7a6c612022b0cad8b9a1f6b529303aa530b7622d6d -workDir "/home"