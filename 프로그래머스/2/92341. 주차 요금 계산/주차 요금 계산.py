def calculate_time(start_time, finish_time):
    start_hour, start_minute = map(int, start_time.split(":"))
    finish_hour, finish_minute = map(int, finish_time.split(":"))
    
    time = finish_hour * 60 + finish_minute - (start_hour * 60 + start_minute ) 
    return time 
    
def ceiling(n, m) : 
    if n%m != 0 : 
        return n//m + 1
    else : 
        return n//m
    
    
def solution(fees, records):
    bus_record = dict()
    default_minute, default_money, unit_minute, unit_money = fees
    
    for record in records : 
        time, number, in_out = record.split()
        if number not in bus_record.keys() :
            bus_record[number] = dict()
            bus_record[number]["IN"] = []
            bus_record[number]["OUT"] = []
            bus_record[number]["FEE"] = 0
        bus_record[number][in_out].append(time) 
    
    
    for number in bus_record.keys():
        n = len(bus_record[number]["IN"])
        m = len(bus_record[number]["OUT"])
        duration = 0 
        
        if n > m : 
            for i in range(n-1):
                duration += calculate_time(bus_record[number]["IN"][i], bus_record[number]["OUT"][i])
            duration += calculate_time(bus_record[number]["IN"][-1], "23:59")
        else : 
            for i in range(n):
                duration += calculate_time(bus_record[number]["IN"][i], bus_record[number]["OUT"][i])
        
        bus_record[number]["FEE"] = default_money
        if duration > default_minute : 
            bus_record[number]["FEE"] += ceiling(duration-default_minute, unit_minute) * unit_money 
    
    keys = list(bus_record.keys())
    keys.sort()
    return [ bus_record[number]["FEE"] for number in keys ]