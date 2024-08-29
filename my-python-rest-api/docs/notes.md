# Install Python3
https://www.python.org/downloads/
python --version

# Install AWS CLI
https://aws.amazon.com/cli/

# Configure AWS IAM user
aws configure
aws sts get-caller-identity

# Install Node.js
https://nodejs.org
node --version

# Install serverless
npm install -g serverless

# Login severless user
https://app.serverless.com/
serverless login

# Install serverless offline
serverless plugin install -n serverless-offline

# Install packages to run offline
pip install boto3
pip install google-api-python-client google-auth

# Run serverless offline
serverless offline

# Package serverless
serverless package

# Deploy serverless
serverless deploy
