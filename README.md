# VCC_Asignment3


Document Report : Auto Scale Local VM to GCP 

Objective : To set up a local VM with resource monitoring and enable auto-scaling to Google Cloud when system resources exceed a defined threshold (e.g., 75%). A sample application will be deployed to demonstrate the complete flow.


Step 1 : Creation of Local VM on Virtual Box

•  Download Ubuntu ISO 
•  Open VirtualBox / VMware → Click "New".
•	Name: UbuntuVM1
•	Type: Linux → Ubuntu (64-bit)
•	Memory: 4GB (recommended)
•	Disk: 20GB dynamically allocated
•  Attach ISO and complete OS installation.

 

Step 2. Implementation of Resource Monitoring- Prometheus & Node Exporter
•	Download Prometheus using GUI & then configure Node exporter in the same way.
•	Visit the official Prometheus GitHub release page:
👉 https://prometheus.io/download/
•	Click on the Linux AMD64 tarball, Choose the latest version and download the file:

•	Open Files and navigate to your Downloads folder.
•	Right-click the downloaded .tar.gz file → Extract Here.
•	Open the extracted folder. You’ll see the prometheus binary file
•	Right-click the prometheus file → Properties.
•	Go to the Permissions tab.
•	Check "Allow executing file as program".
•	 
 
Step 3. Configuration of Cloud Auto-Scaling Policies and Resource Migration.
Platform: Google Cloud Platform (GCP)
Steps:
A. Install GCP CLI
B. Create Service Account & Download Key
1.	Go to IAM > Service Accounts.
2.	Create account with Compute Admin role.
3.	Generate JSON key file and save to VM.
 
 

C. Install Python Libraries
D. Python Script for Auto-Scaling
Create monitor_scale.py:
 
4.	Deployment of Sample Application

•	SSH into the GCP VM:
•	Install Flask:
•	Create app.py:
•	Run the app:



Architecture Design :

 


Repository:
https://github.com/iitjpb/VCC_Asignment3 














