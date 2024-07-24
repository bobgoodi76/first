FROM gitpod/workspace-full

# Install Python dependencies
RUN pip install --upgrade pip

# Install MySQL client
RUN sudo apt-get update && sudo apt-get install -y mysql-client
