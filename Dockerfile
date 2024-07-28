FROM public.ecr.aws/lambda/python:3.12

# Install build-essential compiler and tools
RUN microdnf update -y && microdnf install -y gcc-c++ make

COPY requirements.txt ${LAMBDA_TASK_ROOT}

RUN pip install -r requirements.txt

COPY travelAgent.py ${LAMBDA_TASK_ROOT}

# Set permissions to allow file to be executable
RUN chmod +x travelAgent.py

# Set the CMD to your handler
CMD ["travelAgent.lambda_handler"]
