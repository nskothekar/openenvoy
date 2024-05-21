### VPC Creation
- Create a new VPC in the AWS Management Console.
- Select "VPC and more" to configure VPC and networking components like route table, Internet g/w etc. 
- Enter the vpc name (prod-vpc) 
- Specify the IP address range (IPv4 CIDR block) for your VPC (10.0.0.0/16). 
- For now we will ignore ipv6. Click on **No IPv6 CIDR block** radio button 
- Select number of AZs (select 1) and select **us-east-1a**
- We need atleast 2 subnets, one public and one private. Select 1 public and private subnet
- Use default subnet CIDR blocks for public (10.0.0.0/20) and private (10.0.128.0/20) subnets 
- Since we would be running backend and database in private subnet which would need internet access, click on ** In 1 AZ ** under ** NAT Gateway **
- Keep rest setting as default and click on ** Create VPC **

### Internet Gateway  
- Create an Internet g/w and attach the Internet Gateway to your VPC.

### Route Tables 
- Create two route tables: one for the public subnet and one for the private subnet. 
- In the public subnet's route table, add a route that directs internet-bound traffic (0.0.0.0/0) to the Internet g/w.
```
        10.0.0.0/20  local
        0.0.0.0/0    igw-<gw_id> 
```
- In the private subnet's route table, just add the local entry.
```
        10.0.128.0/20 local
```

### Securing Connection 
  1. Using Security Groups 
- Create security groups to control inbound and outbound traffic to and from your instances. 
- For the web server instance in the public subnet, allow inbound HTTP (port 80) and HTTPS (port 443) traffic from anywhere (0.0.0.0/0) and outbound traffic to anywhere (0.0.0.0/0).  
- For instances in the private subnet, restrict inbound traffic to only allow necessary connections from the web server (add webserver security group in backend security group)  
- You would need a bastion server for access VMs like BE servers and databses in private subnets. Also add bastion servers security group in BE and DB servers SG and allow necessary ports like ssh, application port, etc 

2. Secure Communication
- To secure communication between your EC2 instances and the internet, you can use HTTPS (HTTP over SSL/TLS) for your web application.
- Configure your web server to use HTTPS and obtain a valid SSL/TLS certificate
- Ensure that your security group for the web server instance allows inbound HTTPS (port 443) traffic from anywhere (0.0.0.0/0)

