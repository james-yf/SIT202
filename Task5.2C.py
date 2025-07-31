"""
initialise dictionary CNAME_records
initialise dictionary A_records.

initalise server_addr = localhost 
initalise server_port = some port #

create server socket

bind the socket to server_addr and server_port

print "server is waiting for a query"

loop infinitely
    query = message from the client

    if query == quit
        exit loop

    elif query is in A_records
        get the IP address from A_records
        send the IP address to the client

    elif query is in CNAME_records
        if CNAME is in A_records
            get the IP address from A_records
            send it to the client
        else
            send "the domain does not exist in A records"

    else
        send "the domain does not exist" to the client

close the socket

"""





