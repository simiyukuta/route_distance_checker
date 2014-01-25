track=['AB','BC','CD','DC','DE','AD','CE','EB','AE']
track_distance=[5,4,8,8,6,5,2,3,7]
route=raw_input('Enter a  route\n')
route_length=len(route)
def check_route_existence(route):
	if route in track:
		  state='Route exists\n'
		  return state
	else:
		state='NO SUCH ROUTE\n'
		return state
	
def process_formula(route):
	if len(route)==2:
		f=check_route_existence(route)
		if f=='Route exists\n':
			x=track.index(route)
			print 'Total distance for route ',route,' is ',track_distance[x],' units'
		else:
			print 'NO SUCH ROUTE'
	elif len(route)==3:
		a=route[0]
		b=route[1]
		c=route[2]
		route1=a+b
		route2=b+c		
		f=check_route_existence(route1)
		g=check_route_existence(route2)
		if f=='Route exists\n':
			x=track.index(route1)
			route1_distance=track_distance[x]
		if g=='Route exists\n':
			r=track.index(route2)
			route2_distance=track_distance[r]
			total_distance=route1_distance+route2_distance
			print 'Total distance for route ',route,' is ',total_distance ,'units'
		else:
			print 'NO SUCH ROUTE'
	elif len(route)==5:
		a=route[0]
		b=route[1]
		c=route[2]
		d=route[3]
		e=route[4]
		route1=a+b
		route2=b+c
		route3=c+d
		route4=d+e		
		f=check_route_existence(route1)
		g=check_route_existence(route2)
		h=check_route_existence(route3)
		i=check_route_existence(route4)
		if f=='Route exists\n':
			x=track.index(route1)
			route1_distance=track_distance[x]
		if g=='Route exists\n':
			r=track.index(route2)
			route2_distance=track_distance[r]
		if h=='Route exists\n':
			m=track.index(route3)
			route3_distance=track_distance[m]
		if i=='Route exists\n':
			n=track.index(route4)
			route4_distance=track_distance[n]
			total_distance=route1_distance+route2_distance+route3_distance+route4_distance
			print 'Total distance for route ',route,' is ',total_distance ,'units'
		else:
			print 'NO SUCH ROUTE'
	else:
		print 'YOU ARE LOST,CALL POLICE'
			
			

process_formula(route)			
			
	


