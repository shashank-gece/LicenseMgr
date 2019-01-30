import urllib2  # the lib that handles the url stuff
import os # the lib for deleting or searching file path

def ChangeKey(path) :
	if os.path.isfile(path):
		response = urllib2.urlopen('http://in01-lic02:9090/stats') # it's a file like object and works just like a file
		html = response.read() # Take all the data in the url
		Pkey = ["","","",""]
		TotSeats = [0,0,0,0]
		UsedSeats = [0,0,0,0]
		Pkey[0] = html[1095:1114]
		Pkey[1] = html[1572:1591]
		Pkey[2] = html[2049:2068]
		Pkey[3] = html[2526:2545]
		TotSeats[0] = int(html[1432:1434])
		TotSeats[1] = int(html[1909:1911])
		TotSeats[2] = int(html[2386:2388])
		TotSeats[3] = int(html[2863:2865])
		UsedSeats[0] = int(html[1471:1473])
		UsedSeats[1] = int(html[1948:1950])
		UsedSeats[2] = int(html[2425:2427])
		UsedSeats[3] = int(html[2902:2904])
		for i in range(4):
			if(TotSeats[i] > UsedSeats[i]):
				print '\n' + 'Avaliable key:' + Pkey[i] + '\n'
				Key = Pkey[i]
				os.remove(path)
				f = open(path,"w+")
				f.write("TSK_LICENSE_KEY_SW160800 = " + Key + "\nTSK_LICENSE_SERVER = in01-lic02:9090")
				f.close()
				print 'Avaliable key copied to licopt.txt file' + '\n'
				break
			if(i == 3):
				print 'Sorry, No license available at the moment'
	else:
		print '\n' + 'ERROR: File does not exist in the path specified in environment variable TSK_OPTIONS_FILE_SW160800' + '\n'
	raw_input('Script execution complete!! [Press ENTER]')

Envt_Var = 'TSK_OPTIONS_FILE_SW160800'
if os.getenv(Envt_Var) is not None:
	file_path = os.environ[Envt_Var]
	print 'License file path:' + file_path
	ChangeKey(file_path)
else:
	print '\n' + 'ERROR: Environment variable ' + Envt_Var + ' not present'
#print 'Product Key: ' + Pkey[0] + '  Total Seats: ' + str(TotSeats[0]) + '  Seats in use: ' + str(UsedSeats[0])
#print 'Product Key: ' + Pkey[1] + '  Total Seats: ' + str(TotSeats[1]) + '  Seats in use: ' + str(UsedSeats[1])
#print 'Product Key: ' + Pkey[2] + '  Total Seats: ' + str(TotSeats[2]) + '  Seats in use: ' + str(UsedSeats[2])
#print 'Product Key: ' + Pkey[3] + '  Total Seats: ' + str(TotSeats[3]) + '  Seats in use: ' + str(UsedSeats[3])
