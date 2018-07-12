# Review of Clients, Servers and Protocols

Clients and servers can be most simply understood as computers communicating across the Internet.

We define the **client** as the computer who wants information, and the **server** as the computer that has information that can be shared with clients.

This means that a **client** has to initiate communication to request information, while the **server** constantly stays listening for any clients to communicate with it, and responds with the data that the client requested.

Let's briefly discuss some of the important concepts in order to better understand how this actually happens.

So we know that clients and servers can communicate with each other, but how do we know that they're all speaking the same language? Well, **Protocols** are like the gramatical rules that we use to make sure all machines on the Internet are communicating in the same way.

There are several procotols that computers on the Internet adhere to. The most common three are:
1. Transmission Control Protocol, or TCP
2. Internet Protocol, or IP
3. Hypertext Transfer Protocol, or HTTP

The **Transmission Control Protocol (TCP)** enables information to be broken into small packets and sent between clients and servers.

> If a packet is lost somewhere along the way the sender and receiver have a way of figuring out which of the packets is missing and request that they be resent.

The counterpart to TCP is **User Datagram Protocol (UDP)**, which is good for streaming content like music or video.

Similar to postal addresses, **IP addresses** allow messages to be properly routed to all participants on the Internet.

For simplicity's sake, we can assume that every device on the Internet gets an IP address that is either statically or dynamically assigned by the Internet service provider.

When you type google.com into your browser, your computer first figures out the IP address of Google by looking it up in a **Domain Name Server, or DNS**.

Think of **DNS** as a big online phonebook that finds the IP addresses of web URLs.

Once DNS gives your computer the IP address, it uses that address to initiate communication with the server for Google.

Since multiple applications using the Internet can run on one machine, operating systems use **Ports** to designate channels of communication on the same IP address.

Placing a colon after an IP address, with another number, like so: `66.249.95.255:8080`, indicates that we want to communicate on a specific port on the device using that IP address.

On most machines, port numbers can range from 0 to 65,536. The first 10,000 ports are often times reserved by the operating system for a specific use.

**Port 80** is the most common port for web servers. So most websites we use every day are hitting port 80 when they reach a server. **Port 8080** is also a common port for web communications.

When client and server applications are on the same machine, we indicate this with the term *localhost*. **Localhost** also has a special IP address of `127.0.0.1`. Whenever we type "localhost", or this special IP address into a browser or web application, the operating system knows to look for this resource *locally* and not to go out to the Internet.
