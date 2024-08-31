#KBC

fiftyfifty=0
changeQ=0
while True:
	accept=input('Enter Yes or No to  start the KBC : ')
	if(accept=='Yes'):
		print('1. The International Literacy Day is observed on : \nA. Sep 8\nB. Nov 28\nC. May 2\nD. Sep 22')
		win=int(input('Want a lifeline then enter 1 or enter any no. : '))
		if(win==1):

			if(fiftyfifty==0 and changeQ==0):
				print('You have two lifelines : \n1.50-50 \n2.Change the Question')
				lifeline=int(input('Enter 1 or 2 to continue : '))
				if(lifeline==1):
					fiftyfifty=1
					print('A. Sep 8\nD. Sep 22')
					option=input('Enter the correct option : ')
					if(option=='A' or option=='a'):
						print('Won 10 Lakh.')
					else:
						print('Incorrect Answer!!')
						exit()
				elif(lifeline==2):
					changeQ=1
					print('Question Changed :\nGood Friday is observed to commemorate the event of \nA. Birth of Jesus Christ\nB. Birth of St Peter \nC. Crucification of Jesus Christ \nD. Rebirth of Jesus Christ')
					option=input('Enter the correct option : ')
					if(option=='C' or option=='c'):
						print('Won 10 Lakh.')
					else:
						print('Incorrect Answer!!')
						exit()
				else:
					print('You have 2 lifelines left.')
	

			elif(fiftyfifty==0 and changeQ==1):
				fiftyfifty=1
				print('A. Sep 8\nD. Sep 22')
				option=input('Enter the correct option : ')
				if(option=='A' or option=='a'):
					print('Won 10 Lakh.')
				else:
					print('Incorrect Answer!!')
					exit()
	
	
			elif(fiftyfifty==1 and changeQ==0):
				changeQ=1
				print('Question Changed :\nGood Friday is observed to commemorate the event of \nA. Birth of Jesus Christ\nB. Birth of St Peter \nC. Crucification of Jesus Christ \nD. Rebirth of Jesus Christ')
				option=input('Enter the correct option : ')
				if(option=='C' or option=='c'):
					print('Won 10 Lakh.')
				else:
					print('Incorrect Answer!!')
					exit()

			else:
				print('No lifeline left.')			
				option=input('Enter the correct option : ')
				if(option=='A' or option=='a'):
					print('Won 10 Lakh.')
				else:
					print('Incorrect Answer!!')
					exit()


		else:
			option=input('Enter the correct option : ')
			if(option=='A' or option=='a'):
				print('Won 10 Lakh.')
			else:
				print('Incorrect Answer!!')
				exit()





	
		print('2. The language of Lakshadweep, a union Territory of India is : \nA. Tamil\nB. Hindi\nC. Malyalam\nD. Telugu')
		win=int(input('Want a lifeline then enter 1 or enter any no. : '))
		if(win==1):

			if(fiftyfifty==0 and changeQ==0):
				print('You have two lifelines : \n1.50-50 \n2.Change the Question')
				lifeline=int(input('Enter 1 or 2 to continue : '))
				if(lifeline==1):
					fiftyfifty=1
					print('A. Tamil\nC. Malyalam')
					option=input('Enter the correct option : ')
					if(option=='C' or option=='c'):
						print('Won 20 Lakh.')
					else:
						print('Incorrect Answer!! Won 10 Lakh.')
						exit()
				elif(lifeline==2):
					changeQ=1
					print('Question Changed :\nGood Friday is observed to commemorate the event of \nA. Birth of Jesus Christ\nB. Birth of St Peter \nC. Crucification of Jesus Christ \nD. Rebirth of Jesus Christ')
					option=input('Enter the correct option : ')
					if(option=='C' or option=='c'):
						print('Won 20 Lakh.')
					else:
						print('Incorrect Answer!! Won 10 Lakh.')
						exit()
				else:
					print('You have 2 lifelines left.')
	
	
			elif(fiftyfifty==0 and changeQ==1):
				fiftyfifty=1
				print('A. Tamil\nC. Malyalam')
				option=input('Enter the correct option : ')
				if(option=='C' or option=='c'):
					print('Won 20 Lakh.')
				else:
					print('Incorrect Answer!! Won 10 lakh.')
					exit()
	

			elif(fiftyfifty==1 and changeQ==0):
				changeQ=1
				print('Question Changed :\nGood Friday is observed to commemorate the event of \nA. Birth of Jesus Christ\nB. Birth of St Peter \nC. Crucification of Jesus Christ \nD. Rebirth of Jesus Christ')
				option=input('Enter the correct option : ')
				if(option=='C' or option=='c'):
					print('Won 20 Lakh.')
				else:
					print('Incorrect Answer!! Won 10 Lakh.')
					exit()

			else:
				print('No lifeline left.')
				option=input('Enter the correct option : ')
				if(option=='C' or option=='c'):
					print('Won 10 Lakh.')
				else:
					print('Incorrect Answer!!')
					exit()

		else:
			option=input('Enter the correct option : ')
			if(option=='C' or option=='c'):
				print('Won 20 Lakh.')
			else:
				print('Incorrect Answer!! Won 10 Lakh.')
				exit()





	
		print('3. In which group of places the Kumbha Mela is held every twelve years : \nA. Ujjain, Purl, Prayag,  haridwar\nB. Prayag, Haridwar, Ujjain, Nasik\nC. Rameshwaram, Purl, Badrinath, Dwarika\nD. Chittakoot,Ujjain, Prayag, Haridwar')
		win=int(input('Want a lifeline then enter 1 or enter any no. : '))
		if(win==1):

			if(fiftyfifty==0 and changeQ==0):
				print('You have two lifelines : \n1.50-50 \n2.Change the Question')
				lifeline=int(input('Enter 1 or 2 to continue : '))
				if(lifeline==1):
					fiftyfifty=1
					print('B. Prayag, Haridwar, Ujjain, Nasik\nC. Rameshwaram, Purl, Badrinath, Dwarika')
					option=input('Enter the correct option : ')
					if(option=='B' or option=='b'):
						print('Won 30 Lakh.')
					else:
						print('Incorrect Answer!! Won 20 Lakh.')
						exit()
				elif(lifeline==2):
					changeQ=1
					print('Question Changed :\nGood Friday is observed to commemorate the event of \nA. Birth of Jesus Christ\nB. Birth of St Peter \nC. Crucification of Jesus Christ \nD. Rebirth of Jesus Christ')
					option=input('Enter the correct option : ')
					if(option=='C' or option=='c'):
						print('Won 30 Lakh.')
					else:
						print('Incorrect Answer!! Won 20 Lakh.')
						exit()
				else:
					print('You have 2 lifelines left.')


			elif(fiftyfifty==0 and changeQ==1):
				fiftyfifty=1
				print('B. Prayag, Haridwar, Ujjain, Nasik\nC. Rameshwaram, Purl, Badrinath, Dwarika')
				option=input('Enter the correct option : ')
				if(option=='B' or option=='b'):
					print('Won 30 Lakh.')
				else:
					print('Incorrect Answer!! Won 20 lakh.')
					exit()


			elif(fiftyfifty==1 and changeQ==0):
				changeQ=1
				print('Question Changed :\nGood Friday is observed to commemorate the event of \nA. Birth of Jesus Christ\nB. Birth of St Peter \nC. Crucification of Jesus Christ \nD. Rebirth of Jesus Christ')
				option=input('Enter the correct option : ')
				if(option=='C' or option=='c'):
					print('Won 30 Lakh.')
				else:
					print('Incorrect Answer!! Won 20 Lakh.')
					exit()

			else:
				print('No lifeline left.')
				option=input('Enter the correct option : ')
				if(option=='B' or option=='b'):
					print('Won 10 Lakh.')
				else:
					print('Incorrect Answer!!')
					exit()


		else:
			option=input('Enter the correct option : ')
			if(option=='B' or option=='b'):
				print('Won 30 Lakh.')
			else:
				print('Incorrect Answer!! Won 20 Lakh.')
				exit()







		print('4. Bahubali festival is related to : \nA. Islam\nB. Hinduism\nC. Buddhism\nD. Jainism')
		win=int(input('Want a lifeline then enter 1 or enter any no. : '))
		if(win==1):

			if(fiftyfifty==0 and changeQ==0):
				print('You have two lifelines : \n1.50-50 \n2.Change the Question')
				lifeline=int(input('Enter 1 or 2 to continue : '))
				if(lifeline==1):
					fiftyfifty=1
					print('B. Hinduism\nD. Jainism')
					option=input('Enter the correct option : ')
					if(option=='D' or option=='d'):
						print('Won 40 Lakh.')
					else:
						print('Incorrect Answer!! Won 30 Lakh.')
						exit()
				elif(lifeline==2):
					changeQ=1
					print('Question Changed :\nGood Friday is observed to commemorate the event of \nA. Birth of Jesus Christ\nB. Birth of St Peter \nC. Crucification of Jesus Christ \nD. Rebirth of Jesus Christ')
					option=input('Enter the correct option : ')
					if(option=='C' or option=='c'):
						print('Won 40 Lakh.')
					else:
						print('Incorrect Answer!! Won 30 Lakh.')
						exit()
				else:
					print('You have 2 lifelines left.')


			elif(fiftyfifty==0 and changeQ==1):
				fiftyfifty=1
				print('B. Hinduism\nD. Jainism')
				option=input('Enter the correct option : ')
				if(option=='D' or option=='d'):
					print('Won 40 Lakh.')
				else:
					print('Incorrect Answer!! Won 30 lakh.')
					exit()


			elif(fiftyfifty==1 and changeQ==0):
				changeQ=1
				print('Question Changed :\nGood Friday is observed to commemorate the event of \nA. Birth of Jesus Christ\nB. Birth of St Peter \nC. Crucification of Jesus Christ \nD. Rebirth of Jesus Christ')
				option=input('Enter the correct option : ')
				if(option=='C' or option=='c'):
					print('Won 40 Lakh.')
				else:
					print('Incorrect Answer!! Won 30 Lakh.')
					exit()
			else:
				print('No lifeline left.')
				option=input('Enter the correct option : ')
				if(option=='D' or option=='d'):
					print('Won 10 Lakh.')
				else:
					print('Incorrect Answer!!')
					exit()



		else:
			option=input('Enter the correct option : ')
			if(option=='D' or option=='d'):
				print('Won 40 Lakh.')
			else:
				print('Incorrect Answer!! Won 30 Lakh.')
				exit()

		





		print('5. Which day is observed as the World Standards  Day? : \nA. June 26\nB. Oct 14\nC. Nov 15\nD. Dec 2')
		win=int(input('Want a lifeline then enter 1 or enter any no. : '))
		if(win==1):
		

			if(fiftyfifty==0 and changeQ==0):
				print('You have two lifelines : \n1.50-50 \n2.Change the Question')
				lifeline=int(input('Enter 1 or 2 to continue : '))
				if(lifeline==1):
					fiftyfifty=1
					print('B. Oct 14\nC. Nov 15')
					option=input('Enter the correct option : ')
					if(option=='B' or option=='b'):
						print('Won 50 Lakh.')
					else:
						print('Incorrect Answer!! Won 40 Lakh.')
						exit()
				elif(lifeline==2):
					changeQ=1
					print('Question Changed :\nGood Friday is observed to commemorate the event of \nA. Birth of Jesus Christ\nB. Birth of St Peter \nC. Crucification of Jesus Christ \nD. Rebirth of Jesus Christ')
					option=input('Enter the correct option : ')
					if(option=='C' or option=='c'):
						print('Won 50 Lakh.')
					else:
						print('Incorrect Answer!! Won 40 Lakh.')
						exit()
				else:
					print('You have 2 lifelines left.')


			elif(fiftyfifty==0 and changeQ==1):
				fiftyfifty=1
				print('B. Oct 14\nC. Nov 15')
				option=input('Enter the correct option : ')
				if(option=='B' or option=='b'):
					print('Won 50 Lakh.')
				else:
					print('Incorrect Answer!! Won 40 lakh.')
					exit()


			elif(fiftyfifty==1 and changeQ==0):
				changeQ=1
				print('Question Changed :\nGood Friday is observed to commemorate the event of \nA. Birth of Jesus Christ\nB. Birth of St Peter \nC. Crucification of Jesus Christ \nD. Rebirth of Jesus Christ')
				option=input('Enter the correct option : ')
				if(option=='C' or option=='c'):
					print('Won 50 Lakh.')
				else:
					print('Incorrect Answer!! Won 40 Lakh.')
					exit()

			else:
				print('No lifeline left.')
				option=input('Enter the correct option : ')
				if(option=='B' or option=='b'):
					print('Won 10 Lakh.')
				else:
					print('Incorrect Answer!!')
					exit()



		else:
			option=input('Enter the correct option : ')
			if(option=='B' or option=='b'):
				print('Won 50 Lakh.')
			else:
				print('Incorrect Answer!! Won 40 Lakh.')
				exit()

		





		print('6. Which of the following was the theme of the World Red Cross and Red Crescent Day? : \nA. Dignity for all - focus on women\nB. Dignity for all - focus on Children\nC. Focus on health for all\nD. Nourishment for all-focus on children')
		win=int(input('Want a lifeline then enter 1 or enter any no. : '))
		if(win==1):

			if(fiftyfifty==0 and changeQ==0):
				print('You have two lifelines : \n1.50-50 \n2.Change the Question')
				lifeline=int(input('Enter 1 or 2 to continue : '))
				if(lifeline==1):
					fiftyfifty=1
					print('A. Dignity for all - focus on women\nB. Dignity for all - focus on Children')
					option=input('Enter the correct option : ')
					if(option=='B' or option=='b'):
						print('Won 60 Lakh.')
					else:
						print('Incorrect Answer!! Won 50 Lakh.')
						exit()
				elif(lifeline==2):
					changeQ=1
					print('Question Changed :\nGood Friday is observed to commemorate the event of \nA. Birth of Jesus Christ\nB. Birth of St Peter \nC. Crucification of Jesus Christ \nD. Rebirth of Jesus Christ')
					option=input('Enter the correct option : ')
					if(option=='C' or option=='c'):
						print('Won 60 Lakh.')
					else:
						print('Incorrect Answer!! Won 50 Lakh.')
						exit()
				else:
					print('You have 2 lifelines left.')


			elif(fiftyfifty==0 and changeQ==1):
				fiftyfifty=1
				print('A. Dignity for all - focus on women\nB. Dignity for all - focus on Children')
				option=input('Enter the correct option : ')
				if(option=='B' or option=='b'):
					print('Won 60 Lakh.')
				else:
					print('Incorrect Answer!! Won 50 lakh.')
					exit()


			elif(fiftyfifty==1 and changeQ==0):
				changeQ=1
				print('Question Changed :\nGood Friday is observed to commemorate the event of \nA. Birth of Jesus Christ\nB. Birth of St Peter \nC. Crucification of Jesus Christ \nD. Rebirth of Jesus Christ')
				option=input('Enter the correct option : ')
				if(option=='C' or option=='c'):
					print('Won 60 Lakh.')
				else:
					print('Incorrect Answer!! Won 50 Lakh.')
					exit()

			else:
				print('No lifeline left.')
				option=input('Enter the correct option : ')
				if(option=='B' or option=='b'):
					print('Won 10 Lakh.')
				else:
					print('Incorrect Answer!!')
					exit()



		else:
			option=input('Enter the correct option : ')
			if(option=='B' or option=='b'):
				print('Won 60 Lakh.')
			else:
				print('Incorrect Answer!! Won 50 Lakh.')
				exit()

		






		print('7. September 27 is celebrated every year as : \nA. Teachers Day\nB. National Integration Day\nC. World Tourism Day\nD. International Literacy Day')
		win=int(input('Want a lifeline then enter 1 or enter any no. : '))
		if(win==1):

			if(fiftyfifty==0 and changeQ==0):
				print('You have two lifelines : \n1.50-50 \n2.Change the Question')
				lifeline=int(input('Enter 1 or 2 to continue : '))
				if(lifeline==1):
					fiftyfifty=1
					print('A. Teachers Day\nC. World Tourism Day')
					option=input('Enter the correct option : ')
					if(option=='C' or option=='c'):
						print('Won 70 Lakh.')
					else:
						print('Incorrect Answer!! Won 60 Lakh.')
						exit()
				elif(lifeline==2):
					changeQ=1
					print('Question Changed :\nGood Friday is observed to commemorate the event of \nA. Birth of Jesus Christ\nB. Birth of St Peter \nC. Crucification of Jesus Christ \nD. Rebirth of Jesus Christ')
					option=input('Enter the correct option : ')
					if(option=='C' or option=='c'):
						print('Won 70 Lakh.')
					else:
						print('Incorrect Answer!! Won 60 Lakh.')
						exit()
				else:
					print('You have 2 lifelines left.')


			elif(fiftyfifty==0 and changeQ==1):
				fiftyfifty=1
				print('A. Teachers Day\nC. World Tourism Day')
				option=input('Enter the correct option : ')
				if(option=='C' or option=='c'):
					print('Won 70 Lakh.')
				else:
					print('Incorrect Answer!! Won 60 lakh.')
					exit()


			elif(fiftyfifty==1 and changeQ==0):
				changeQ=1
				print('Question Changed :\nGood Friday is observed to commemorate the event of \nA. Birth of Jesus Christ\nB. Birth of St Peter \nC. Crucification of Jesus Christ \nD. Rebirth of Jesus Christ')
				option=input('Enter the correct option : ')
				if(option=='C' or option=='c'):
					print('Won 70 Lakh.')
				else:
					print('Incorrect Answer!! Won 60 Lakh.')
					exit()

			else:
				print('No lifeline left.')
				option=input('Enter the correct option : ')
				if(option=='C' or option=='c'):
					print('Won 10 Lakh.')
				else:
					print('Incorrect Answer!!')
					exit()



		else:
			option=input('Enter the correct option : ')
			if(option=='C' or option=='c'):
				print('Won 70 Lakh.')
			else:
				print('Incorrect Answer!! Won 60 Lakh.')
				exit()

		





		print('8. Who is the author of Manas Ka-Hans ? : \nA. Khushwant Singh\nB. Prem Chand\nC. Jayashankar Prasad\nD. Amrit Lal Nagar')
		win=int(input('Want a lifeline then enter 1 or enter any no. : '))
		if(win==1):


			if(fiftyfifty==0 and changeQ==0):
				print('You have two lifelines : \n1.50-50 \n2.Change the Question')
				lifeline=int(input('Enter 1 or 2 to continue : '))
				if(lifeline==1):
					fiftyfifty=1
					print('B. Prem Chand\nD. Amrit Lal Nagar')
					option=input('Enter the correct option : ')
					if(option=='D' or option=='d'):
						print('Won 80 Lakh.')
					else:
						print('Incorrect Answer!! Won 70 Lakh.')
						exit()
				elif(lifeline==2):
					changeQ=1
					print('Question Changed :\nGood Friday is observed to commemorate the event of \nA. Birth of Jesus Christ\nB. Birth of St Peter \nC. Crucification of Jesus Christ \nD. Rebirth of Jesus Christ')
					option=input('Enter the correct option : ')
					if(option=='C' or option=='c'):
						print('Won 80 Lakh.')
					else:
						print('Incorrect Answer!! Won 70 Lakh.')
						exit()
				else:
					print('You have 2 lifelines left.')


			elif(fiftyfifty==0 and changeQ==1):
				fiftyfifty=1
				print('B. Prem Chand\nD. Amrit Lal Nagar')
				option=input('Enter the correct option : ')
				if(option=='D' or option=='d'):
					print('Won 80 Lakh.')
				else:
					print('Incorrect Answer!! Won 70 lakh.')
					exit()


			elif(fiftyfifty==1 and changeQ==0):
				changeQ=1
				print('Question Changed :\nGood Friday is observed to commemorate the event of \nA. Birth of Jesus Christ\nB. Birth of St Peter \nC. Crucification of Jesus Christ \nD. Rebirth of Jesus Christ')
				option=input('Enter the correct option : ')
				if(option=='C' or option=='c'):
					print('Won 80 Lakh.')
				else:
					print('Incorrect Answer!! Won 70 Lakh.')
					exit()

			else:
				print('No lifeline left.')
				option=input('Enter the correct option : ')
				if(option=='D' or option=='d'):
					print('Won 10 Lakh.')
				else:
					print('Incorrect Answer!!')
					exit()



		else:
			option=input('Enter the correct option : ')
			if(option=='D' or option=='d'):
				print('Won 80 Lakh.')
			else:
				print('Incorrect Answer!! Won 70 Lakh.')
				exit()

		






		print('9. The death anniversary of which of the following leaders is observed as Martyrs Day? : \nA. Smt. Indira Gandhi\nB. PI. Jawaharlal Nehru\nC. Mahatma Oandhi\nD. Lal Bahadur Shastri')
		win=int(input('Want a lifeline then enter 1 or enter any no. : '))
		if(win==1):


			if(fiftyfifty==0 and changeQ==0):
				print('You have two lifelines : \n1.50-50 \n2.Change the Question')
				lifeline=int(input('Enter 1 or 2 to continue : '))
				if(lifeline==1):
					fiftyfifty=1
					print('C. Mahatma Oandhi\nD. Lal Bahadur Shastri')
					option=input('Enter the correct option : ')
					if(option=='C' or option=='c'):
						print('Won 90 Lakh.')
					else:
						print('Incorrect Answer!! Won 80 Lakh.')
						exit()
				elif(lifeline==2):
					changeQ=1
					print('Question Changed :\nGood Friday is observed to commemorate the event of \nA. Birth of Jesus Christ\nB. Birth of St Peter \nC. Crucification of Jesus Christ \nD. Rebirth of Jesus Christ')
					option=input('Enter the correct option : ')
					if(option=='C' or option=='c'):
						print('Won 90 Lakh.')
					else:
						print('Incorrect Answer!! Won 80 Lakh.')
						exit()
				else:
					print('You have 2 lifelines left.')


			elif(fiftyfifty==0 and changeQ==1):
				fiftyfifty=1
				print('C. Mahatma Oandhi\nD. Lal Bahadur Shastri')
				option=input('Enter the correct option : ')
				if(option=='C' or option=='c'):
					print('Won 90 Lakh.')
				else:
					print('Incorrect Answer!! Won 80 lakh.')
					exit()


			elif(fiftyfifty==1 and changeQ==0):
				changeQ=1
				print('Question Changed :\nGood Friday is observed to commemorate the event of \nA. Birth of Jesus Christ\nB. Birth of St Peter \nC. Crucification of Jesus Christ \nD. Rebirth of Jesus Christ')
				option=input('Enter the correct option : ')
				if(option=='C' or option=='c'):
					print('Won 90 Lakh.')
				else:
					print('Incorrect Answer!! Won 80 Lakh.')
					exit()

			else:
				print('No lifeline left.')
				option=input('Enter the correct option : ')
				if(option=='C' or option=='c'):
					print('Won 10 Lakh.')
				else:
					print('Incorrect Answer!!')
					exit()



		else:
			option=input('Enter the correct option : ')
			if(option=='C' or option=='c'):
				print('Won 90 Lakh.')
			else:
				print('Incorrect Answer!! Won 80 Lakh.')
				exit()

		






		print('10. Who is the author of the epic Meghdoot? : \nA. Vishakadatta\nB. Valmiki\nC. Banabhatta\nD. Kalidas')
		win=int(input('Want a lifeline then enter 1 or enter any no. : '))
		if(win==1):

			if(fiftyfifty==0 and changeQ==0):
				print('You have two lifelines : \n1.50-50 \n2.Change the Question')
				lifeline=int(input('Enter 1 or 2 to continue : '))
				if(lifeline==1):
					fiftyfifty=1
					print('B. Valmiki\nD. Kalidas')
					option=input('Enter the correct option : ')
					if(option=='D' or option=='d'):
						print('Won 1 Crore.')
					else:
						print('Incorrect Answer!! Won 90 Lakh.')
						exit()
				elif(lifeline==2):
					changeQ=1
					print('Question Changed :\nGood Friday is observed to commemorate the event of \nA. Birth of Jesus Christ\nB. Birth of St Peter \nC. Crucification of Jesus Christ \nD. Rebirth of Jesus Christ')
					option=input('Enter the correct option : ')
					if(option=='C' or option=='c'):
						print('Won 1 Crore.')
					else:
						print('Incorrect Answer!! Won 90 Lakh.')
						exit()
				else:
					print('You have 2 lifelines left.')


			elif(fiftyfifty==0 and changeQ==1):
				fiftyfifty=1
				print('B. Valmiki\nD. Kalidas')
				option=input('Enter the correct option : ')
				if(option=='D' or option=='d'):
					print('Won 1 Crore.')
				else:
					print('Incorrect Answer!! Won 90 lakh.')
					exit()


			elif(fiftyfifty==1 and changeQ==0):
				changeQ=1
				print('Question Changed :\nGood Friday is observed to commemorate the event of \nA. Birth of Jesus Christ\nB. Birth of St Peter \nC. Crucification of Jesus Christ \nD. Rebirth of Jesus Christ')
				option=input('Enter the correct option : ')
				if(option=='C' or option=='c'):
					print('Won 1 Crore.')
				else:
					print('Incorrect Answer!! Won 90 Lakh.')
					exit()

			else:
				print('No lifeline left.')
				option=input('Enter the correct option : ')
				if(option=='D' or option=='d'):
					print('Won 10 Lakh.')
				else:
					print('Incorrect Answer!!')
					exit()



		else:
			option=input('Enter the correct option : ')
			if(option=='D' or option=='d'):
				print('Won 1 Crore.')
			else:
				print('Incorrect Answer!! Won 90 Lakh.')
				exit()

		





	else:
		print('Are You Sure :' )
		confirm=int(input('Enter 0 to end or any number to continue : '))
		if(confirm==0):
			print('End!!!')
			exit()