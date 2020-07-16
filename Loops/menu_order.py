#### Update Order  
##
##def update_order(new_item, current_order=None):
##    if current_order is None:
##        current_order = []
##        current_order.append(new_item)
##        return current_order
##
### First order, burger and a soda
##order1 = update_order({'item': 'burger', 'cost': '3.50'})
##order1 = update_order({'item': 'soda', 'cost': '1.50'}, order1)
##
### Second order, just a soda
##order2 = update_order({'item': 'soda', 'cost': '1.50'})
##
### What's in that second order again?
##print(order2)


#########################################

import datetime as dt
#def log_time(message, time=dt.datetime.now()):
def log_time(message, time):
    
    print("{0}: {1}".format(time.isoformat(), message))

log_time("log message 1, ", time=dt.datetime.now())

log_time("log message 2, ", time=dt.datetime.now())
log_time("log message 3, ", time=dt.datetime.now())
log_time("log message 4, ", time=dt.datetime.now())
log_time("log message 5, ", time=dt.datetime.now())
log_time("log message 6, ", time=dt.datetime.now())

















