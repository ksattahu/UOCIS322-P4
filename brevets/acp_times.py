"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow


#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.
#
BREVET = [(200,15,34),(400,15,32),(600,15,30),(1000,11.428,28)]

def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
       brevet_dist_km: number, nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  A date object (arrow)
    Returns:
       A date object indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    if(control_dist_km == 0):
        return brevet_start_time
    sum = 0
    last = 0
    for b in BREVET:
        if (brevet_dist_km == 300) and (control_dist_km >= 300):
             return brevet_start_time.shift(hours=9)
        elif b[0] >= control_dist_km:
            sum += (control_dist_km - last) / b[2]
            minutes = round((sum - (sum//1))*60)
            return brevet_start_time.shift(hours=(sum//1), minutes=minutes)
        elif (1.2 * brevet_dist_km) >= control_dist_km and (b[0] >= brevet_dist_km):
            sum += (b[0] - last)/ b[2]
            minutes = round((sum - (sum//1))*60)
            return brevet_start_time.shift(hours=(sum//1), minutes=minutes)
        elif b[0] < control_dist_km:
            sum += (b[0] - last) / b[2]
            last = b[0]


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
          brevet_dist_km: number, nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  A date object (arrow)
    Returns:
       A date object indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    sum = 0
    last = 0
    for b in BREVET:
        if(control_dist_km <= 60):
            sum += (control_dist_km)/ 20
            minutes = round((sum - (sum//1))*60)
            return brevet_start_time.shift(hours=1+(sum//1), minutes=round(minutes))
        elif (brevet_dist_km == 300) and (control_dist_km >= 300):
             return brevet_start_time.shift(hours=20)
        elif b[0] > control_dist_km:
            sum += (control_dist_km - last) / b[1]
            minutes = round((sum - (sum//1))*60)
            return brevet_start_time.shift(hours=(sum//1), minutes=round(minutes))
        elif (1.2 * brevet_dist_km) >= control_dist_km and (b[0] >= brevet_dist_km):
            if(brevet_dist_km == 200):
                return brevet_start_time.shift(hours=13, minutes=30)
            elif(brevet_dist_km == 300):
                return brevet_start_time.shift(hours=20)
            elif(brevet_dist_km == 400):
                return brevet_start_time.shift(hours=27)
            elif(brevet_dist_km == 600):
                return brevet_start_time.shift(hours=40)
            elif(brevet_dist_km == 1000):
                return brevet_start_time.shift(hours=75)
        elif b[0] == control_dist_km:
            sum += (control_dist_km - last) / b[1]
            minutes = round((sum - (sum//1))*60)
            return brevet_start_time.shift(hours=(sum//1), minutes=round(minutes))
        elif b[0] < control_dist_km:
            sum += (b[0] - last) / b[1]
            last = b[0]
