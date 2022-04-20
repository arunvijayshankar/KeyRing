# Taqqiq

A CLI for secure login storage and retrieval. Taqqiq uses a redis server on the local machine to store and retieve login information. 
Data is encrypted before being stored in the database, and redis is configured to deny requests from remote machines. This rather simple implementation will serve as a foundation for a full fledged password storage web service/app.

I DO NOT RECOMMEND STORING YOUR PASSWORDS/LOGIN INFORMATION IN ANY HOMEBREWED SYSTEMS SUCH AS THIS ONE, ENCRYPTION NOTWITHSTANDING
