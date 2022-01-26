# KeyRing

This is the backend for a secure login storage and retrieval system. KeyRing uses a redis server on the local machine to store and retieve login information. 
Data is encrypted before being stored in the database, and redis is configured to deny requests from remote machines. This rather simple implementation will serve as a foundation for a full fledged password storage web service/app.

KeyRing is intended to be proof-of-concept ONLY

I DO NOT RECCOMMEND STORING YOUR PASSWORDS/LOGIN INFORMATION IN ANY HOMEBREWED SYSTEMS SUCH AS THIS ONE, ENCRYPTION NOTWITHSTANDING
