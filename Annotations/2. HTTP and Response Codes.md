# HTTP and Response Codes

The main concept of HTTP is that clients tell servers what they want by using an HTTP verb, also known an **HTTP method**.

There are **9** HTTP verbs in the current HTTP specification. They are:

1. **GET**

  The `GET` method requests a representation of the specified resource. Requests using GET should only retrieve data.

2. **HEAD**

  The `HEAD` method asks for a response identical to that of a `GET` request, but without the response body.

3. **POST**

  The `POST` method is used to submit an entity to the specified resource, often causing a change in state or side effects on the server.

4. **PUT**

  The `PUT` method replaces all current representations of the target resource with the request payload.

5. **DELETE**

  The `DELETE` method deletes the specified resource.

6. **CONNECT**

  The `CONNECT` method establishes a tunnel to the server identified by the target resource.

7. **OPTIONS**

  The `OPTIONS` method is used to describe the communication options for the target resource.

8. **TRACE**

  The `TRACE` method performs a message loop-back test along the path to the target resource.

9. **PATCH**

  The `PATCH` method is used to apply partial modifications to a resource.

The two most commonly used methods for websites though, are **GET** and **POST**.

GETs are sometimes called safe methods, since they are only used to retrieve existing data from the database, whereas POSTs call for data to be added, removed, or changed on a server.

We know that the client prefixes requests to the server with HTTP verbs. So, how does the server reply?

**Status codes** are the server's reply to a client as to what happened after a specific request. In addition to a status code, a server can also supply any requested resources that the client requested, such as HTML, CSS and JavaScript, and media files such as images and audio.

Some common response codes are:
1. **200**, which indicates a *successful* GET request
2. **301**, which is a permanent *redirect*, used to send a browser to a different URL
3. **404**, which indicates that we were looking for a file on the server, and the server couldn't find it.
