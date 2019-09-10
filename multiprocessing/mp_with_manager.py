import multiprocessing

def insert_new_record(record, new_record):
    record.append(new_record)
    print record

def print_record(record):
    print record


if __name__ == '__main__':
    with multiprocessing.Manager() as manager:
        record = manager.list([1,2,3,4])
        new_record = 5
        p1 = multiprocessing.Process(target=insert_new_record, args=(record, new_record))
        p2 = multiprocessing.Process(target=print_record, args=(record,))

        p1.start()
        p1.join()

        p2.start()
        p2.join()

"""import multiprocessing 

def print_records(records): 
	for record in records: 
		print("Name: {0}\nScore: {1}\n".format(record[0], record[1])) 

def insert_record(record, records): 

	records.append(record) 
	print("New record added!\n") 

if __name__ == '__main__': 
	with multiprocessing.Manager() as manager: 
		# creating a list in server process memory 
		records = manager.list([('Sam', 10), ('Adam', 9), ('Kevin',9)]) 
		# new record to be inserted in records 
		new_record = ('Jeff', 8) 

		# creating new processes 
		p1 = multiprocessing.Process(target=insert_record, args=(new_record, records)) 
		p2 = multiprocessing.Process(target=print_records, args=(records,)) 

		# running process p1 to insert new record 
		p1.start() 
		p1.join() 

		# running process p2 to print records 
		p2.start() 
		p2.join() 

        
"""
