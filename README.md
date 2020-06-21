# check_out_system_git


Summary
===========

This repository contains flask server and check out system code.
Users can add products in cart and the system will show the total bill with discount (apply code) and without  discount.
There are 4 API 
1) /add_product
2) /add_product_in_cart
3) /show_product
4) /delete/<prd_cd>

Below is explanation of each API.
We can redirect to each api from home page as well i.e  http://127.0.0.1:5000 .
Each page has link for home page .

1) /add_product :
	This API is for adding products.
	Steps to add product :
		a) Run server
		b) Hit url http://127.0.0.1:5000/add_product
		c) Once you hit url , you will see "Add New Product" page with three fields Product Name , Product Code , Product price.
		d) All three fields are mandatory . If you skip the value of any field system won't allow you to save product .
		e) It also checks for valid value of Product price , it allows only int and float value .If you give any other value, an alert will pop up.
		f) You can give any value for Product Price and Product Code.
		g) Once you give a valid value , it will save in DB and will redirect to the message "successfully created!"

2) /add_product_in_cart :
		a) Run server
		b) Hit url http://127.0.0.1:5000/add_product_in_cart
		c) Once you hit url , you will see add_product_in_cart form with 4 column(Product Name,	Product Code, Unit Price, Quantity) and two buttons (submit and Get Bill)
		e) You can give value only for Quantity field and for remaining three field shows only product information. Form will be look like below 
		
		Product Name	Product Code	Unit Price	Quantity

			Chai	CH1	         $ 3.11	        <Input> 
			Coffee	CF1	         $ 11.23        <Input> 
			Milk	MK1	         $ 4.75         <Input>
			Oatmeal	OM1	         $ 3.69         <Input>
			Apples	AP1	         $ 6            <Input>
		
		f) If you want to add item in cart like as below:
			CH1, AP1, AP1, AP1, MK1
		then you need to give 1 for CH1 Quantity input field , 3 for AP1 Quantity input field and 1 for MK1 Quantity input field
		If you are in between shopping but you want to see your bill then you need to click on the get bill button ,the system will calculate Total bill with applying code 
		and format of output will be like in the same form.
		
						
					Product : CH1	Price : 3.11
					Product : MK1	Price : 4.75
					Product : AP1	Price : 18.0
					Total Bill without discount : 25.86
					Applied Code : APPL	Discount Price : -4.5
					Applied Code : CHMK	Discount Price : -4.75
					Total discount amount : -9.25

					Total Bill 16.61
		g) There are multiple validations for this form . You need to give quantity for at least one product , it will allow you only for integer value . You can't give text or alphanumeric value
		h) Once you are done with shopping you can click on the submit button , it will show the bill in the same format as above but it will redirect to another page.
		

3) /show_product
		a) Run server
		b) Hit url http://127.0.0.1:5000/show_product
		c) Once you hit url , you will see Available Product list in tabular form.
4) /delete
		a) Run server
		b) Hit url http://127.0.0.1:5000/delete/<prd_cd> and hit enter.
		c) After deleting product after deleting product , it shows message "successfully deleted!"
		d) If there is not any product is exist with <prd_cd> , then it will show message "Error deleting #test"


Steps to setup:
----------------

install Python3.7 and Docker in your system .
1) Clone the repository:

    - git clone https://github.com/mjayant/check_out_system_git.git

To run code in docker container please follow below steps-
-------------------

i) Build the docker image
	Note: Before running below comand , make sure you are in parent dir of src folder .

    -   docker build -t <image_name:tag> -f src/Dockerfile .

    Note: Navigate to parent  folder i.e checkout_system_git then execute above command.


ii) Run the container:

    - docker run --rm -t -p 5000:5000 <image_name:tag>

    Note: Please check the proxy if you are in secured connection.
    Now, the container is up and running.

Run flask server in local system, this is only for local not for docker
------------------

i) Navigate to src folder and execute below command-

    - pip3 install -r requirements.txt

ii) Start the development server

    - python app.py


Open browser and type the below url:

    - http://127.0.0.1:5000/<api>



Unittest:
-----------
Before executing test cases make sure checkout_system app’s container is up and running.
Follow below step:
1) Run docker ps  command in your terminal
2) Copy container id 
3) run command: docker exec -it <container_id> pytest -s -v

Or you can test locally 
1) Navigate parent folder i.e check_out_system_git or <other_folder_name>(if you have cloned using this command: git clone https://github.com/mjayant/check_out_system_git.git <other_folder_name>)
2) Start server using: python src/app.py
3)  Then run command : pytest -s -v

Coverage Report:
------------

Install coverage(pip install coverage) and execute below command after installing coverage:

<To_Do>
