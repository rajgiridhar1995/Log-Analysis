#Log Analysis

Before running the code you need to setup up a virtual machine. Install VirtualBox and Vagrant in your system.
Clone the repository from by typing 'git clone https://github.com/udacity/fullstack-nanodegree-vm' from the terminal. cd into vagrant folder. Run the command 'vagrant up' in your terminal to install the operating system as per the Vagrantfile.

You will need Python3 and PostgreSQL installed on your system.

The following Python3 packages are required:
- psycopg2

Download the sql dump file from [this link](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). After you have downloaded the zip file extract it. To load the data into the database, use the command 'psql -d news -f newsdata.sql'

This will create a new database named 'news'. To execute the program, run the following command on your terminal 'python3 main.py'
