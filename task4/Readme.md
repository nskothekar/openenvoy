### Install required python modules
```
pip3 install boto3 sys
```

### Install and configure aws cli  
- Follow the steps for installation [AWS CLI Installation](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html "Install AWS CLI")  
- Once installation is done, configure cli. Follow [this](https://docs.aws.amazon.com/cli/latest/reference/configure/ "Configure AWS CLI") document.

### Syntax to run the script
``` 
python3 aws_list_services.py <service> <region> <user_profile>
```

### Example 
```
python3 aws_list_services.py ec2 ap-south-1 nitish-p
```
