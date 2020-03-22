# Twitter Video RESTFUL API

### Brian Macomber
#### EC500 - Building Software
#### Professor Osama Alshaykh

### Objectives:
- Use Flask as the web service platform for the Twitter Video API.
- Integrate the system to be a RESTFUL system and deploy it onto AWS.

### Summary:
This API is running on an AWS EC2 instance with the public IP of 3.135.235.40 ; 
To see more on how this API is created, view: https://github.com/BUEC500C1/video-brian-macomber



### How to run:
In a browser, go to the url `ec2-3-135-235-40.us-east-2.compute.amazonaws.com` to see the homepage.  
To queue a process and recieve a video, enter the following url and replace the desired username with USER:  
  `ec2-3-135-235-40.us-east-2.compute.amazonaws.com/tweets?user=USER`  
To view the list of past and current processes:  
  `ec2-3-135-235-40.us-east-2.compute.amazonaws.com/processes`



### References:
- https://blog.miguelgrinberg.com/post/designing-a-restful-api-using-flask-restful
- https://www.datasciencebytes.com/bytes/2015/02/24/running-a-flask-app-on-aws-ec2/  

##### Note: This is not always running, it is turned on upon request.
